# 1. Name: 
#    Andrew Nerdin
# 2. Assignment Name: 
#    Lab 04: Monopoly
# 3. Assignment Description:
#    A program in Python that informs the user if he or she 
#    is able to build a hotel on Pennsylvania Avenue. 
# 4. What was the hardest part? Be as specific as possible.
#    
# 5. How long did it take for you to complete the assignment?
#    

def main():
    #create hotel and end_turn variable.
    hotel = 0
    end_turn = 0

    #loop through the prompts until we get a hotel.
    while hotel != 1 | end_turn == 0:

        #user input for all green property.
        property = str(input("Do you own all the green properties? (Y/N)"))

        #Checks response for output.
        if property == "N":
            print("You cannot purcahse a hotel until you own all the properties of a given color group.")
            end_turn = 1
        elif property != "Y" | property != "N":
            print("Please enter the proper response.")
            property = str(input("Do you own all the green properties? (Y/N)"))
        
        #user input for Pennsylvania Avenue.
        penn = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, or 5:a hotel"))

        #check response for PA output.
        if penn == 5:
            print("You cannot purcahse a hotel if the property already has one.")
            hotel = 1
        elif penn < 5 | penn > 0:
            print("Please enter the proper response.")

        #user input for North Carolina.
        carolina = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, or 5:a hotel"))

        #checks response for NC output.
        if carolina == 5:
            print("Swap North Carolina's hotel for Pennsylvania's 4 houses.")
            end_turn = 1
        elif carolina < 5 | carolina > 0:
            print("Please enter the proper response.")
            carolina = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, or 5:a hotel"))
            
        #user input for Pacific Avenue.
        pacific = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, or 5:a hotel"))

        #checks response for PC output.
        if pacific == 5:
            print("Swap Pacific's hotel for Pennsylvania's 4 houses.")
            end_turn = 1
        elif pacific < 5 | pacific > 0:
            print("Please enter the proper response.")
            pacific = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, or 5:a hotel"))

        #user input for available hotels
        buy_hotels = int(input("How many hotels are there to purchase?"))

        #checks response for No Hotels output.
        if buy_hotels == 0:
            print("There are not enough hotels available for purchase at this time.")
            end_turn = 1
        elif buy_hotels > 0 | buy_hotels < 12:
            print("Please enter the proper response.")
            buy_hotels = int(input("How many hotels are there to purchase?"))


if __name__ == "__main__":
    main()        