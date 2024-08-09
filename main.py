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
symbol_value={
    "A":5, # more rare the symbol is the higher your bet gets multiplied
    "B":4,
    "C":3,
    "D":2

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
        # 1 line = top
        #2 =top+middle
        #3= all 3 lines
        # check how much user won
def check_winnings(columns,lines,bet,values):
    # look through only the rows/lines they bet on
    winnings=0
    winning_lines=[]
    for line in range(lines): # lines=2 -> line 0 and 1, looping throu ever row/ checking user bet on
        #every single symbol in the line/row is the same
        symbol=columns[0][line] # the symbol we need to check is whatever the symbol in the first column,columns 0 -> we have all the columns not the rows
        for column in columns:# loops through every single column and check for that symbol
            symbol_to_check = column[line] # column at the current row we're looking/column 1st row/simbol/line
            if symbol!=symbol_to_check: #if the symbles are not the same we break and go to the 1st for loop and check the next line
                break# if we found one of the symbols not equels to previous symbol
        else:
            winnings+=values[symbol]*bet # bet on each line not the total bet/ coz they could win one line and loose other line
            winning_lines.append(line+1) # what line they won / line only gonna give index that's why we add 1
    return winnings,winning_lines



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

def spin(balance): # check the balance if user make a bet
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
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines) # unpack operator/ if user won 2 -> 1 2/ didn't win any it's not gonna say anything
    return winnings-total_bet # how much they won or lost from one instance
def main():
    balance=deposit() # this is gonna stay same but below code should run continuesly, and reduce from the balance
    while True:
        print(f"current balance is ${balance}")
        answer=input(f"Press enter to play or 'q' to quit.")
        if answer == 'q':
            break
        balance+=spin(balance)
    print(f"You left with $ {balance}")
#     lines=get_number_of_lines()
#     while True:
#         bet=get_bet()
#         total_bet=bet*lines
#         if total_bet>balance:
#             print(f"You do not have enough to bet that amount, your current balance is ${balance} ")
#         else:
#             break

#     print(f"You're betting ${bet} on {lines} lines. The total bet is equal to: ${total_bet}")
   
# # generate the slot machine
#     slots=get_slot_machine_spin(ROWS,COLUMNS,symbol_count)# slots = columns= what in the each slot
#     print_slot_machine(slots)
#     winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
#     print(f"You won ${winnings}")
#     print(f"You won on lines: ", *winning_lines) # unpack operator/ if user won 2 -> 1 2/ didn't win any it's not gonna say anything

main()
