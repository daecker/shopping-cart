# shopping_cart.py

import datetime
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()


SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")   

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


#Step 1: Define Variables

grocery_name = "ECKER GROCERY"
grocery_website = "WWW.ECKERGROCERY.COM"
checkout_message = "THANK YOU FOR VISITING! EAT WELL AND COME BACK SOON"
checkout_start = datetime.datetime.now()
formated_checkout_time = checkout_start.strftime("%Y-%m-%d %I:%M %p")
subtotal_price = 0
tax_rate = .0875
selected_ids = []
all_id_list = [id["id"] for id in products]
products_count = len(products)

#Step 2: Define Fuctions

def to_usd(my_price):
    return "${0:.2f}".format(my_price)

#Step 3: User Input Selections + validation + print
while True:
    selected_id = input("Please input a product identifier or 'DONE': ") #output is a string

    if selected_id == "DONE":
        break
    #elif int(selected_id) > products_count: #line assumes all product IDs are unique and chronological.
    #    print("Error: Please enter a valid ID")
    elif int(selected_id) not in all_id_list: #validation of selected_id
        print("Error: Please enter a valid ID")
    else:
        selected_ids.append(selected_id)


print("---------------------------------")
print(grocery_name)
print(grocery_website)
print("---------------------------------")
print("CHECKOUT TIME: " + formated_checkout_time)
print("---------------------------------")
print("SELECTED PRODUCTS:")

#Step 4: Operations on user inputs
for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    print(" ... " + str(matching_product["name"]) + " (" + to_usd(matching_product["price"]) + ")")


tax_amount = subtotal_price * tax_rate
total_price = subtotal_price + tax_amount

#Step 5: Print final results
print("---------------------------------")
print("SUBTOTAL PRICE: " + to_usd(subtotal_price))
print("TAX (8.75%): " + to_usd(tax_amount))
print("TOTAL PRICE: " + to_usd(total_price))
print("---------------------------------")
print(checkout_message)
print("---------------------------------")

print_receipt = input("Would you like an email receipt? y/n: ")
if print_receipt == "y":
    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))
    subject = "Your Receipt"

    html_content = "Hello World"
    print("HTML", html_content)

    message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=subject, html_content=html_content)
    try:
        response = client.send(message)

        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)
    
    except Exception as e:
        print("OOPS", e.message)
else:
    print("THANK YOU")
    exit
