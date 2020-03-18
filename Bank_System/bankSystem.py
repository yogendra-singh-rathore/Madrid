def splitName(name):
    newName = ""
    space = " "
    for i in name.split():
        newName = newName+ space + i
    return newName[1:]


def userForm():
    """
    Getting User Details by using Input Function
    :return: Name(Str) and Age (Int) ----> Tuple Data
    """
    while True:
        name = input("Enter Your Name Here :")
        if splitName(name):
            break
        else:
            print("Please Enter Your Name Correctly")
    while True:
        age = input("Enter age here :")
        if age.isnumeric() and len(age) == 2:
            age = int(age)
            if age >= 18 and age <= 99:
                break
            else:
                print("Enter age in correctly between 18 to 99")
        else:
            print("Enter age in Numbers")
    return name, age


def accountNumber():
    """
    Creating Account Number according to user
    :return: Account Number (int)
    """
    while True:
        account_Number = input("Enter 5 digit Account Number here: ")
        checkAccount(account_Number)
        if len(account_Number) == 5:
            account_Number = int(account_Number)
            break
        else:
            print("Please Enter 5 Digit Account Number Only: ")
    return account_Number


def checkAccount(checkData):
    """
    Checking if account number is exist then we need another account number
    :return: Account Number Function so we can get another number
    """
    check_data = str(checkData)
    file = open("database.txt", "r")
    data = file.read()
    if check_data in data:
        print("Account Number is not available try another number")
        return accountNumber()
    else:
        pass


def cardNumber():
    """
    Getting Card Number from user
    :return: Card Number
    """
    while True:
        card_Number = input("Enter 5 Digit Card Number Here: ")
        checkCardNumber(card_Number)
        if len(card_Number) == 5:
            card_Number = int(card_Number)
            break
        else:
            print("Please Enter 5 Digit Card Number Only: ")
    return card_Number


def checkCardNumber(checkData):
    """
    Checking Card is exist or not
    :return: Card Number function
    """
    check_data = str(checkData)
    file = open("database.txt", "r")
    data = file.read()
    if check_data in data:
        print("Card Number is not available try another number")
        return cardNumber()
    else:
        pass


def pin():
    """
    Getting PIN number form user
    :return: PIN Number
    """
    while True:
        PIN = input("Enter 4 Digit PIN Number Here: ")
        len_pin = len(PIN)
        if len_pin == 4 and PIN.isnumeric():
            PIN = int(PIN)
            break
        else:
            print("Please Enter 4 Digit PIN Number Only: ")
    return PIN




if __name__ == "__main__":
    accountNumber()