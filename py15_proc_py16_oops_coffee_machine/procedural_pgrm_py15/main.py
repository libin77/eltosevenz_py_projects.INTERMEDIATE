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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def display_resource(machine_res, money):
    formatted_val = ""
    unit = "ml"
    for key in machine_res:
        if key == "coffee":
            unit = "g"
        formatted_val += f"{key.title()}: {resources[key]}{unit}\n"
    formatted_val += f"Money: ${money}"
    return formatted_val


def resource_available(coffee_name, avail_resources):
    """return True if resource is available for making coffee, otherwise False"""
    req_resource = MENU[coffee_name]["ingredients"]
    for key in req_resource:
        if req_resource[key] > avail_resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def coin_transaction_done(coffee_price):
    """return True if enough coin for processing, otherwise False"""
    print("please insert coins.")
    quarters = int(input("How many quarter? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    coin_available = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if coin_available < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = coin_available-coffee_price
    if change > 0:
        print(f"Here is the ${round(change,2)} dollars in change.")
    return True


def make_coffee(coffee_name, avail_resources):
    """return available resource after making coffee"""
    req_resource = MENU[coffee_name]["ingredients"]
    for key in req_resource:
        avail_resources[key] = avail_resources[key] - req_resource[key]
    print(f"Here is your {coffee_name}. Enjoy!")
    return avail_resources


def start_machine():
    machine_on = True
    profit = 0
    avail_resources = resources
    while machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            coffee_price = MENU[user_input]["cost"]
            if resource_available(user_input, resources) and coin_transaction_done(coffee_price):
                avail_resources = make_coffee(user_input, avail_resources)
                profit += coffee_price
        elif user_input == "off":
            machine_on = False
        else:
            print(display_resource(avail_resources, profit))


start_machine()
