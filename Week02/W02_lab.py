# 1. Name: 
#    Andrew Nerdin
# 2. Assignment Name: 
#    Lab 02: Authentication
# 3. Assignment Description:
#    A program in Python that reads the contents of the file into a list. 
#    The program will then prompt the user for a username and password. 
#    Finally, we will tell the user whether the user is authenticated.
# 4. What was the hardest part? Be as specific as possible.
#    -type here-
# 5. How long did it take for you to complete the assignment?
#    -type here-

import json

#Read the JSON file
with open('Week02/Lab02.json') as f:
    try:
        data_json = json.load(f)
    except:
        print("Unable to open file Lab02.json.")

#Convert JSON to string
data = json.dumps(data_json, indent=4, sort_keys=False)
print(data)