# Import and test 3 of the functions from your functions exercise file.
# Your functions exercise are not currently in a file with a name that can be easily imported.
# Copy your functions exercise file and name the copy functions_exercises.py.
# Import each function in a different way:
# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name
import functions_exercises as fe

# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# How many different ways can you combine two of the letters from "abcd"?
import itertools as it

len(list(it.product([1, 2, 3], "abc")))

len(list(it.combinations("abcd", 2)))

# Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

# Total number of users
# Number of active users
# Number of inactive users
# Grand total of balances for all users
# Average balance per user
# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users

import json

profiles = json.load(open("profiles.json"))

profiles[0].keys()

[profile for profile in profiles[:4]]

