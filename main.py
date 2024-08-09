# to make the program dynamic adding global constant
MAX_LINES=3# capitales coz this is a constant 
MAX_BET=100
MIN_BET=1

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


#collect the bet from the user/ how many lines they wanna bet on/then multiply their amount by number of lines
def get_number_of_lines():# pick a number between 1 and 3
    while True: # continusely ask the user to input a valied amount
        lines=input("Enter the number of lines to bet on(1-"+str(MAX_LINES)+")? ") #converting the number into string
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break # breaking from the while loop and returning the amount
            else:
                print("Enter a valied number of lines.")
        else:
            print("Please enter a valied number!")
    return lines
# input-amount that i need to bet on each line


def main():
    balance=deposit()
    lines=get_number_of_lines()
    print(balance,lines)

main()
