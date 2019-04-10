##########################################################################
# Lab 10: PySpark with Paired RDDs
##########################################################################

import pyspark
sc = pyspark.SparkContext(appName = "Lab 10")

# Use the paired RDD created below to answer the first set of questions. 
# Note that each record in the RDD will be a tuple,
# which consists of a key (state) and a value (city).

records = [ ('CT', 'Hartford'), ('CT', 'Willimantic'),  ('AZ', 'Pheonix'), 
           ('ID', 'Boise')]
rdd = sc.parallelize(records)
rdd.count()


# 1. Use the 'keys' and 'distinct' methods to get a list of all of the states,
#    with no duplicates, and print out the list.

# 2. Use the 'countByKey' method to find the number of records for each state.
#    Note that 'countByKey' returns a 'defaultdict'. A 'defaultdict' is a 
#    type of dictionary that has a default value (in this case the integer 0).
#    Loop through each element of the dictionary to output the state and 
#    corresponding frequency.


# 3. The code below groups the values of each key and converts the values
#    to a list ('groupByKey' returns the values as an iterable). 
#    Filter this result to include only those records where the state has 
#    more than 1 city.

rdd_by_key = rdd.groupByKey().mapValues(list)


# 4. In the code below, the records have the format city, state.
#    Transform the RDD so that each record contains a key-value pair, 
#    with the key the state and the value the city, as was used for 
#    question (1).
records = ['Hartford, CT', 'Willimantic, CT', 'Pheonix, AZ', 'Boise, ID']
rdd = sc.parallelize(records)

# 5. Using the la_parking_citations data from Lab 7, create an RDD named 'rdd'
#    from the data in 2015-12.csv. Then run the statement below to filter 
#    out the citations with invalid (non-numeric) amounts


# filter the RDD to contain only those amounts which are valid
rdd5 = rdd.filter(lambda x: x.split(',')[-1].isdigit())


# 6. Use an appropriate transformation or transformations to create an RDD 
#    where each record contains a key-value pair, where the key is the date 
#    and the value is the amount (the last column), stored as an integer. 
#    Note: if you do this correctly, the first record in the RDD will 
#    be ('2016-12-03', 93)


# 7. Use the 'sortByKey' method to create a new RDD where the results are
#    sorted by key (which will sort the dates alphabetically).

# 8. Use the 'countByKey' method to create a new RDD that includes the number
#    of citations for each date.


# 9. Apply appropriate transformations to your RDD from (7) so that the
#    first record of the RDD contains the date with the most citations.
#    Hint: since most operations are applied to the 'key', you may
#    want to create a new paired RDD with a different key than (7).

# 10. Use the 'reduceByKey' method to the RDD in (7) to find the total 
#    amount in citations per day. Note: for this to work, your amounts
#    must be converted to integers (which you should have done in (6))

# 11. The statements below takes the RDD from (5) and transforms it to include
#     a unique set of citation codes and amounts where amounts are more than 
#     $100. Read in the codes.csv file, and create a paired RDD where the
#     key is the code and the value is the description. Then join this RDD
#     to the one below to create a new RDD where the key is the code, and 
#     the value is a tuple containing the amount and the description.

# keep records where the citation amount > $100
rdd = rdd5.filter(lambda x: int(x.split(',')[-1]) > 100)

# create (key,value) tuples from the last 2 fields, where the
# key is the citation code and the value is the citation amount
rdd = rdd.map(lambda x: x.split(',')[-2:]).map(tuple).distinct()

# 12. Apply a transformation to the RDD from (11) so that each record in
#     the resulting RDD is a tuple where the key is the code and the 
#     value is the description only. Hint: you need to apply a 
#     transformation to the values only.


# stop the current SparkContext
sc.stop()

