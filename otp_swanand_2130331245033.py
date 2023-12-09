import random
import re
import smtplib
from twilio.rest import Client

class CommunicationService:
    def _init_(self, account_sid, auth_token, sender_email, sender_password):
        self.client = Client(account_sid, auth_token)
        self.sender_email = sender_email
        self.sender_password = sender_password

    @staticmethod
    def generate_otp(n=6):
        return ''.join(str(random.randint(0, 9)) for _ in range(n))

    def send_otp(self, message, receiver):
        raise NotImplementedError("Subclasses must implement this method.")

class MobileService(CommunicationService):
    def _init_(self, account_sid, auth_token):
        super()._init_(account_sid, auth_token, None, None)

    @staticmethod
    def validate_mobile(mobile):
        return len(mobile) == 10 and mobile.isdigit()

    def send_otp(self, target_mobile, otp):
        if self.validate_mobile(target_mobile):
            target_mobile = "+91" + target_mobile
            message = self.client.messages.create(
                body=f"Your OTP is {otp}. Valid for next 15 minutes.",
                from_=self.sender_email,
                to=target_mobile
            )
            print(message.body)
            print(f"Check Phone! Sent to {target_mobile}")
        else:
            print("Enter a valid mobile number!!")

class EmailService(CommunicationService):
    @staticmethod
    def validate_email(receiver):
        validation_condition = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.search(validation_condition, receiver))

    def send_otp(self, receiver_email, otp):
        if self.validate_email(receiver_email):
            body = f"Your OTP is {otp}. Valid for next 15 minutes."
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, receiver_email, body)
            print(f"Mail sent - OTP: {otp}")
        else:
            print("Please enter a valid email!!")

class OTPServices:
    def _init_(self, account_sid, auth_token, twilio_num, sender_email, sender_password):
        self.mobile_service = MobileService(account_sid, auth_token)
        self.email_service = EmailService(account_sid, auth_token)
        self.mobile_service.sender_email = sender_email
        self.email_service.sender_email = sender_email
        self.mobile_service.sender_password = sender_password
        self.email_service.sender_password = sender_password
        self.mobile_service.twilio_num = twilio_num

    def send_otp(self, receiver, send_twilio=True, target_mobile=None):
        generated_otp = CommunicationService.generate_otp(6)

        if send_twilio:
            self.mobile_service.send_otp(target_mobile, generated_otp)

        self.email_service.send_otp(receiver, generated_otp)

if _name_ == "_main_":
    print("Welcome to Random OTP sender!!\nHere, we send random OTPs to phone number and mails.\n")

    account_sid_value = 'AC1a01a4fd1cc7cdbb358e19fe12b9ce93'
    auth_token_value = '1fbcb17dfe649c3d4476b8d0330e07dc'
    twilio_number = '+15735944610'
    sender_email = "swanandbhuskute567@gmail.com"
    sender_password = "gvkguusgyahnhnfe"

    otp_services = OTPServices(account_sid_value, auth_token_value, twilio_number, sender_email, sender_password)

    receiver_email = input("Enter mail: ")
    send_twilio = input("\nDo you want to send OTP via SMS: ")

    if send_twilio.lower() == "yes":
        target_mobile = input("Enter mobile: ")
        otp_services.send_otp(receiver_email, send_twilio=True, target_mobile=target_mobile)
    else:
        otp_services.send_otp(receiver_email, send_twilio=False)

    print("\nOTP sending program ended\n")
    # Program Ended
