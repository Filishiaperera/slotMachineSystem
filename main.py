def deposit():
    while True: # continusely ask the user to input a valied amount
        amount=input("How much would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break # breaking from the while loop and returning the amount
            else:
                print("The amount should be greater than 0.")
        else:
            print("Please enter a valied number!")
    return amount

deposit()