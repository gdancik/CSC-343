import pyspark
sc = pyspark.SparkContext(appName = "Lab 9")


# Use the RDD below to answer the first set of questions, which is
# generated from the 'records' list. When answering the questions, 
# assume that all records have the format 'city, state', and that CT 
# could appear anywhere in the record.

records = ['Hartford, CT', 'Willimantic, CT', 'Pheonix, AZ', 'Boise, ID']
rdd = sc.parallelize(records)
rdd.count()


# 1. Output the first record from this RDD

# 2. Output each record from this RDD

# 3. Apply a transformation to this RDD that creates a new RDD that contains
#    only the city for each record

# 4. Apply a transformation to this RDD that creates a new RDD that contains
#    the complete record (city, state) for those from CT.

# 5. In a single statement, starting with the original 'rdd' object, create 
#    an RDD containing the cities in CT


# 6. Using the la_parking_citations data from Lab 7, create an RDD from the
#    data in 2015-12.csv. Output the number of citations from this file

# 7. Get the first 3 citations

# 8. Create an RDD that includes only the amounts (the last column), then look
#    at the first five amounts.


# 9. If you look at the first 5 amounts from the RDD in (8), you will see that
#    one of the amounts is missing. In order to calculate the total amount for
#    all citations, we will need to remove missing and invalid amounts.  
#    In a single statement, remove invalid amounts and convert the valid 
#    amounts to integers. To this, the following will be useful: (1) to check 
#    whether an object 'val' is an integer, use val.isdigit() which will return 
#    true if all characters in 'val' are digits. To convert a string 's' to an 
#    integer, use 'int(s)'


# 10. Find the sum of the amounts from the RDD in (9) by applying the 'sum'
#     action to the rdd (e.g., rdd.sum()) (Note: you will get an error
#     if any of the RDD elements are not numeric))



import json

# 11.  Each line in the file 'stream.json' contains a JSON formatted
# tweet, which was streamed in real time on 3/31. Create an RDD that 
# stores each line in the file as a record in an RDD. How many 
# tweets are in the file?


# 12. Create an RDD that converts each JSON formatted tweet into
#     a Python dictionary


# 13. Some tweets, such as the first tweet, have been deleted. You
#     can see this by using rdd.first(). Remove the deleted tweets 
#     by filtering the RDD and keeping only those tweets where 
#     'delete' is not one of the keys of the dictionary. How many 
#     tweets are remaining?


# 14. Starting with the RDD from (13), keep all the tweets that are 
#     in english (where 'lang' is equal to 'en')


# 15. Create a new RDD that contains only the 'text' of each tweet,
#     and view the text of the first 5 tweets.


# 16. Starting with your RDD from (13), create an RDD that contains the 
#     name of each user



# stop the current SparkContext
sc.stop()

