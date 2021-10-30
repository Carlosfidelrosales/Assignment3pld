def money_have():
    money = float(input('How much money do you have in your pocket?: '))
    return money

def apple_cost():
    apple = int(input('What is the amount for each apple: '))
    return apple

def afford_apple():
    max_apples = int(money_have() // apple_cost())
    return max_apples
    
def change():
    change = float(money_have() % apple_cost())
    return change

print(f"You can buy {afford_apple()} apples and your change is{change(): .2f} pesos")
