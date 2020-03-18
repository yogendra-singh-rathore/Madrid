import os
import bankSystem
import xlsxwriter

def createFile():
    """
    Create a Database File to store data from bank
    :return: database file (database.txt)
    """
    if os.path.isfile("database.txt"):
        pass
    else:
        print("Creating file ....")
        workbook = xlsxwriter.Workbook('database.xlsx')
        workbook.close()


def get_AlldataBanksystem():
    """
    Storing All Details from Bank System.py
    :return: Name, Account Number, Card number, PIN
    """
    createFile()
    tup_data = bankSystem.userForm()
    accountNumber= bankSystem.accountNumber()
    cardNumber = bankSystem.cardNumber()
    pin = bankSystem.pin()
    return append_Data(name=tup_data[0],age=tup_data[1],account_Number=accountNumber,card_Number=cardNumber,PIN=pin)


def append_Data(name=None, age=None, account_Number=None, card_Number=None, PIN=None):
    workbook = xlsxwriter.op
    insert_stringData = ""
    data = [name, age, account_Number, card_Number, PIN]
    while True:
        for get_val in data[1:]:
            insert_stringData = insert_stringData + " " + str(get_val)
        insert_stringData = "Customer Details: "+ " " + data[0] + insert_stringData
        break

    file.write(insert_stringData)
    file.write("\n")
    file.close()


if __name__ == "__main__":
    get_AlldataBanksystem()

# append_Data(append_Data(name="Yogi",age=24,account_Number=12345,card_Number=14526, PIN=0000))
