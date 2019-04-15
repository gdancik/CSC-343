#########################################################
# Data in a RDD consists of records that are 
# partitioned across worker nodes
#########################################################

import pyspark
sc = pyspark.SparkContext()

# map function needs to return a generator
# https://realpython.com/introduction-to-python-generators/
def f(splitIndex, iterator) :
     yield (splitIndex, list(iterator))


#########################################################
# use default number of partitions (this will vary by 
# environment)
#########################################################
r = range(20)
rdd = sc.parallelize(r)

# look at first 3 records
rdd.take(3)

# output the number of partitions
num_partitions = rdd.getNumPartitions()
print("num partitions:", num_partitions)

# map each partition so we can view it
rdd = rdd.mapPartitionsWithIndex(f)
partitions = rdd.collect()
for p, vals in partitions :
    print(p, ": ", vals, sep = "")



#########################################################
# use (minimum of) 2 partitions
#########################################################
r = range(20)
rdd = sc.parallelize(r, 2)

# look at first 3 records
rdd.take(3)


# output the number of partitions
num_partitions = rdd.getNumPartitions()
print("num partitions:", num_partitions)

# map each partition so we can view it
rdd = rdd.mapPartitionsWithIndex(f)
partitions = rdd.collect()
for p, vals in partitions :
    print(p, ": ", vals, sep = "")


######################################################
# stop the Spark Context
######################################################
sc.stop()
