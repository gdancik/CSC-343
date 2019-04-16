#####################################################
# RDD persistence example
#####################################################

import pyspark
import time

sc = pyspark.SparkContext(appName='persist')


#############################################################################
# read in citation data, count total number of citations, and total
# number of citations on Christmas, summarize states that are
# cited on Christmas
#############################################################################

file = '2016-12.csv'

# Specifies RDD lineage: 
# (1) read data from file
rdd = sc.textFile(file)

# Action requires execution of entire lineage
# (1) read data from file
# Then count the number of records (which is the number of lines in the file)
rdd.count()

# is rdd cached?
rdd.is_cached

# Addition to RDD lineage:
# (2) filter data to include only citations from 12/25/2016
rdd = rdd.filter(lambda x: x.split(',')[1] == '2016-12-25')

# Action requires execution of entire lineage
# (1) read data from file
# (2) filter data to include only citations from 12/25/2016
# Then count the number of records (number of citations on 12/25/2016)
rdd.count()


# Addition to RDD lineage:
# (3) create pair RDDs where key = state and value = original record 
rdd = rdd.keyBy(lambda x: x.split(',')[2])


# Action requires execution of entire lineage
# (1) read data from file
# (2) filter data to include only citations from 12/25/2016
# (3) create pair RDDs where key = state and value = original record 
# Then return dictionary counting number of results by key
rdd.countByKey()

###########################################################################
# persist will store rdd in memory (by default)
###########################################################################

# This rdd will persist (in memory) the next time it is computed
rdd.persist()
rdd.is_cached

# Action requires execution of entire lineage, but RDD is stored in memory
# (1) read data from file
# (2) filter data to include only citations from 12/25/2016
# (3) create pair RDDs where key = state and value = original record 
# The RDD in (3) is set to persist, so this RDD is stored in memory
# Then return dictionary counting number of results by key
rdd.count()

# Action requires execution of lineage, starting with last persistent RDD,
# which is the RDD in lineage step (3)
# (1) (NOT EXECUTED) read data from file
# (2) (NOT EXECUTED) filter data to include only citations from 12/25/2016
# (3) (NOT EXECUTED) create pair RDDs where key = state and value = original record 
# Uses 'rdd' from memory to return a dictionary counting results by key
rdd.countByKey()



###########################################################
# Function that times how long it takes to 
###########################################################

def time_rdd(file, persist = False) : 
    start = time.time()
  
    rdd = sc.textFile(file)

    # count total number of citations
    rdd.count()

    # filter citations to include only those given on Christmas
    rdd = rdd.filter(lambda x: x.split(',')[1] == '2016-12-25')
 
    # if specified, persist this rdd
    if persist :
        rdd.persist()

    # count the total number of citations (on Christmas)
    rdd.count()

    # get number of citations per state on Christmas
    rdd.keyBy(lambda x: x.split(',')[2]).countByKey()

    end = time.time()
    
    return end - start




# lists to store times
t1 = []
t2 = []

r = range(1,11) 
for num in r :
    print("Iteration #", num)
    
    #time execution without persistence
    time1 = time_rdd(file, False)
    t1.append(time1)
    
    # time execution with persistence
    time2 = time_rdd(file,True)
    t2.append(time2)

    

######################################################################
# Compare execution times with and without persistence
######################################################################
    

# import libraries for plotting
import matplotlib.pyplot as plt
import pandas as pd
 
# Data
df=pd.DataFrame({'num': r, 't1': t1, 't2': t2})
 
# multiple line plot
plt.plot( 'num', 't1', data=df, color='blue', label = 'persistence=no')
plt.plot( 'num', 't2', data=df, marker='', color='maroon', label = 'persistence=yes')
plt.xlabel("iteration #")
plt.ylabel("time (seconds)")

plt.legend()


# stop the Spark Context
sc.stop()









