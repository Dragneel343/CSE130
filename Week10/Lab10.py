# 1. Name:
#      Andrew Nerdin
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program will prompt the user for a positive 
#      integer n and then display the nth François number.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was figuring out the while loop.
#      Then after asking the discussion board i realized i didnt need it.
# 5. How long did it take for you to complete the assignment?
#    coding plus the video, roughly 3.5 hours

#prompt user for number
number = input("Which Francois number would you like to see? ")

assert number.isnumeric()
number = int(number)

assert number > -1

assert number < 100000
    
francois = [1,2]

if number > 2:
    for x in range(3,number + 1):
        francois[x % 2] = francois[0] + francois[1]
    
        
value = francois[number % 2]

print('Francois number '+ str(number) +' is '+ str(value) + '.')