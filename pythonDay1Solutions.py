# INPUT FUNCTION

# Take input of you and your neighbor
my_name = input("What is your name? ")
your_name = input("What is his name? ")

# Take how long each of you have been coding
my_months = input("How many months have I been coding? ")
your_months = input("How many months have you been coding? ")

# Add total month
total_months = int(my_months) + int(your_months)

# Print results
print(f"Wow! The two of you have been coding for {total_months} months!")

####################

# CONDITIONALS

# define variables
x = 1
y = 10
z = False

# if statement 

if not z:
    print("z is false")

# check if one value is equal to another
if x == 1:
    print("x is equal to 1")

# check if one value is NOT equal to another
if x != 1:
    print("x is not equal to 1")

# check if one value is less than another
if x < y:
    print("x is less than y")

# check if one value is greater than another
if y > x:
    print("y is greater than x")

# check if one value is greater than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

# checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned true")

# checks if either of two conditions is met using "or"
if x < 45 or y < 5:
    print("One or more of the statements were true")

# nested if statements: "if x is less than 10, check if y is less than 5. if this is true, print(), if not true, check if y is equal to 5....if not true print 
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")

# more conditional statement examples

# if 2 * x is greater than 10, print1, if not, print2
x = 5
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooh, needs some work")


# if the length of the word "dog" is less than the value for x, print1, if not, print2    
x = 5
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out!")

# if x to the power of 3 is greater than or equal to y AND if y to the power of 2 is less than 26, print 1, if not, print 2
x = 2
y = 5
if (x ** 3 >-y) and (y ** 2 < 26):
    print("Got Question 3!")
else:
    print("Oh good! You can count!")

# look for the name Dan in the three groups established, print the statement belonging to the group you find the name in
name = "Dan"
# create lists []
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Bob", "Joe", "Ed"]
group_three = ["Dan", "Anna", "Mary"]

if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in the second group")
elif name in group_three:
    print(name + " is in the third group")
else:
    print(name + " does not have a group")

# with height, age & adult permission variables set to find matching conditions and print out statement
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light costers")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to the lazy river!")

# more list [] examples
    
# create a variable, set it as a list and print list
myList = ["Mary", 50, "Edward", 43]
print(myList)

# add an element to the end of a list and print list
myList.append("Adam")
print(myList)

# find and print the index number of first object with a matching value
print(myList.index("Mary"))

# change a specific element in a list by index number, print list
# find element at index# 3 and change value to 55
myList[3] = 55
print(myList)

# find the length of a list
print(len(myList))

# remove an object from a list, print list
myList.remove("Mary")
print(myList)

# remove an object in a list by index number, print list
# remove object at original index 0
myList.pop(0)
# remove object at new index 1
myList.pop(1)
print(myList)

#create a tuple (immutable list of Python objects, cannot change)
myTuple = ("Python", 100, "VBA", False)
print(myTuple)

#############################################
# create rock paper scissors game

# import modules
import random

# print title
print("Let's Play Rock Paper Scissors!")

# specify player options as a list
options = ["r", "p", "s"]
# specify option names as a dictionary
option_names = {"r" : "Rock", "p" : "Paper", "s" : "Scissors"}

# create game with an option to replay using "while" statement
retry = "y"

while retry.lower() == "y":

    # computer selection
    computer_choice = random.choice(options)

    # user selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    # run game conditionals
    print(f" You chose {option_names[user_choice]}. The computer chose {option_names[computer_choice]}")

    # its a tie
    if user_choice == computer_choice:
        print("Its a tie! Try again!")
    # otherwise, user win conditions
    elif (user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (user_choice == "s" and computer_choice == "p"):
        print("Hooray! You won!")
    # otherwise, user lose conditions
    elif (user_choice == "r" and computer_choice == "p") or (user_choice == "p" and computer_choice == "s") or (user_choice == "s" and computer_choice == "r"):
        print("Sorry! You lose!")
    # if user choice is not recognized
    else:
        print("I don't understand that")
        print("Next time, choose from "r", "p" or "s".")
    
    # retry game?
    ret = input("Do you want to continue? (y)es, (n)o?")

###########################################


# additional "loop" statement examples
    
# loop through a range of numbers (0 through 4, remember computer counts from 0)
list(range(5))
list(range(2, 7))

for x in range(5):
    print(x)

# loop through a range of numbers 2 through 6, up to but not including 7
for x in range(2, 7):
    print(x)

# iterate through letters in a string
word = "Peace"
for letter in word:
    print(letter)

# iterate through a list []
zoo = ["monkey", "giraffe", "anteater"]
for animal in zoo:
    print(animal)

# continue loop while a condition is met
run = "y"
while run == "y":
    print("Yes!")
    run = input("To run again, enter "y": ")

############################
# number chain create game

# initial variable to track game play
user_play = "y"

# while conditions
while user_play == "y":

    # ask how many numbers to loop through and cast answer as an integer
    user_number = int(input("How many numbers? "))

    # loop through numbers
    for x in range(user_number):

        #print each number in the range
        print(x)

    # play again?
    user_play = input("Play again: (y)es or (n)o? ")

##################################