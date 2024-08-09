import random # we need to generate slot machine values randomely(amount of items in each row and how long the lines to be)if you get 3 in row you win
# to make the program dynamic adding global constant
MAX_LINES=3# capitales coz this is a constant 
MAX_BET=100
MIN_BET=1
ROWS=3
COLUMNS=3

symbol_count={
    "A":2, # every single column we have 2 A's (symbol/count)
    "B":4,
    "C":6,
    "D":8

}
#generate the values
#all symboles list
def get_slot_machine_spin(rows,cols,symbols):
    # number of rows inside of each column
    all_symbols=[]
    for symbol,symbol_count in symbols.items():#add how many symbols we have into the symbols list/ iterating through a dictionery(.items-geting the key and the value)
        for _ in range(symbol_count): # _ annonymous variable
            all_symbols.append(symbol) # if the symbol count is 2 it loops 2 times into my all symboles list
#values go in every column
    columns=[]# nested list/ storing the columns/ columns= amount of rows
    for _ in range(cols): # every column we generate certain number of rows/symbols/ 3 columns= do the inside code 3 times
        #picking random values for each column
        column=[]
        current_symbols= all_symbols[:] # copy of the all symbol list
        for _ in range(rows): # loop through number of values we need to generate =number of rows we have in slot machine
            value=random.choice(current_symbols)# picks a random value from current_symbols list
            current_symbols.remove(value) # remove the value coz we shouldn't pick it again/find the first instance of the value in the list then remove 
            column.append(value)#adding value to the column empty list
        columns.append(column)# adding the colums to columns list
    return columns
def print_slot_machine(columns): #transposing- coz we have a matrix
    for row in range (len(columns[0])):#[0] we should at least have one column/ loop through every row we have/number of rows(number of elements in each column) in the columns
        for i,column in enumerate(columns): # enumerate- gives index and item/for each row we loop through every column/looping through all the items in the columns/ gives every column
            if i !=len(columns)-1:# max index
                print(column[row], end=' | ') # for every column we only print the current row that we in
            else:
                print(column[row],end='')# otherwise max index also gonna print | this
        print() #goes to the next line

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
# input-amount that user need to bet on each line
def get_bet():
    while True: # continusely ask the user to input a valied amount
        amount=input("How much would you like to bet? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break # breaking from the while loop and returning the amount
            else:
                print(f"The amount should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valied number!")
    return amount


def main():
    balance=deposit()
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance} ")
        else:
            break

    print(f"You're betting ${bet} on {lines} lines. The total bet is equal to: ${total_bet}")
   
# generate the slot machine
    slots=get_slot_machine_spin(ROWS,COLUMNS,symbol_count)# slots = columns= what in the each slot
    print_slot_machine(slots)
main()
