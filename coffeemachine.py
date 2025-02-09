print("""   (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/""")
menuData={
    "espresso":{
        "ingredients": {
            "water":50,
            "coffee":18,
        },
        "cost":1.5,

    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":2.5
    },
    "cappuccino":{"ingredients":{
        "water":250,
        "milk":100,
        "coffee":24,
    },
    "cost":3.0,

    }
    }
profit=0
resources={
        "water":600,
        "milk":350,
        "coffee":100,
    }

def is_resource_suffucuent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    print("please insert Money.")
    total = int(input("How many Dollars: "))*1
    total +=int(input("How many Quarters: "))*0.25
    total +=int(input("How many Dimes: "))*0.25
    print(f"You gave is ${total} ")
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received- drink_cost,2)
        print(f"your change is ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False




def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

Coffee_is_on=True
while Coffee_is_on:
    choice = input("Welcome to coffee Express.(espresso/latte/cappuccino): ")
    if choice =="off":
        print("Good bye!")
        Coffee_is_on= False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    elif choice not in ["espresso","latte","cappuccino"]:
        print("error Please try again")
    else:
        drink = menuData[choice]
        if is_resource_suffucuent(drink["ingredients"]):
            payment = process_coin()
            is_transaction_successful(payment,drink["cost"])
            make_coffee(choice,drink["ingredients"])

"""
Available selections: Espresso, Latte, or Cappuccino.
Enter "report" to view the coffee machine's current resource inventory.
Enter "off" to shut down the coffee machine.
"""