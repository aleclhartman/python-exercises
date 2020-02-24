# Define a function named is_two. It should accept one input and return True
# if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    return x == 2 or x == "2"


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    return len(letter) == 1 and letter.lower() in 'aeiou'


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise.
# Use your is_vowel function to accomplish this.
def is_consonant(letter):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return len(letter) == 1 and letter.isalpha() and not is_vowel(letter)
    

# Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_consonant_word(word):
    if is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        return word
    

# Define a function named calculate_tip.
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(percent, bill_total):
    tip_amount = percent * bill_total
    return tip_amount


# Define a function named apply_discount.
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(price, discount):
    discounted_price = price - price * discount
    return discounted_price


# Define a function named handle_commas.
# It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(number_as_string):
    return int(number_as_string.replace(",", "_"))


# Define a function named get_letter_grade.
# It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number):
    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70:
        return "C"
    else:
        return "F"


# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    string = string.lower()
    vowels = ["a", "e", "i", "o", "u"]
    for letters in string:
        if letters in vowels:
            string = string.replace(letters, "")
    return string


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
def normalize_name(string):
    for character in string:
        if character.isidentifier() == False:
            string = string.replace(character, " ")
    string = string.strip()
    for character in string:
        if character == " ":
            string = string.replace(character, "_")
    string = string.lower()
    return string


# Write a function named cumsum that accepts a list of
# numbers and returns a list that is the cumulative sum of the numbers in the list.
def cumsum(numbers):
    cumulative_list = []
    cumulative_sum = 0
    for n in numbers:
        cumulative_sum += n
        cumulative_list.append(cumulative_sum)
    return cumulative_list


# Create a function named twelveto24. It should accept a string in the format 10:45am or
# 4:30pm and return a string that is the representation of the time in a 24-hour format.
# Bonus write a function that does the opposite.
def hours(string):
    string = string.split(":")
    hour = int(string[0])
    if "p" in string[1] and hour != 12:
        return str(hour + 12)
    if hour == 12 and "a" in string[1]:
        return "00"
    return str(hour)

def minutes(string):
    string = string.split(":")
    minute_m = string[1]
    minute = minute_m[:2]
    return minute

def twelveto24(string):
    return hours(string) + ":" + minutes(string)
