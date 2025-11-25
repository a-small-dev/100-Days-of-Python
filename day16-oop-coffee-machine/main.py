from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
        selection = input(f"Hello what drink would you like? {menu.get_items()}: ")
        if selection == "off":
            is_on = False
        elif selection == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(selection)
            sufficient = coffee_maker.is_resource_sufficient(drink)
            if sufficient:
                payment_successful = money_machine.make_payment(drink.cost)
                if payment_successful:
                    coffee_maker.make_coffee(drink)
            