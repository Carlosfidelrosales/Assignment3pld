#Giving a short greetings after the initialization of the program
print("WELCOME TO CARLITO STORE! The fruit available for today is an apple. ")


#Added a docstring function to reduce the confusion of the programmer
def apple_change(_money, _apple):
    """
    The user's input and the store's return are represented by the _money and _apple variables. 
    Based on the calculations that were entered, the if statement reveals that the user can afford an apple. 
    On the other hand, contradicts the user's estimate.
    """
    if _money <= _apple:
        change = float(_money) % float(_apple)
        apple_max = float(_money) // float(_apple)
        print(f"You can buy {apple_max:,.0f} apple(s) and your change is {change:,.2f} pesos.")
    
    elif _money >= _apple:
        change1 = float(_money) % float(_apple)
        apple_max1 = float(_money) // float(_apple)
        print(f"You can buy {apple_max1:,.0f} apple(s) and your change is {change1:,.2f} pesos.")
        
    elif _apple > _money:
        money_needed = float(_apple) - float(_money)
        print(f"I'm sorry, you don't have enough money. You must have additional {money_needed:,.2f} peso(s) in order to buy an apple.")


#input a string to determine the user's money and the price of each apple
apple_change(_money = input("How much cash do you have in your pocket right now?: "), _apple = input("How much is the price of each apple?: "))
