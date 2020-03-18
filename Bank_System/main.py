from database import *
from bankSystem import *
import os  # Os.system('cls) ----> Clear Screen
import atm
from atmBackend import card,currentBalance
def openAccounnt():
    """

    :return:
    """
    while True:
        user_input = int(input(
            "Please Select any one Option: \n 1) Create  Account \n 2) Create Care Number\n 3) Create ATM PIN \n "
            "4)Exit \n Select Number Please: "))
        if user_input == 1:
            os.system('cls')
            get_AlldataBanksystem()
            break
        elif user_input == 2:
            os.system('cls')
            cardNumber()
            pin()
        elif user_input == 3:
            os.system('cls')
            pin()
        elif user_input == 4:
            break
        else:
            print("Wrong Input please select right number: ")
            print()
            os.system('cls')

def useingATM():
    atm.welcomeATM()
    print(card, currentBalance )
    atm.atmWork()

def main():
    """
    Handling all program from by using Main() Function
    :return: NONE
    """
    while True:
        print("Welcome to China Bank")
        while True:
            os.system('cls')
            user_input = int(input("\n1) Open A New Account \n2) Using ATM Machine \n3) Exit\nPlease Select any option: "))
            if user_input == 1:
                os.system("cls")
                openAccounnt()
            elif user_input ==2:
                os.system('cls')
                useingATM()
            elif user_input ==3:
                break
            else:
                print("Wrong Input")
        break


if __name__ == "__main__":
    main()
    os.system('cls')
    print("Thank for using US")
