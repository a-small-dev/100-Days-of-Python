"""
The coffee machine project
"""
# Imports necessary modules
import data
import art

# Creating global variables
machine_on = True
money = 0
selection = ""

# Defining functions

# Checks if enough money was entered, then proceeds to finish the transaction and prints coffee art
def check_money(selection):
    global money

    print("Please enter your money")

    while True:
        try:
            quarters = int(input("Please enter your quarters: "))
            break
        except ValueError:
            print("Please input a whole number.")

    while True:
        try:
            dimes = int(input("Please enter your dimes: "))
            break
        except ValueError:
            print("Please input a whole number.")

    while True:
        try:
            nickles = int(input("Please enter your nickles: "))
            break
        except ValueError:
            print("Please input a whole number.")

    while True:
        try:
            pennies = int(input("Please enter your pennies: "))
            break
        except ValueError:
            print("Please input a whole number.")

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if selection == 1:
        if total >= data.MENU['espresso']['cost']:

            money += data.MENU['espresso']['cost']
            total -= data.MENU['espresso']['cost']
            print(f"Here is ${total:.2f} in change.")
            print("Here is your espresso. Enjoy!")
            print(art.coffee)

        else:

            total = 0
            print("Sorry, that's not enough money. Money refunded.")

    elif selection == 2:
        if total >= data.MENU['latte']['cost']:

            money += data.MENU['latte']['cost']
            total -= data.MENU['latte']['cost']
            print(f"Here is ${total:.2f} in change.")
            print("Here is your latte. Enjoy!")
            print(art.coffee)

    else:
        if total >= data.MENU['cappuccino']['cost']:

            money += data.MENU['cappuccino']['cost']
            total -= data.MENU['cappuccino']['cost']
            print(f"Here is ${total:.2f} in change.")
            print("Here is your cappuccino. Enjoy!")
            print(art.coffee)

# Checks for sufficient resources and updates new quantities
def check_resources(selection):

    if selection == 1:
        ingredients = data.MENU['espresso']['ingredients']

        if data.resources['water'] >= ingredients['water'] and data.resources['coffee'] >= ingredients['coffee']:
            data.resources['water'] -= ingredients['water']
            data.resources['coffee'] -= ingredients['coffee']
            return True

        if data.resources['water'] < ingredients['water']:
            print("Sorry, there is not enough water.")

        if data.resources['coffee'] < ingredients['coffee']:
            print("Sorry, there is not enough coffee.")

        if data.resources['water'] < ingredients['water'] or data.resources['coffee'] < ingredients['coffee']:
            return False


    elif selection == 2:
        ingredients = data.MENU['latte']['ingredients']

        if (data.resources['water'] >= ingredients['water'] and data.resources['coffee'] >= ingredients['coffee'] and
                data.resources['milk'] >= ingredients['milk']):

            data.resources['water'] -= ingredients['water']
            data.resources['coffee'] -= ingredients['coffee']
            data.resources['milk'] -= ingredients['milk']
            return True

        if data.resources['water'] < ingredients['water']:
            print("Sorry, there is not enough water.")

        if data.resources['coffee'] < ingredients['coffee']:
            print("Sorry, there is not enough coffee.")

        if data.resources['milk'] < ingredients['milk']:
            print("Sorry, there is not enough milk.")

        if (data.resources['water'] < ingredients['water'] or data.resources['coffee'] < ingredients['coffee'] or
                data.resources['milk'] < ingredients['milk']):
            return False


    else:
        ingredients = data.MENU['cappuccino']['ingredients']

        if (data.resources['water'] >= ingredients['water'] and data.resources['coffee'] >= ingredients['coffee'] and
                data.resources['milk'] >= ingredients['milk']):

            data.resources['water'] -= ingredients['water']
            data.resources['coffee'] -= ingredients['coffee']
            data.resources['milk'] -= ingredients['milk']
            return True

        if data.resources['water'] < ingredients['water']:
            print("Sorry, there is not enough water.")

        if data.resources['coffee'] < ingredients['coffee']:
            print("Sorry, there is not enough coffee.")

        if data.resources['milk'] < ingredients['milk']:
            print("Sorry, there is not enough milk.")

        if (data.resources['water'] < ingredients['water'] or data.resources['coffee'] < ingredients['coffee'] or
                data.resources['milk'] < ingredients['milk']):
            return False


# processes espresso selection
def process_espresso():
    make_drink = check_resources(1)
    if make_drink:
        check_money(1)

# processes latte selection
def process_latte():
    make_drink = check_resources(2)
    if make_drink:
        check_money(2)

# processes cappuccino selection
def process_cappuccino():
    make_drink = check_resources(3)
    if make_drink:
        check_money(3)

# generates report
def process_report():
 #   global money
    print("#" * 30)
    print("Coffee Machine Report:")
    print()
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Money: ${money:.2f}")
    print()
    print("END REPORT")
    print("#" * 30)

# Sends user selection to correct function
def process_selection(selection):
    global machine_on
    if selection == "espresso":
        process_espresso()
    elif selection == "latte":
        process_latte()
    elif selection == "cappuccino":
        process_cappuccino()
    else:
        process_report()


# Main program
print(art.logo)
while machine_on:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while selection not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print(f"{selection} is not a valid selection. Please try again.")
        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "off":
        machine_on = False
    else:
        process_selection(selection)
