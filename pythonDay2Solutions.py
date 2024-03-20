# SIMPLE LOOPS

# a "for" loop moves through a given range of numbers (if only one number is provided it will loop from 0 to that number)
for x in range(10):
    print(x)

# if two numbers are provided, it will loop from the first number up to but not including second number.
for x in range(20, 30):
     print(x)

# if a list is provided, loop will go through each statement on the list
words = ["Icecream", "And", "Cake", "n", "Cake"]
for word in words:
    print(word)

# a "while" loop will continue to loop through code until some condition is met or not met
x = "yes"
while x.lower() == "yes":
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Wuild you lik to go on the ride again? ")

########################
# CANDY SHOPPING

# create list of available candy to purchase
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starburst", "Peanut M&Ms"]

# create a variable that limits the number of items to 5
allowance = 5

# create a shopping cart as an empty list
shoppingCart = []

# print available candies using index as selection #
for candy in candyList:
    print(f"[{str(candyList.index(candy))}] {candy}")

# Another option to run the for loop involves Python's enumerate method
# This method obtains both the index and the value of an item during a for loop
# for index, candy in candy_list:
#     print(index, candy)

# create loop for candy selection
print("What candy would you like to select? ")
for x in range(allowance):
    selected = input("Input the number of the candy you want: ")

    # add selection to the shopping cart as data type "integer"
    shoppingCart.append(candy_list[int(selected)])

# loop through shopping cart to see what was purchased
print("I purchased: ")
for candy in shoppingCart:
    print(candy)

######################################

# ADVANCED LOOPS
    
# PIE SHOPPING
    
# initial variable to track shopping status
shopping = "y"

# empty list to hold purchases
purchasedPies = []

# create list of available pies
pieList = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Tamale", "Steak"]

# create and display initial msg
print("Welcome to the house of pies! Here are our pie selections: ")

# create "while" statement for still shopping mode
while shopping == "y":

    # pie selection display
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")
    
    pieChoice = input("What pie would you like? ")

    # add selection to purchasedPie list
    purchasedPies.append(pieChoice)

    print("---------------------------------------------------------------------")

    # confirm pie purchase
    print(f"Great! We'll have that {pieList[int(pieChoice) -1]} right out for you. ")

    # provide shopping exit option
    stillShopping = input("Would you like to make another purchase: (y)es or (n)o?")

# when done shopping, print purchased list with number value as a string
print("---------------------------------------------------------------------")
print(f"You purchased a total of {str(len(purchasedPies))} .")

###########################################

# set path with data file to be read
file = "./Resources/input.txt"

# open the file in "read" mode ('r') and store the contents in the variable "text" with open(file, 'r') as text:
with open(file, "r") as text:

    # This stores a reference to a file stream
    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)

###########################################
    
# PYTHON MODULES
    
# "random" & "string"
import random
import string

# use the string module's custom method: ".ascii_letters"
print(string.ascii_letters)

# use the random module's custom randiint
# for the range 0-9, print a random object as an integer
for x in range(10):
    print(random.randint(1, 10))


########################################

# reading CSV files

# import dependencies & modules
import os
import csv

# set path for file to read
csvpath = os.path.join(".", "Resources", "contacts.csv")
print(csvpath)

# read file using CSV module
with open(csvpath) as csvfile:

    # specify delimiter & variable to hold contents of file
    csvreader = csv.reader(csvfile, delimiter=",")

    # look at contents of file
    print(csvreader)

    # read headder row (skip if no header)
    csvHeader = next(csvreader)
    print(f"{csvHeader}")

    # read each row after the header
    for row in csvreader:
        print(row)


#################################
# searching through a database

# import dependencies & modules
import os
import csv

# prompt user for search value
comic = input("What title are you looking for? ")

# set path for data file
csvpath - os.path.join(".", "Resources", "comic_books.csv")

# set variable to check if value found
found = False

# open file w/utf-8 encoding
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # loop through looking for value
    for row in csvreader:
        if row[0] == comic:
            print(row[0] + " was published by " + row[8]+ " in " + row[9])

            # set variable to confirm value found
            found = True

        # set user alert if value not found
        if found is False:
            print("Sorry, we don't have that title in stock.")

###########################################
# creating analysis output file

# import dependencies & modules
import os
import csv

# set path & file name of where to export file
outputPath = os.path.join(".", "output", "new.csv")

# open file in "write" mode (allows editing of file vs "read" mode)
with open(outputPath, "w") as csvfile:

    # initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=",")

    # add column headers
    csvwriter.writerow(["First Name", "Last Name", "SSN"])

    # write first data row
    csvwriter.writerow(["Mary", "Mackin", "123-45-6789"])

###################################
# combining lists and output new file as csv
    
# import dependencies & modules
import os
import csv

# create lists to merge
indexes = [1, 2, 3, 4]
employees = ["Mary", "Edward", "Adam", "Ben"]
department = ["Boss", "ViceBoss", "Music", "Gaming"]

# merge lists usin "zip" and print to confirm merge
orgChart = list(zip(indexes, employees, department))
print(orgChart)

# print contents of each row of a specific column
for employees in orgChart:
    print(employees)

# set output path/file name
outputFile = os.path.join("output.csv")

# open the output file, create a new header row, write zipped object to te csv file
with open(outputFile, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Index", "Employee", "Department"])

    writer.writerows(orgChart)

######################################
# intro to functions in python
    
# define a function and give it a command to print a value
def printHello()
    print(f"Hello!")

# call the function within the application to check code
printHello()

# define function that takes in and uses defined parameters
def printName(name):
    print(f"Hello {name} !")

# call a function with a specific parameter
printName("Bob Smith")

# the main use of functions is to be able to run the same code for different values/lists, etc.
# create lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

def listInfo(simpleList):
    print(f"The values within the list are: ")
    for value in simpleList:
        print(value)
    print(f"The length of this list is: {str(len(simpleList))}")

listInfo(list1)
listInfo(list2)

def sumValues(simpleList):
    total = 0
    for value in simpleList:
        total += value
    print("The lenght of this list is: " + str(len(simpleList)))
    print("The total sum of this list is: " + str(total))
    return total
totalList1 = sumValues(list1)
sumValues(list2)

print(totalList1)








