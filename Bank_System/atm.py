from atmBackend import *
import os

card = 0
balance_data = 0
def welcomeATM():
    while True:
        print("Please Enter Your  Card and PIN Details")
        global card
        card = input("Enter Card Details Here: ")
        pin = input("Enter Pin Details Here: ")
        if checkATM_input(atmcard=card, atmPin=pin) == card:
            os.system('cls')
            return card
        else:
            os.system('cls')


def atmWork():
    while True:
        global balance_data
        print("Select any one option.\n1) Check Balance\n2) Banking\n3) Return Card")
        user_input = int(input("Enter Here: "))

        if user_input == 1:
            balance_data = checkBalance()
            print(balance_data)
        elif user_input == 2:
            balance_data = balance(balance_data)
            add_DataInFile(balances=balance_data)
            balance_data = balance_data
        elif user_input == 3:
            add_DataInFile(balances=balance_data)
            break
        else:
            print("Please Enter Correct Option")
            os.system('cls')


if __name__ == "__main__":
    welcomeATM()
    atmWork()
