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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

treasury = 0


def report():
    print(f"Water = {resources["water"]}\nMilk = {resources["milk"]}\nCoffee = {resources["coffee"]}")


def payment(drink):
    global treasury
    print("Please insert coins.")
    quarters = 0.25*int(input("How many quarters: "))
    dimes = 0.1*int(input("How many dimes: "))
    nickels = 0.05*int(input("How many nickels: "))
    pennies = 0.01*int(input("How many pennies: "))
    paid = quarters + dimes + nickels + pennies
    if paid < MENU[drink]["cost"]:
        print("Insufficient coins inserted.")
        print(f"Here are you ${paid}. Please try again.")
        return False
    elif paid == MENU[drink]["cost"]:
        treasury += MENU[drink]["cost"]
        print("Payment Successful")
        return True
    else:
        change = paid - MENU[drink]["cost"]
        treasury += MENU[drink]["cost"]
        print(f"Here is your ${round(change, 2)} change.")
        print("Payment Successful")
        return True


def check_espresso():
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
        if payment("espresso"):
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print("Enjoy you espresso.")
    else:
        print("Insufficient ingredients.")


def check_cappuccino():
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
        if payment("cappuccino"):
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print("Enjoy you cappuccino.")
    else:
        print("Insufficient ingredients.")


def check_latte():
    if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
        if payment("latte"):
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print("Enjoy you latte.")
    else:
        print("Insufficient ingredients.")


while True:
    person = int(input("Select 1 to order coffee and 2 for machine maintenance: "))
    if person == 1:
        choice = input("What would you like (espresso / latte / cappuccino): ").lower()
        if choice == "espresso":
            check_espresso()
        elif choice == "latte":
            check_latte()
        elif choice == "cappuccino":
            check_cappuccino()
        else:
            print("Invalid selection.")
    elif person == 2:
        choice = input("What would you like (report / treasury): ").lower()
        if choice == "report":
            report()
        elif choice == "treasury":
            print(f"The total money collected is ${treasury}")
        else:
            print("Invalid selection.")
    else:
        print("Invalid selection.")
