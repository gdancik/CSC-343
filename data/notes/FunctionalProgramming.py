##################################################################
# In true functional programming, all code consists of functions
# (in the mathematical sense). A function maps inputs to outputs
# and does nothing else (e.g., does not output anything or change
# the state of any variable)

# Here we cover some basic functional programming concepts
##################################################################

# example function which squares a number
def square(x) :
    return x*x

square(3)

##################################################################
# The lambda function syntax is based on 'lambda calculus', 
# \lambda inputs.expression, e.g. \lambda x.x*x, which has the
# basic structure of input --> output
# In python, the syntax is
# lambda input : expression
# and the statement cannot span multiple lines.
# The main motivation is that lambda functions can be anonymous, 
# as described in a later example
##################################################################

# lambda function, x --> x*x
square = lambda x : x*x
square(3)

# lambda function, x,y --> x + y
add2 = lambda x,y : x+ y
add2(3,4)


##################################################################
# The map function has the format map(func, iter) and applies 
# the function 'func' to each element of the iterator 'iter', 
# and returns a new iterator with each element replaced by 
# func(elememnt)

# Note: you can think of an iterator as a pointer to a collection 
# of elements; the iterator can only move forward through the
# collection and always starts where it left off
##################################################################

# create a list of numbers
l = [11,3,5,4]

# the first argument to the map function is a function, which can be named
m = map(square, l)
list(m)


# ... but we can do the same thing using an anonymous 
# (unnamed) lambda function
m = map(lambda x: x*x, l)
list(m)

#####################################################################
# The filter function has the format filter(func, iter) and applies 
# the function 'func' to each element of the iterator 'iter', 
# and returns a new iterator that keeps only those elements where
# func(element) is True.
#####################################################################

f = filter(lambda x : x >= 5, l)
list(f)


###########################################################################
# Use filter and map to square only those numbers that are greater than 5
###########################################################################

# first filter the values
f = filter(lambda x : x >= 5, l)

# then map the filtered values
m = map(lambda x : x*x, f)
list(m)


############################################################################
# Since the output of 'filter' is input to 'map', we can use a single 
# statement
############################################################################
m = map(lambda x : x*x, filter(lambda x: x >= 5, l))
list(m)


#####################################################################
# The reduce function applies a rolling computation to a sequential
# pairs of values in a collection, and returns the reduced value.
# The reduce function has teh format reduce(func, iter, initial), 
# where initial is an optional value pre-pended to the iterator
#####################################################################

# required for 'reduce'
from functools import reduce

# the sum of numbers in our list:
sum(l)

# sum of numbers calculated using the 'reduce' function
r = reduce((lambda x, y: x + y), l)
r


# Let's look at what 'reduce' is doing
def addAndOutput(x,y) :
    print("Adding",x, "and", y)
    return x+y

print("list is:", l)
r = reduce(addAndOutput, l)

