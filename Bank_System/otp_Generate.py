# import library
import math, random, smtplib


# function to generate OTP
def generateOTP():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

    # length of password can be chaged
    # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


def email(otp):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login("testdataml143@gmail.com", "Faber48Castell@18")  # Email and Password
    connection.sendmail("testdataml143@gmail.com", "testdataml143@gmail.com", "subject: OTP:{}".format(otp))
    connection.quit()
    print("Finish")


# Driver code
if __name__ == "__main__":
    get_otp = generateOTP()
    print("OTP of 4 digits:", get_otp)
    email(get_otp)
