#Giving a short greetings after the initialization of the program
print("WELCOME TO CARLITO STORE! The fruit available for today is an apple. ")


#Added a docstring function to reduce the confusion of the programmer
def change_apple(_money, _apple):
    """
    The user's input and the store's return are represented by the _money and _apple variables. 
    Based on the calculations that were entered, the if statement reveals that the user can afford an apple. 
    On the other hand, contradicts the user's estimate.
    """
    if _money >=  _apple:
        change = _money % _apple
        apple_max = _money // _apple
        print(f"You can buy {apple_max:,.0f} apple(s) and your change is {change:,.2f} pesos.")
    else:
        _apple > _money
        insufficient_money = _apple - _money
        print(f"You don't have enough money. You must need atleast additional {insufficient_money:,.2f} pesos in order to buy an apple.")



#input a string/function to determine the user's money balance and the price of each apple
change_apple(_money = float(input("How much money do you have in your pocket right now?: ")), _apple = float(input("How much is the price for each apple?: ")))