#######################################################################
# Word count example in pyspark
#######################################################################

import pyspark
sc = pyspark.SparkContext(appName = 'wordcount')

################################################################
# Read in the data
################################################################
lines = ["Dorothy lived in the midst of the great Kansas prairies,",
         "with Uncle Henry, who was a farmer, and Aunt Em, who was", 
         "the farmer's wife. Their house was small, for the lumber", 
         "to build it had to be carried by wagon many miles.  There",
         "were four walls, a floor and a roof, which made one room;"
         "and this room contained a rusty looking cookstove, a",
         "cupboard for the dishes, a table, three or four chairs,"
         "and the beds."]

rdd = sc.parallelize(lines)

# TO DO: look at the first 3 lines


################################################################
# Pre-processing the data
################################################################



# TO DO: transform the RDD into a new one (also called 'rdd')
# with only lowercase characters


# TO DO: transform the RDD into a new one (also called 'rdd')
# with all punctuation removed


# create a translation table that deletes all punctuation
import string
t = str.maketrans('', '', string.punctuation)



################################################################
#  Map each line to a list of words, then flatten 
# (i.e., make each word its own record in the RDD) 
################################################################

rdd = rdd.flatMap(lambda x: x.split())


################################################################
# To apply map-reduce, make each word to a key with the value 1: 
#   (word, 1)
################################################################
rdd = rdd.map(lambda x: (x,1))


################################################################
# Apply 'reduce' step by adding the values for each key
################################################################
rdd = rdd.reduceByKey(lambda v1,v2 : v1+v2)

# TO DO: how many unique words are there?

# TO DO: What are the counts for the first 3 words?

################################################################
# Stop the Spark Context
################################################################
sc.stop()
