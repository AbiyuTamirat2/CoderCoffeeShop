# Getting user information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Validating and getting a 10-digit phone number from the user
while True:
    phone_number = input("Enter your 10-digit phone number: ")
    if phone_number.isdigit() and len(phone_number) == 10:
        break
    else:
        print("Please enter a valid 10-digit phone number with only digits.")

# Setting up the Coffee Shop
coffee_shop_name = "Coder Coffee Shop"

# Displaying a Welcome Message
print(f"Hello, {first_name}! Welcome to {coffee_shop_name}.")
print("=" * 50)

# Defining the Coffee Menu
menu = {
    1: {"name": "Black Coffee", "price": 3.25},
    2: {"name": "Latte", "price": 4.50},
    3: {"name": "Cappuccino", "price": 4.50},
    4: {"name": "Espresso", "price": 3.50},
    5: {"name": "Americano", "price": 3.50}
}

# Initializing Variables
total_cost, cart = 0, []

# Taking Coffee Orders
while True:
    # Displaying the Menu
    print("\nMenu:")
    for key, item in menu.items():
        print(f"{key}. {item['name']}: ${item['price']:.2f}")

    # Getting the User's Choice
    option = input("Choose the coffee number you would like to order? (Enter '0' to proceed to checkout): ")

    # Exiting the Loop if '0' is Entered
    if option == '0':
        break

    option = int(option)

    # Adding the Selected Coffee to the Cart
    if option in menu:
        quantity = int(input("Enter the quantity: "))
        total = quantity * menu[option]["price"]
        total_cost += total
        cart.append((f"{quantity} x {menu[option]['name']} - ${total:.2f}", total))
    else:
        print("Invalid option. Please choose a valid coffee number.")

# Calculating Tax (10%)
tax = total_cost * 0.10
total_cost_with_tax = total_cost + tax

# Displaying the Order Summary with Tax
print("*" * 50)
print("Your Order Summary:\n")
for item, price in cart:
    print(f"{item}")
print("*" * 50)
print(f"Subtotal: ${total_cost:.2f}")
print(f"Tax (10%): ${tax:.2f}")
print(f"Total Cost (Including Tax): ${total_cost_with_tax:.2f}")
print("*" * 50)

# Thank You Message
print(f"Thank you for ordering! \n"
      f"You'll get a text when your coffee is ready.")
print("Have a wonderful day!")
print("*" * 50)
