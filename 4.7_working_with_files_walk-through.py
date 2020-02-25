# Example of unpacking tuple
a, b = (1, 2)

filename = "4.6_import_exercises.py"

# Read the contents of your last exercise file into a variable.

# Print out every line in the file
# Print out every line in the file, but add a line numbers

with open(filename, "r") as f:
    contents = f.readlines()
    for i, line in enumerate(contents, start=1):
        print(i, line)

# Write some python code to create a grocery list.

# Create a variable named grocery_list. It should be a list, and the elements in the list should be a least 3 things that you need to buy from the grocery store.
grocery_list = ["chia seed", "almonds", "kale", "yogurt", "guava"]

# Create a function named make_grocery_list. When run, this function should write the contents of the grocery_list variable to a file named my_grocery_list.txt.
def make_grocery_list(grocery_list):
    filename = "my_grocery_list.txt"
    with open(filename, "w") as f:
        for item in grocery_list:
            f.write(item + "\n")

make_grocery_list(grocery_list)

# Create a function named show_grocery_list. When run, it should read the items from the text file and show each item on the grocery list.

def show_grocery_list():
    with open("my_grocery_list.txt") as f:
        contents = f.readlines()
        for item in contents:
            print(item)

show_grocery_list()

# Create a function named buy_item. It should accept the name of an item on the grocery list, and remove that item from the list.

def buy_item(item, grocery_list):

    # remove mutates the lst object
    grocery_list.remove(item)

    make_grocery_list(grocery_list)

buy_item("kale", grocery_list)

show_grocery_list()