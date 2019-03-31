##################################################################
# Lab 8: Functional Programming, Dictionaries
##################################################################


# 1. Using 'def' notation, write a function called 'wordCount'. The
#    function has one parameter (asssumed to be a string) and 
#    returns the number of words in the string. Assume that a word 
#    is any sequence of characters separated by white space. 
#    For example, if the string is "this is a string", then the 
#    function will return 4. Use your function to test that 
#    it works correctly when "this is a string" is passed to it.


# 2. Rewrite your function using lambda notation.


# 3. Using lambda notation, write a function called 'first' that has 
#    one parameter, assumed to be a list, and returns the first 
#    element of the list. 


# 4. Use the 'map' function and the built-in 'len' function to
#    find the length of the words in the list below. Convert the iterator
#    returned by 'map' to a list and output the result.
words = ['down', 'up', 'left', 'right']


# For the next set of questions, you must use an anonymous function
# (i.e., use lambda notation) with 'map', 'filter', or 'reduce'.
# When using 'map' or 'filter', output the results of the
# transformation, either by converting the iterator to a list and/or iterating 
# through each result to output it.


# 5. Use the 'map' function to count the number of words in each string.
#    For example, the list 'strings' below should map to [3,1,2,1].

strings = ['big data programming','tacos', 'web development', 'kfc']


# 6. Use the 'filter' function to create a list of 'CSC' courses from
# the 'courses' list below, and then output the number of 'CSC' courses
# in the list.

courses = ['CSC-450', 'MAT-243', 'CSC-343', 'ART-100']

# 8. Use appropriate map and filter functions to extract the city for
#    all cities in Connecticut from the records below. Assume all 
#    records have the format 'city, state', and that CT could appear
#    anywhere in the record.

records = ['Hartford, CT', 'Willimantic, CT', 'Pheonix, AZ', 'Boise, ID']

# 9. This semester, I am teaching the following courses
#    CSC 343-01, 11-11:50
#    CSC 314-01, 1-1:50
#    CSC 314-02, 2-2:50

# Create a Python dictionary named schedule where the key is the course I
# am teaching (e.g., CSC 343-01) and the value is the corresponding time
# (e.g., 11-11:50). Then use the dictionary to output when I am teaching
# CSC 343-01.    


# 10. Information about the book 'Eloquent Javascript, Second Edition' is
#     stored in the JSON formatted string below. Convert the JSON to a
#     dictionary and output the title of the book and the author.

book1 = """{"isbn": "9781593275846","title": "Eloquent JavaScript, Second Edition",
            "subtitle": "A Modern Introduction to Programming",
            "author": "Marijn Haverbeke",
            "published": "2014-12-14T00:00:00.000Z",
            "publisher": "No Starch Press",
            "pages": "472"}"""
      

# Wikipedia has an Application Programming Interface (API) for retreiving 
# JSON formatted information from its pages. The code below connects to
# wikipedia and converts the results to a python dictionary object 
# named 'wiki' (Note: you need an internet connection for this step)
# You can see a nicely formatted version of the JSON results here:
# https://en.wikipedia.org/api/rest_v1/page/summary/Big_data

import requests
import json
res = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/Big_data')
wiki = json.loads(res.content.decode())

# 11. Print out the page summary, which is stored under 'extract'


# 11. Print out the source URL of the original image




