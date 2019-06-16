# shopping-cart

# Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "shopping-cart". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like https://github.com/YOUR_USERNAME/shopping-cart.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/shopping-cart
```

Use your text editor or the command-line to create a file in that repo called "shopping_cart.py", and then place the following contents inside:

```sh
# shopping_cart.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output
```
Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.

# Environment Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

From within the virtual environment, install the pytest package:

```sh
# NOTE: we won't need pytest until/unless addressing the optional "Automated Testing" challenge,
# so you can feel free to skip this now and return later...

pip install pytest
```

From within the virtual enviornment, install the sendgrid package
'''sh
pip install sendgrid==6.0.5
'''


# Usage
From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python shopping_cart.py
```

If you see the provided "products" data structure, you're ready to move on to project development. This would be a great time to make any desired modifications to your project's "README.md" file (like adding instructions for how to setup and run the app like you've just done), and then make your first commit, with a message like "Setup the repo".

# Guided Steps
Step 1: Import datetime package using import datetime   
Step 2: Write code to apture Product IDs
Step 3: Use a loop to capture multiple user inputs
Step 4: Restructure code to match expected output (hint: first ask for IDs, then print output)
Step 5: Print results to match expected output format

If you need help: follow the screencast here:
https://www.youtube.com/watch?v=3BaGb-1cIr0&feature=youtu.be

# End Result Sample

```sh
Please input a product identifier: 1
Please input a product identifier: 8
Please input a product identifier: 6
Please input a product identifier: 8
Please input a product identifier: 8
Please input a product identifier: 16
Please input a product identifier: 12
Please input a product identifier: DONE
---------------------------------
GREEN FOODS GROCERY
WWW.GREEN-FOODS-GROCERY.COM
---------------------------------
CHECKOUT AT: 2019-06-06 11:31 AM
---------------------------------
SELECTED PRODUCTS:
 ... Chocolate Sandwich Cookies ($3.50)
 ... Cut Russet Potatoes Steam N' Mash ($4.25)
 ... Dry Nose Oil ($21.99)
 ... Cut Russet Potatoes Steam N' Mash ($4.25)
 ... Cut Russet Potatoes Steam N' Mash ($4.25)
 ... Mint Chocolate Flavored Syrup ($4.50)
 ... Chocolate Fudge Layer Cake ($18.50)
---------------------------------
SUBTOTAL: $61.24
TAX: $5.35
TOTAL: $66.59
---------------------------------
THANKS, SEE YOU AGAIN SOON!
---------------------------------
```

