# Define a function named is_two. It should accept one input and return True
# if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    if x == 2 or x == "2":
        return True
    else:
        return False

is_two(2)

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(string):
    if string.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False

is_vowel("a")

# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise.
# Use your is_vowel function to accomplish this.
def is_consonant(letter):
    if is_vowel(letter.lower()) != True:
        return True
    else:
        return False
    
is_consonant("v")

# Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_consonant_word(word):
    if is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        return word
    
capitalize_consonant_word("alec")

# Define a function named calculate_tip.
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(percent, bill_total):
    tip_amount = percent * bill_total
    return tip_amount

calculate_tip(.2, 100)

# Define a function named apply_discount.
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(price, discount):
    discounted_price = price - price * discount
    return discounted_price

apply_discount(10, .4)

# Define a function named handle_commas.
# It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(number_as_string):
    return int(number_as_string.replace(",", "_"))

handle_commas("9,000")

# Define a function named get_letter_grade.
# It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number):
    if number in range(90, 101):
        return print("A")
    elif number in range(80, 90):
        return print("B")
    elif number in range(70, 80):
        return print("C")
    elif number in range(60, 70):
        return print("D")
    else:
        return print("F")

get_letter_grade(69)

# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    string = string.lower()
    vowels = ["a", "e", "i", "o", "u"]
    for letters in string.lower():
        if letters in vowels:
            string = string.replace(letters, "")
    print(string)

remove_vowels("alec")

# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
def normalize_name(string):
    string = string.lower()
    string = string.strip()
    string = string.replace(" ", "_")
    for character in string:
        if character.isidentifier() == False:
            string = string.replace(character, "")
    return string

normalize_name("$Al^ec Lou%is Hart#man!")