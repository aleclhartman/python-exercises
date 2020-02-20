# 1. Conditional Basics
#   a. prompt the user for a day of the week,
#      print out whether the day is Monday or not
day = input("What day is it? ")

if day == "Monday":
    print("Happy Monday")
else:
    print("Not Monday")

#   b. prompt the user for a day of the week,
#      print out whether the day is a weekday or a weekend
day = input("What day is it? ")

if day == "Saturday" or "Sunday":
    print("Weekend :)")
else:
    print("Weekday")

#   c. create variables and make up values for
#       - the number of hours worked in one week
#       - the hourly rate
#       - how much the week's paycheck will be
#      write the python code that calculates the weekly paycheck.
#      You get paid time and a half if you work more than 40 hours
def weekly_paycheck(hours_worked):
    standard_workweek_hours = 40
    hourly_rate = 50
    if hours_worked > standard_workweek_hours:
        print((standard_workweek_hours * hourly_rate) 
              + ((hours_worked - standard_workweek_hours)
                 * (1.5 * hourly_rate)))
    else:
        print(standard_workweek_hours * hourly_rate)

# 2. Loop Basics
#   a. While
#       - Create an integer variable i with a value of 5.
#       - Create a while loop that runs so long as i
#         is less than or equal to 15
#       - Each loop iteration, output the current value of i,
#         then increment i by one.
i = 5

while i <= 15:
    print(i)
    i += 1

#       - Create a while loop that will count by 2's starting
#         with 0 and ending at 100. Follow each number with a
#         new line.
x = 0

while x <= 100:
    print(x)
    x += 2

#       - Alter your loop to count backwards by 5's from 100 to -10.
x = 100

while x <= 100 and x >= -10:
    print(x)
    x -= 5

#       - Create a while loop that starts at 2, and displays the
#         number squared on each line while the number is less
#         than 1,000,000.
x = 2

while x < 1000000:
    print(x)
    x *= x

#       - Subtract by 5s starting at 100 and stopping at 5
x = 100

while x > 0 and x <= 100:
    print(x)
    x -= 5

#   b. For Loops
#       i. Write some code that prompts the user for a number,
#          then shows a multiplication table up through 10 for
#          that number.
number = int(input("Give me a number, any number! "))

for i in range(1,11):
    print(number, "x", i, "=", number*i)

#       ii. Create a for loop that uses print to create the
#           output shown below.
n = int(input("Give me number of rows: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()

#   c. break and continue
#       i. Prompt the user for an odd number between 1 and 50.
#          Use a loop and a break statement to continue
#          prompting the user if they enter invalid input.
#          (Hint: use the isdigit method on strings to
#          determine this). Use a loop and the continue
#          statement to output all the odd numbers between
#          1 and 50, except for the number the user entered.
i = int(input("Give me an odd number between 1 and 50: "))

while i < 1 or i > 50 or i % 2 == 0:
    i = int(input("Give me a odd number between 1 and 50: "))

for n in range(51):
    if n % 2 == 0 or n == i:
        continue
    print("Here is an odd number: {}".format(n))


