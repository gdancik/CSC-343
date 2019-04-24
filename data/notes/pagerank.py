#######################################################
# Modified by Garrett Dancik
#######################################################

#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


"""
This is an example implementation of PageRank, for demonstration purposes;
For an efficient implementation, see GraphX:
    https://spark.apache.org/docs/latest/graphx-programming-guide.html
"""


import pyspark


# Initialize the spark context.
sc = pyspark.SparkContext(appName="PythonPageRank")


# returns list of (url, contribution) tuples to each url 
def computeContribs(urls, rank):
    """Calculates URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    contributions = []
    for url in urls:
        contributions.append( (url, rank/num_urls ) )
    return contributions



########################################################
# input has format:
#         URL   neighbor URL
########################################################
urls = [ "Page1 Page3",
         "Page2 Page1",
         "Page3 Page1",
         "Page3 Page4",
         "Page4 Page1",
         "Page4 Page2"]
    
    
# create RDD in format (URL, [neighbors])
links = sc.parallelize(urls)
links = links.map(lambda x: x.split()).map(lambda x: (x[0], x[1])).distinct().groupByKey()

# after groupBy, value is iterator; let's convert to a list
links = links.mapValues(lambda x: list(x))
links.collect()
   

# Initialize rank of each URL to 1
ranks = links.map(lambda x: (x[0], 1.0))
ranks.collect()

# Calculates and updates URL ranks continuously using PageRank algorithm.
#   (10 iterations are used)
for iteration in range(10):
    
    # create RDD of form: (url, (neighbors, rank)
    contribs = links.join(ranks)
    contribs.collect()
    
    # create RDD of form: (url, contributed rank)
    contribs = contribs.flatMap( #neighbor urls,  rank
            lambda x: computeContribs(x[1][0], x[1][1]))

    # Re-calculates URL ranks based on neighbor contributions, by
    #     summing contributions to each url (reduceByKey)
    #     rank = .85*contributions + 0.15 (mapValues)
    ranks = contribs.reduceByKey(lambda v1,v2:v1+v2).mapValues(lambda rank: rank * 0.85 + 0.15)
    ranks.collect()


# Output final URL ranks
for link, rank in ranks.collect():
    print(link, "has rank:", rank)



sc.stop()
