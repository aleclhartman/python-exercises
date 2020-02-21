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

#   d. The input function can be used to prompt for input and
#      use that input in your python code. Prompt the user to
#      enter a positive number and write a loop that counts from
#      0 to that number. (Hints: first make sure that the value
#      the user entered is a valid number, also note that the
#      input function returns a string, so you'll need to convert
#      this to a numeric type.)
i = int(input("Give me a positive number: "))

while i < 1 or i == float:
    i = int(input("Give me a positive number: "))

for n in range(0, i+1):
    print(n)

#   e. Write a program that prompts the user for a positive
#      integer. Next write a loop that prints out the numbers
#      from the number the user entered down to 1.
i = int(input("Give me a posistive integer: "))

while i < 1:
    i = int(input("Give me a posistive integer: "))

for n in range(i, 0-1, -1):
    print(n)

# 3. Fizzbuzz
#   One of the most common interview questions for entry-level
#   programmers is the FizzBuzz test. Developed by Imran Ghory,
#   the test is designed to test basic looping and conditional
#   logic skills.
#       - Write a program that prints the numbers from 1 to 100.
for n in range(1, 101):
    print(n)

#       - For multiples of three print "Fizz" instead of the number
for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz")
        continue
    print(n)

#       - For the multiples of five print "Buzz".
for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz")
        continue
    print(n)
    print(n)

#       - For numbers which are multiples of both three
#         and five print "FizzBuzz".
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
        continue
    if n % 3 == 0:
        print("Fizz")
        continue
    if n % 5 == 0:
        print("Buzz")
        continue
    print(n)

# 4. Display a table of powers.
#   - Prompt the user to enter an integer.
#   - Display a table of squares and cubes from 1
#     to the value entered.
#   - Ask if the user wants to continue.
#   - Assume that the user will enter valid data.
#   - Only continue if the user agrees to.
i = int(input("Give me an integer: "))

while i < 1:
    i = int(input("Give me an integer: "))   

number = [n for n in range(1, i + 1)]
squared = [n*n for n in range(1, i + 1)]
cubed = [n*n*n for n in range(1, i + 1)]
columns = ["number", "squared", "cubed"]
data = [columns] + list(zip(number, squared, cubed))

proceed = input("Do you wish to continue? ")

if proceed.capitalize() == 'Yes':
    for a, h in enumerate(data):
        line = '|'.join(str(x).ljust(12) for x in h)
        print(line)
        if a == 0:
            print('-' * len(line))
else:
    print("Halt")

# 5. Convert given number grades into letter grades.
#   - Prompt the user for a numerical grade from 0 to 100.
#   - Display the corresponding letter grade.
#   - Prompt the user to continue.
#   - Assume that the user will enter valid integers for the grades.
#   - The application should only continue if the user agrees to.
grade = int(input("Enter your grade here: "))

while grade < 0 or grade > 100:
    grade = int(input("Enter your grade here: "))
    
    
proceed = input("Do you wish to continue? ")

if proceed.capitalize() == 'Yes':
    if grade in range(101, 88-1, -1):
        print("A")
    elif grade in range(87, 80-1, -1):
        print("B")
    elif grade in range(79, 67-1, -1):
        print("C")
    elif grade in range(66, 60-1, -1):
        print("D")
    else:
        print("F")
else:
    print("Halt")

# 6. Create a list of dictionaries where each dictionary
#    represents a book that you have read. Each dictionary
#    in the list should have the keys title, author, and genre.
#    Loop through the list and print out information about each
#    book.
#   a. Prompt the user to enter a genre, then loop through your
#      books list and print out the titles of all the books in
#      that genre.
books = [
    {
        "title": "12 Rules for Life",
        "author": "Jordan Peterson",
        "genre": "Self-help"
    },
    {
        "title": "Extreme Ownership",
        "author": "Jocko Willink",
        "genre": "Leadership"
    },
    {
        "title": "The Prophet",
        "author": "Kahlil Gibran",
        "genre": "Poetry"
    },
    {
        "title": "Lord of the Rings",
        "author": "J. R. R. Tolkien",
        "genre": "Fantasy"
    },
    {
        "title": "Letter to a Christian Nation",
        "author": "Sam Harris",
        "genre": "Non-fiction"
    },
    {
        "title": "Peace is Every Step",
        "author": "Thich Nhat Hanh",
        "genre": "Self-help"
    }
]

for book in books:
    print(book["title"])

genre = input("Enter a genre: ")

while genre not in ["Self-help", "Leadership", "Poetry", "Fantasy", "Non-fiction"]:
    genre = input("Enter a genre: ")

[book["title"] for book in books if book["genre"] == genre]