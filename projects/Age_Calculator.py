# This line of code below imports the datetime module from Python's standard library.
"""import is a Python keyword used to bring in code from another module (a file or library) so you can use its features.

datetime is a built-in Python module that deals with dates and times.

The module datetime actually contains a class also called datetime (yes, same name!).

from datetime import datetime means:

"From the module named datetime, import the class called datetime". """

from datetime import datetime

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# int() converts the str() text passed into the input() into an integer since age is meant to be a number.
# The input() function always returns a string.
# Variables included in this code are: name, age, current_year and year_turn_100.

# Get the current year
current_year = datetime.now().year

# Calculate the year the user will turn 100
year_turn_100 = current_year + (100 - age)

# Output the result
print(f"Hello {name}, you will turn 100 years old in the year {year_turn_100}.")

# Output without using the f-string
# print("Hello " + name + ", you will turn 100 years old in the year " + str(year_turn_100) + ".")

"""from datetime import datetime

print("Current year:", datetime.now().year)"""
"The above code is used to check the time"

