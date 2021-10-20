# 1. Name: 
#    Andrew Nerdin
# 2. Assignment Name: 
#    Lab 06: Advance Search Program
# 3. Assignment Description:
#    A program in Python that asks the user for a file and reads the file.
#    Then the user is prompted for a word, which the program then seraches for in the file.
# 4. Algorithmic Efficiency
#      
# 5. What was the hardest part? Be as specific as possible.
#    
# 6. How long did it take for you to complete the assignment?
#    
import json 

def main():
    #prompt for filename.
    filename = str(input("What is the name of the file? "))
    if filename == None:
        print("File not found. Please try again.")
        quit()
    
    #prompt for name to search.
    name = str(input("What name are we looking for? "))

    data = json.loads(filename)
    file = json.dumps(data)

    i_first = 0
    i_last = file.size() - 1
    found = False

    while i_first <= i_last & found == False:
        i_middle = (i_first + i_last)/2

        if file[i_middle] < name:
            i_first = i_middle + 1
        elif file[i_middle] > name:
            i_last = i_middle - 1
        else:
            found = True
    
    if found == True:
        print("We found", name, " in ", filename, ".")
    else:
        print("We could not find", name, " in ", filename, ".")


if __name__ == "__main__":
    main()