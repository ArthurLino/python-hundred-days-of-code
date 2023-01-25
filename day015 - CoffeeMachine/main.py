from formatters import format_resources, format_monetary_value

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

VALUE_PER_COIN = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources_sufficient(coffee):
    """
    Check if there are plenty resources for making the selected drink,
    if it does, returns True, otherwise returns False and a message saying which resource is not enough.
    """

    for needed_resource, needed_amount in MENU[coffee]["ingredients"].items():
        if not resources[needed_resource] - needed_amount > 0:
            print(f"Sorry, there is not enough {needed_resource}.")
            return False
    return True


def process_coins():
    """ Ask for inserting coins to the user and returns the total value of the payment."""
    total_value = 0

    print("Please insert coins.")

    for coin in VALUE_PER_COIN.keys():
        total_value += int(input(f"How many {coin}?: ")) * VALUE_PER_COIN[coin]
        print(total_value)

    return total_value


def check_transaction_successful(coffee, payment):
    """Returns True when the payment is accepted and False when there is not enough money."""
    coffee_cost_price = MENU[coffee]['cost']
    if coffee_cost_price <= payment:
        resources["money"] += payment
        if coffee_cost_price < payment:
            print(f"Here is {format_monetary_value(payment - coffee_cost_price)} dollars in change.")
        return True
    else:
        print(f"Sorry, that's not enough money (given: {resources['money']}). Money refunded")
        return False


def make_coffee(drink):
    """Returns the asked drink and deduct the ingredients from the machine resources."""
    for needed_resource, needed_amount in MENU[drink]["ingredients"].items():
        resources[needed_resource] -= needed_amount
    return drink


machine_is_on = True

while machine_is_on:
    print("Menu:",
          f"espresso: ({format_monetary_value(MENU['espresso']['cost'])})",
          f"latte: ({format_monetary_value(MENU['latte']['cost'])})",
          f"cappuccino: ({format_monetary_value(MENU['cappuccino']['cost'])})",
          sep="\n- ")
    user_input = input(f"What would you like? ").lower()

    if user_input == "off":
        machine_is_on = False

    if user_input == "report":
        print(format_resources(resources))

    if user_input in MENU.keys():
        if check_resources_sufficient(user_input) and check_transaction_successful(user_input, process_coins()):
            print(f"Here is your {make_coffee(user_input)}. Enjoy! ☕☕☕")

    print()
