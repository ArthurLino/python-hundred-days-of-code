def format_monetary_value(value):
    return f"${value:.2f}"


def format_resources(resources):
    """Return the coffee machine resources in a printable format."""

    return f"""Water: {resources['water']}ml
           \nMilk: {resources['milk']}ml
           \nCoffee: {resources['coffee']}g
           \nMoney: {resources['money']}"""
