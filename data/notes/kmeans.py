
########################################################################
# Modified by Garrett Dancik
########################################################################

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
The K-means algorithm written from scratch against PySpark. In practice,
one may prefer to use the KMeans algorithm in MLlib, as shown in
examples/src/main/python/mllib/kmeans.py.

This example requires NumPy (http://www.numpy.org/).

This is a k-means clustering example for demonstration purposes; 
for a more efficient implementation, the Spark MLib package
is recommended: https://spark.apache.org/docs/latest/mllib-clustering.html#k-means
"""

import numpy as np
from pyspark import SparkContext
import matplotlib.pyplot as plt


##############################################################################
# plots points and centers, and color codes by groups
##############################################################################
def plotPoints (points, centers, groups, groupCenters, title, index = 0 ) :

    if len(centers) != 2 :
        raise("Error: plotting function requires 2 centers")

    
    if index != 0:
        plt.subplot(2,3,index)
        
    # get x- and y- values
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    colors = 'green'
    if groups :
        color_num = [g for g in groups]
        colors = [['blue','red'][c] for c in color_num]

    plt.scatter(x,y, color = colors, label = "observations")
    
    if centers :    
        xCenter = [c[0] for c in centers]
        yCenter = [c[1] for c in centers]
        colors = 'green'
        if groups :
            colors = ['blue','red']
        plt.scatter(xCenter, yCenter, marker = "*", color = colors, s = 100, 
                    label = "centers")
    plt.title(title)
    plt.legend(loc = "upper left")
    

##############################################################################
# returns the index of the closest center to point p
##############################################################################
def closestPoint(p, centers):
    bestIndex = 0
    closest = float("+inf")
    for i in range(len(centers)):
        # distance from point to center
        tempDist = np.sum((p - centers[i]) ** 2)
        
        # check if this center is closest
        if tempDist < closest:
            closest = tempDist
            bestIndex = i
    return bestIndex



sc = SparkContext(appName="PythonKMeans")


# generate data and create RDD
points = [ [1,1], [2,2], [2,3], [10,10], [10,11], [11,12]]
data = sc.parallelize(points)
data = data.map(lambda x: np.array(x))
data.collect()


K = 2  # number of centers
convergeDist = 0.002 # convergence threshold

# randomly select K points to use as centers
kPoints = data.takeSample(False, K, 3)


# run code below generate plots in new window
# %matplotlib auto


groups = None
groupCenters = None
plt.figure(1)
plotPoints(points, kPoints, groups, groupCenters, "Initial centers")


index = 1
tempDist = 1.0
plt.figure(2)
while tempDist > convergeDist:
    
    ######################################################################
    # Find all points closest to each center
    ######################################################################

    # transform to (closestPointIndex, point, 1)
    closest = data.map(lambda p: (closestPoint(p, kPoints), (p, 1)))
    closest.collect()

    groups = closest.map(lambda x: x[0]).collect()

    plotPoints(points, kPoints, groups, groupCenters, 
               "Find points closest to each center", index)    
    index+=1
    
    ##########################################
    # find the center of each cluster
    ##########################################

    # for each key, add points and count them
    pointStats = closest.reduceByKey(
            lambda p1_c1, p2_c2: (p1_c1[0] + p2_c2[0], p1_c1[1] + p2_c2[1]))
    
    # find new centers by averaging 
    newPoints = pointStats.map(lambda st: (st[0], st[1][0] / st[1][1]))
    newPoints.collect()
    
    centers = newPoints.map(lambda x: x[1]).collect()
    groupCenters = newPoints.map(lambda x: x[0]).collect()

    plotPoints(points, centers, groups, groupCenters, "Update centers", index)
    index += 1
    
    newPoints = newPoints.collect()
    
    # find distance in which centers move
    tempDist = sum(np.sum((kPoints[iK] - p) ** 2) for (iK, p) in newPoints)

    # set new centers
    for iK, p in newPoints:
        kPoints[iK] = p

print("Final centers: " + str(kPoints))



sc.stop()
