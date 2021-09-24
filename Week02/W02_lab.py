# 1. Name: 
#    Andrew Nerdin
# 2. Assignment Name: 
#    Lab 02: Authentication
# 3. Assignment Description:
#    A program in Python that reads the contents of the file into a list. 
#    The program will then prompt the user for a username and password. 
#    Finally, we will tell the user whether the user is authenticated.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part was probably the authentification, 
#    mostly due to me doing it differently at first and then changing.
# 5. How long did it take for you to complete the assignment?
#    approx. 2.5 hrs

import json

try:
    #Read from the JSON file
    with open('Week02/Lab02.json') as file:

        #Reads the file into text.
        text = file.read()

        #Converts text file into JSON.
        my_json = json.loads(text)

    #Pulls the list of username and list of passwords.
    usernames = my_json['username']
    passwords = my_json['password']

    #print(usernames)
    #print(passwords)

    #User entrs input.
    username = input("Username: ")
    password = input("Password: ")

    #Authenticate username and password.
    for i in range(len(usernames)):
        if username == str(usernames[i]) and password == str(passwords[i]):
            print("You are authenticated!")
        else:
            print("You are not authorized to use the system.")

except FileNotFoundError:
    print("Unable to open file Lab02.json.")