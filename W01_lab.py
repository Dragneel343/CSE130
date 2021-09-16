# 1. Name: 
#    Andrew Nerdin
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    a program in Python that displays a message on the screen, 
#    prompts the user for information, makes a decision, stores data in a list, and loops
# 4. What was the hardest part? Be as specific as possible.
#    The overall project was relatively easy, I forgot to add int() to the user inputs which casued some problems
#    then it was a matter of just fine tuning the overall program. LOL the biggest problem was the infant strapped to my chest
#    distracting me from coding.
# 5. How long did it take for you to complete the assignment?
#    Hour and a half, more or less.
import random

# Game introduction
print('This is the "guess a number" game.')
print('You try and guess a random number in the smallest number of attempts')
print()

# Prompt the user for how difficult the game will be. Ask for an integer
value_max = int(input('Pick a positive integer: '))
#error handling
if value_max <= 1 :
    print('The number entered was not a positive integer! Try again!')
    value_max = int(input('Pick a positive integer: '))

# Generate a random number between 1 and the chosen value
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing
print('Guess a number between 1 and',value_max,'.')

# Initialize the sentinal and the array of guesses
guesses = []
guess = 0
while guess != value_random:

# Play the guessing game

    # Prompt the user for a number
    guess = int(input('> '))

    # Store the number in an array so it can be displayed later
    guesses.append(guess)

    # Make a decision: was the guess too high, too low, or just right
    if guess > value_random:
        print('\tToo high!')

    elif guess < value_random:
        print('\tToo low!')

# Give the user a report: How many guesses and what the guesses were
print('You were able to find the number in', len(guesses), 'guesses.')
print('The numbers you guessed were: ',guesses)