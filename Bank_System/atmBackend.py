import os
import atm

card = 0
index_no = 0
currentBalance = 0
def read_Database():
    """
    Read All data from database file and stored in data
    :return: Data
    """
    createFile()
    file = open("database.txt", "r")
    data = file.readlines()
    file.close()
    return data


def checkATM_input(atmPin, atmcard):
    """
    Checking User Card and PIN Details from Database
    :param atmPin: User ATM PIN
    :param atmcard: USER ATM CARD
    :return: Card Number Details
    """
    global card
    card = atmcard
    data = read_Database()
    for get_val in data:
        if atmPin in get_val and atmcard in get_val :
            get_val_list = get_val.split()
            os.system('cls')
            print("Welcome to China Bank ATM ",get_val_list[2])
            return atmcard
    else:
        print("Please Enter Correct Card Details: ")


def createFile():
    """
    Creating Account Balance Management File
    :return:
    """
    if os.path.isfile("accountBalance.txt"):
        pass
    else:
        print("Creating file ....")
        file = open("accountBalance.txt", "w")
        file.close()


def balance(balance_stored = None):
    os.system('cls')
    global currentBalance
    currentBalance = int(balance_stored)
    while True:
        print("Select any one option:\n 1)Add Amount\n 2)Balance Withdrawal\n 3) Return Back")
        user_input = int(input("Enter Here: "))
        if user_input ==1:
            amount = int(input("Enter Amount for Deposit: "))
            currentBalance = currentBalance + amount
            os.system('cls')
            return currentBalance
        elif user_input ==2:
            wamount = int(input("Enter Amount to withdrawal: "))
            currentBalance = currentBalance - wamount
            os.system('cls')
            return currentBalance
        elif user_input ==3:
            return currentBalance
        else:
            os.system('cls')
            return currentBalance


def balance_readData():
    global card
    global index_no
    file = open("accountBalance.txt","r")
    data = file.readlines()
    get_len = len(data)
    while index_no<get_len:
        if str(card) in data[index_no]:
            break
        index_no +=1
    file.close()
    return data

def checkBalance():
    global card
    global index_no
    global currentBalance
    file = open("accountBalance.txt","r")
    data = file.readlines()
    get_len = len(data)
    while index_no<get_len:
        if str(card) in data[index_no]:
            update_balance = data[index_no]
            currentBalance = update_balance
            return update_balance[6:]
        index_no +=1
    file.close()
    add_DataInFile(balances=0)
    return currentBalance


def add_DataInFile(cards=None,balances=None):
    createFile()
    global index_no
    global card
    cards = str(card)
    balances = str(balances)
    final = cards+" "+balances
    data = balance_readData()
    file = open("accountBalance.txt", "w")
    if balances =="0":
        file.writelines(final)
        file.close()
    elif final != data[index_no]:
        data[index_no] = final+"\n"
        file.writelines(data)
        file.close()
    else:
        file.writelines(data)
        file.close()



if __name__ == "__main__":
    pass