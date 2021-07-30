# Actions
BUY = 'buy'
FILL = 'fill'
TAKE = 'take'
EXIT = 'exit'
REMAINING = 'remaining'
BACK = 'back'

# Coffee types
ESPRESSO = '1'
LATTE = '2'
CAPPUCCINO = '3'

# Stored ingredients
STORAGE = {'MONEY': 550,
           'WATER': 400,
           'MILK': 540,
           'BEANS': 120,
           'CUPS': 9
           }
espresso = {'price': 4,
            'water': 250,
            'milk': 0,
            'beans': 16,
            'cups': 1
           }
latte = {'price': 7,
         'water': 350,
         'milk': 75,
         'beans': 20,
         'cups': 1
        }
cappuccino = {'price': 6,
              'water': 200,
              'milk': 100,
              'beans': 12,
              'cups': 1
             }


def check_ingredients(coffee_type):
    global STORAGE, espresso, latte, cappuccino
    enough_water = STORAGE['WATER'] - coffee_type['water']
    enough_milk = STORAGE['MILK'] - coffee_type['milk']
    enough_beans = STORAGE['BEANS'] - coffee_type['beans']
    enough_cups = STORAGE['CUPS'] - coffee_type['cups']
    if enough_water >= 0  and enough_milk >= 0 and enough_beans >= 0 and enough_cups >= 0:
        print("I have enough resources, making you a coffee!")
        return True
    else:
        print("Sorry, not enough ingredients!")
        return False


def make_espresso():
    # espresso cup = 1, water = 250, beans = 16, price = 4
    global STORAGE
    STORAGE['CUPS'] -= 1
    STORAGE['WATER'] -= 250
    STORAGE['BEANS'] -= 16
    STORAGE['MONEY'] += 4


def make_latte():
    # latte cup = 1, water = 350, milk = 75, beans = 20, price = 7
    global STORAGE
    STORAGE['CUPS'] -= 1
    STORAGE['WATER'] -= 350
    STORAGE['MILK'] -= 75
    STORAGE['BEANS'] -= 20
    STORAGE['MONEY'] += 7


def make_cappuccino():
    # cappuccino cup = 1, water = 200, milk = 100, beans = 12, price = 6
    global STORAGE
    STORAGE['CUPS'] -= 1
    STORAGE['WATER'] -= 200
    STORAGE['MILK'] -= 100
    STORAGE['BEANS'] -= 12
    STORAGE['MONEY'] += 6


def report():
    print(f"""
The coffee machine has:
{STORAGE['WATER']} ml of water
{STORAGE['MILK']} ml of milk
{STORAGE['BEANS']} g of coffee beans
{STORAGE['CUPS']} of disposable cups
{STORAGE['MONEY']} of money
""")


def buy():
    while True:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        option = input()
        if option == ESPRESSO:
            if check_ingredients(espresso):
                make_espresso()
            break
        elif option == LATTE:
            if check_ingredients(latte):
                make_latte()
            break
        elif option == CAPPUCCINO:
            if check_ingredients(cappuccino):
                make_cappuccino()
            break
        elif option == BACK:
            break
        else:
            print("Wrong option")
            break


def fill():
    global STORAGE
    print("Write how many ml of water do you want to add:")
    STORAGE['WATER'] += int(input())
    print("Write how many ml of milk do you want to add:")
    STORAGE['MILK'] += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    STORAGE['BEANS'] += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    STORAGE['CUPS'] += int(input())


def take():
    global STORAGE
    print(f"I gave you ${STORAGE['MONEY']}")
    STORAGE['MONEY'] = 0


def coffee_machine():
    print("Write action (buy, fill, take, remaining, exit):")
    option = input()
    if option == BUY:
        buy()
    elif option == FILL:
        fill()
    elif option == TAKE:
        take()
    elif option == REMAINING:
        report()
    elif option == EXIT:
        exit()
    else:
        print("Wrong input")


while True:
    coffee_machine()
