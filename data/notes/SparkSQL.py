####################################################################
# SparkSQL - Spark module that provides a Data Frame API, so that
#   records can be treated as data from a table
####################################################################

# import pyspark modules
import pyspark
from pyspark.sql import SQLContext

#import pandas module for data frames
import pandas as pd  


# create Spark Context and SQLContext
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)


########################################################
# Spark Data Frame Basics
########################################################

# create a Spark DataFrame from a list
df = sqlContext.createDataFrame([1,2,3,43,2], "Int")

# the data frame is made up of rows
df.take(2)

# show the specified number of rows
df.show(3)


# create Spark DataFrame from a list of tuples, and corresponding
# column names
df = sqlContext.createDataFrame([('Mary', 18), ('Joe', 20)], 
                                 ['name', 'age'] )

# get list of columns
df.columns

# show data types of each column
for t in df.dtypes :
    print(t)

# get the first row
row = df.first()
row

# you can access row elements using dot (.) notation
row.name
row.age    


# create Spark DataFrame from a pandas data frame
d = {'name': ['Joe', 'Mary', 'Anna', 'Zak'],
     'age': [20,18,18,19]}
pdf = pd.DataFrame(d)

df = sqlContext.createDataFrame(pdf)

df.show(3)
df.collect()
df.count()


########################################################
# Spark Data Frames can be queried 
########################################################

# 'select' example
df.select("age").show()

# 'where' example
df.select("age").where("age>18").show()

# column names can be referenced using dot (.) notation
df.select(df.age).where("age>18").show()

# sort example
df.select(df.age).where("age>18").sort(df.age.desc()).show()


# register a table to use any SQL query
df.registerTempTable("students")
sqlContext.tableNames()

# use 'sql' method with valid SQL query
sqlContext.sql("Select * from students").show()
sqlContext.sql("Select name as firstName from students").show()


# use .rdd to convert to standard RDD, where each record is 
# a 'Row' object and where columns can be accessed using 
# dot (.) notation
df.rdd.collect()

# create pair RDD where the key is the age and the value is 1
rdd = df.rdd.map(lambda x: (x.age, 1))
rdd.collect()

# count by key
rdd.countByKey()

##################################################################
# SparkSQL allows you to load data from a variety of sources,
# including csv, text, and json files, and from other databases
##################################################################

# set file to correct location
file = '2015-12.csv'

# specify the schema, in form of column1 type1, column2 type2, etc
schema = 'id BIGINT, date DATE, state STRING, make STRING, color STRING, code STRING, amt INT'

# read in a csv file and specify the schema
citations = sqlContext.read.csv(file, schema )

# look at the first 5 rows
citations.show(5)


##################################################################
# Questions: 
# 1) How many citations are there?
# 2) Use the Spark Data Frame 'where' method and find the
#    number of citations that were issued to cars with CT 
#    plates?
# 3) Use the 'where' method to show up to 5 citations for
#    CT cars where the amount was more than $100
# 4) Use the 'select' and 'where' method to show the id, state,
#    make, and amount for citations issued to CT cars
# 5) Register a temporary table from the citations Data Frame.
# 6) Show the 5 states and the corresponding number of citations
#    for the states with the most citations
# 7) Repeat number (6) but for car types (makes) rather than 
#    states
################################################################




