#!/usr/bin/env python
# coding: utf-8

# In[122]:


# Read the contents of your last exercise file into a variable.
with open("4.6_import_exercises.py") as f:
    contents = f.read()


# In[123]:


# Print out every line in the file
lines = contents.split("\n")
lines


# In[124]:


# Print out every line in the file, but add a line numbers
for number, line in enumerate(lines):
    print(number + 1, line)


# In[108]:


# Write some python code to create a grocery list.

# Create a variable named grocery_list.
# It should be a list and
# the elements in the list should be a least 3 things that you need to buy from the grocery store.
grocery_list = ["beer", "spinach", "corn"]
grocery_list


# In[132]:


# Create a function named make_grocery_list.
# When run, this function should write the contents of the grocery_list variable to a file named my_grocery_list.txt.
def make_grocery_list():
    grocery_list
    with open("my_grocery_list.txt", "w") as f:
        for item in grocery_list:
            f.writelines(item + "\n")

make_grocery_list()


# In[133]:


# Create a function named show_grocery_list.
# When run, it should read the items from the text file and show each item on the grocery list.
def show_grocery_list():
    with open("my_grocery_list.txt") as f:
        contents = f.read()
        print(contents)

show_grocery_list()


# In[134]:


# Create a function named buy_item.
# It should accept the name of an item on the grocery list, and remove that item from the list.
def buy_item(item_bought):
    with open("my_grocery_list.txt") as f:
        items = f.readlines()
    with open("my_grocery_list.txt", "w") as f:
        for item in items:
            if item.strip("\n") != item_bought:
                f.write(item)
    with open("my_grocery_list.txt") as f:
        print(f.read())
        
buy_item("beer")


# In[ ]:




