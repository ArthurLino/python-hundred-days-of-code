from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:

    print("-"*22)
    print("Menu\n", menu.get_items().replace("/", "\n "))
    print("-"*22)

    customer_request = input("Enter: ").lower()

    if customer_request == "report":
        coffee_machine.report()
        money_machine.report()
        continue

    if customer_request == "off":
        break

    drink = menu.find_drink(customer_request)

    if drink:
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
