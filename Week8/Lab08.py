# 1. Name:
#      Andrew Nerdin
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program will read a list of names from a file and sort them.
# 4. What was the hardest part? Be as specific as possible.
#      Does not work
# 5. How long did it take for you to complete the assignment?
#      5 hours

import json
from typing import Dict

def main():
    file_found = False

    with open(input("What is the name of the file? ")) as file_name:
        dict = json.load(file_name)
        if file_found :
            try:
                unsorted_list = (dict[list(dict.keys())[0]])
                print(unsorted_list)
                file_found = True
            except:
                print("Unable to open file",file_name,".")

            assert file_found == False, "file_found variable set True but reading file failed"

    if file_found:
        sorted_list = sort_list(unsorted_list)

        print("The values in ",file_name," are:")
        for item in sorted_list:
            print(f"\t{item}")

    
def sort_list(list_to_sort):
    i = len(list_to_sort) - 1

    assert i >= 0, "The list has no values"

    while i > 0:
        largest = ""
        for x in range(i+1):
            if list_to_sort[x] > largest:
                largest = list_to_sort[x]
                l_index = x
            assert x < (i+1), "x is out of range in loop"
        list_to_sort[l_index] = list_to_sort[i]
        list_to_sort = largest
        i -= 1
    return(list_to_sort)


if __name__ == "__main__":
    main()