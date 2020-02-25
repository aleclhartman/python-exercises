# Import and test 3 of the functions from your functions exercise file.
# Your functions exercise are not currently in a file with a name that can be easily imported.
# Copy your functions exercise file and name the copy functions_exercises.py.
# Import each function in a different way:
# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name
import functions_exercises as functions

functions.is_two(2)

functions.is_vowel("a")

from functions_exercises import handle_commas

handle_commas("3,500")

from functions_exercises import get_letter_grade as grade

grade(88)

# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
from itertools import permutations
from itertools import combinations

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
jackson_five = permutations("abc123", 2)

for x in jackson_five:
    print(x)

# How many different ways can you combine two of the letters from "abcd"?
letters = combinations("abcd", 2)

for c in letters:
    print(c)

# Save this file as profiles.json inside of your exercises directory.
# Use the load function from the json module to open this file, it will produce a list of dictionaries.
import json

json.load(open("profiles.json"))

# Using this data, write some code that calculates and outputs the following information:
profiles = json.load(open("profiles.json"))

print(profiles)

# Total number of users
total_users = len(profiles)
total_users

# Number of active users
active_users = len([profile for profile in profiles if profile["isActive"] == True])
active_users

# Number of inactive users
inactive_users = len([profile for profile in profiles if profile["isActive"] == False])
inactive_users

# Grand total of balances for all users
balances = [profile["balance"] for profile in profiles]
balances

no_dollar_sign = [balance[1:] for balance in balances]
no_dollar_sign

remove_commas = [balance.replace(",", "_") for balance in no_dollar_sign]
remove_commas

convert_float = [float(balance) for balance in remove_commas]
convert_float

grand_total_balance = sum(convert_float)
grand_total_balance

# Average balance per user
average_balance = grand_total_balance / total_users
round(average_balance, 2)

# User with the lowest balance
user_lowest_balance = [profile["name"] for profile in profiles if profile["balance"] == min(balances)]
user_lowest_balance

# User with the highest balance
user_lowest_balance = [profile["name"] for profile in profiles if profile["balance"] == max(balances)]
user_lowest_balance

# Most common favorite fruit
fruits = [profile["favoriteFruit"] for profile in profiles]
fruits

from collections import Counter

Counter(fruits)

most_common_fave_fruit = max(Counter(fruits))
most_common_fave_fruit

# Least most common favorite fruit
least_common_fave_fruit = min(Counter(fruits))
least_common_fave_fruit

# Total number of unread messages for all users
greetings = [profile["greeting"] for profile in profiles]
greetings

split_greetings = [greeting.split(" ") for greeting in greetings]
split_greetings

unread_messages = [split_greeting[:][5] for split_greeting in split_greetings]
unread_messages

integer_messages = [int(unread_message) for unread_message in unread_messages]
integer_messages

total_unread_messages = sum(integer_messages)
total_unread_messages