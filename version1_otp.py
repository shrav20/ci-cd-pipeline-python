# OTP to mail

import smtplib
import random

SENDER = "swanandbhuskute567@gmail.com"
PASSWORD = "gvkguusgyahnhnfe"
RECEIVER = "swanandtest85@gmail.com"
BODY = "Your OTP is " + str(random.randint(100000, 999999)) + ". Valid for next 15 minutes."

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(SENDER, PASSWORD)

server.sendmail(SENDER, RECEIVER, BODY)

print("Mail sent")
