from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine_start():
    my_menu = Menu()
    my_coffee_maker = CoffeeMaker()
    my_money = MoneyMachine()

    is_off = False

    while not is_off:
        user_input = input(f"what you like to have {my_menu.get_items()}? ").lower()
        if user_input == "off":
            is_off = True
        elif user_input == "print":
            my_coffee_maker.report()
            my_money.report()
        else:
            my_coffee = my_menu.find_drink(user_input)
            if my_coffee_maker.is_resource_sufficient(my_coffee) and my_money.make_payment(my_coffee.cost):
                my_coffee_maker.make_coffee(my_coffee)


coffee_machine_start()