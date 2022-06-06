# Sample Code for Lab 4

# Sample Code to Remove Punctuation

import string
  
# the string module includes punctuation characters
print("punctuation characters:", string.punctuation)

# create a translation table, which says to delete all characters specified in
# the third argument (i.e., to delete all punctuation)
t = str.maketrans('', '', string.punctuation)

# example string
s = "Look! Hey!?"

# call the translate function which translates string based on the translation table
# in this case, all punctuation is removed
new_s = s.translate(t)

print(s)
print(new_s)


# Sample code to work with a set (a collection of unique values)

# If you have a list, you can remove duplicate values by converting to a set
l = ['a','b','c','a'] # create a list containing 'a','b','c', and 'a'
s = set(l) # convert from a list to a set, which will contain only 'a','b',and 'c'
print(s)
print(','.join(s)) # print a comma-separated string of values

# You can keep a set of unique values as you go, by starting with an empty set 
s = set() # start with an empty set
s.add('a') # add an 'a'
s.add('b') # add a 'b'
s.add('a') # 'a' is not added, since it already exists in the set
print(s)  # the set contains only 'a','b'

