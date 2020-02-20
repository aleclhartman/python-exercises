# 1. Conditional Basics
#   a. prompt the user for a day of the week,
#   print out whether the day is Monday or not
day = input("What day is it? ")

if day == "Monday":
    print("Happy Monday")
else:
    print("Not Monday")

#   b. prompt the user for a day of the week,
#   print out whether the day is a weekday or a weekend
day = input("What day is it? ")

if day == "Saturday" or "Sunday":
    print("Weekend :)")
else:
    print("Weekday")

#   c. create variables and make up values for
#       - the number of hours worked in one week