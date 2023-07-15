import os
import math
import random
import smtplib
S = "0123456789"
OTP = ""
for i in range(6):
    OTP += S[math.floor(random.random() * 10)]
otp = OTP + "is your OTP"
message = otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
id = input("Enter your email: ")
s.login("XXXXXXXXX@gmail.com", "XXXXXXXXX")
s.sendmail('&&&&&&', id, message)

otp = input("Enter your OTP: ")
if otp == OTP:
    print("Verified")
else:
    print("Incorrect OTP, Please Check your OTP again")



