#########################################################################
# A dictionary is a Python object for storing key-value pairs, such as
# word-definition pairs, though this need not be the interpretation 
# With a dictionary, it is easy to look up a 'key' and get the 'value'
# Note that keys MUST be unique and immutable
# More info: http://www.tutorialspoint.com/python/python_dictionary.htm
#########################################################################

# format for setting up a dictionary:
d = {"Key1": "Value1", "Key2": "Value2"}
print("dictionary: ", d)
print("d['Key1'] = ", d['Key1'])
print()

# more practical example
email = {"Dancik": "dancikg@easternct.edu", 
	  "Tasneem": "TasneemS@easternct.edu",
	  "Rosiene": "RosieneJ@easternct.edu",
	  "Tu": "tuH@easternct.edu",
	  "Lin:": "LINJ@easternct.edu"}

print("keys = ", email.keys())
print()

# we can add a new value
email['Gao'] = "GaoK@easternct.edu" 
print ("keys = ", email.keys())
print()

print("Please e-mail Dr. Dancik at " + email["Dancik"])
print()

# Note: looking up a 'key' that does not exist will give you an error
# email['Smith']
# You may need to confirm that the key exists first
if 'Smith' in email :
    print("Smith:", email['Smith'])
else :
    print("'Smith' is not in the dictionary")
print()


# you can specify default values for keys that don't exist, and look up values
# using the 'get' method
print("Dancik:", email.get("Dancik", "E-mail Not Found"))
print("Smith:", email.get("Smith", "E-mail Not Found"))



################################################################
# Javascript Object Notation (JSON) is a common data format
# used to express objects as attribute-value pairs. JSON is 
# commonly used to transfer data across the internet. 
# For example, twitter data is stored in JSON format:
# http://tinyurl.com/y6wdvjx6
# A JSON viewer is available here: http://jsonviewer.stack.hu/

# In Python, use the json module to convert JSON objects to 
# Python dictionaries
################################################################

import json

##########################
# simple example
##########################

# JSON format requires that property names are in double quotes 
student = '{"first":"Sarah", "last":"Parker", "age":17}'
studentDict = json.loads(student)

# look up student information in dictionary (Note: these are not
# printed; to display these values, execute commands in the console 
# rather than running the entire script)
studentDict['first']
studentDict['last']


##########################
# Twitter example
##########################

tweet = """
{
  "created_at": "Thu Apr 06 15:24:15 +0000 2017",
  "id_str": "850006245121695744",
  "text": "1\/ Today we\u2019re sharing our vision for the future of the Twitter API platform!\nhttps:\/\/t.co\/XweGngmxlP",
  "user": {
    "id": 2244994945,
    "name": "Twitter Dev",
    "screen_name": "TwitterDev",
    "location": "Internet",
    "url": "https:\/\/dev.twitter.com\/",
    "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ \u2328\ufe0f #TapIntoTwitter"
  },
  "place": {   
  },
  "entities": {
    "hashtags": [      
    ],
    "urls": [
      {
        "url": "https:\/\/t.co\/XweGngmxlP",
        "unwound": {
          "url": "https:\/\/cards.twitter.com\/cards\/18ce53wgo4h\/3xo1c",
          "title": "Building the Future of the Twitter API Platform"
        }
      }
    ],
    "user_mentions": [     
    ]
  }
}
 """

# json.loads does not allow newline characters in the string by default,
# so let's delete all newlines (this is how data is really generated)
tweet = tweet.replace("\n", "")
tweetDict = json.loads(tweet)

# look at tweet, with data stored in a dictionary
tweetDict.keys()
tweetDict['created_at']
tweetDict['text']

# each element of 'entities' is another dictionary
type(tweetDict['entities'])
tweetDict['entities']

# looking up 'urls' in the 'entities' dictionary, we get a list
# (a list of dictionaries)
type(tweetDict['entities']['urls'])
tweetDict['entities']['urls']

