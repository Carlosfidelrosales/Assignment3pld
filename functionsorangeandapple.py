#Having a short greetings to the user after the program started.
print('WELCOME TO CARLITO STORE! APPLE IS 20PHP EACH WHILE ORANGE IS 25PHP EACH. ')

#asking the user on how many apples he/she wants to buy
def acquire_apple():
    apple = int(input('Enter how many apples do you want to buy: '))
    return apple 

#asking the user on how many oranges he/she wants to buy
def acquire_orange():
    orange = int(input('Enter how many oranges do you want to buy: '))
    return orange

#total cost of apple
def cost_apple():
    price_apple = 20
    return price_apple

#total cost of orange
def cost_orange():
    price_orange = 25
    return price_orange

#grand total
def acquire_pricetotal():
    apple = (acquire_apple() * cost_apple())
    orange = (acquire_orange() * cost_orange())
    grand_total = (apple + orange)
    print_output(_grand_total=grand_total)

#prints the total amount in php
def print_output(_grand_total):
    print(f"The total amount is {_grand_total:,} Pesos.")

acquire_pricetotal()


