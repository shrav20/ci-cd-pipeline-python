import os
import random
import re
import smtplib
# pylint: disable=import-error
from twilio.rest import Client
# pylint: enable=import-error

# pylint: disable=duplicate-code
class CreateCommunicatingService:
    def __init__(self, account_sid, auth_token, sender_email, sender_password):
        self.client = Client(account_sid, auth_token)
        self.sender_email = sender_email
        self.sender_password = sender_password

    @staticmethod
    def test_generate_otp(n=6):
        return ''.join(str(random.randint(0, 9)) for _ in range(n))

    def test_send_otp(self, message, receiver):
        raise NotImplementedError("Subclasses must implement this method.")

class CreateMobileService(CreateCommunicatingService):
    def __init__(self, account_sid, auth_token):
        super().__init__(account_sid, auth_token, None, None)

    @staticmethod
    def test_validate_mobile(mobile):
        return len(mobile) == 10 and mobile.isdigit()

    def test_send_otp(self, target_mobile, otp):   # pylint: disable=arguments-renamed
        if self.test_validate_mobile(target_mobile):
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

class CreateEmailService(CreateCommunicatingService):
    @staticmethod
    def test_validate_email(receiver):
        validation_condition = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.search(validation_condition, receiver))

    def test_send_otp(self, receiver_email, otp):  # pylint: disable=arguments-renamed
        if self.test_validate_email(receiver_email):
            body = f"Your OTP is {otp}. Valid for next 15 minutes."
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, receiver_email, body)
            print(f"Mail sent - OTP: {otp}")
        else:
            print("Please enter a valid email!!")

class GenerateOTPServices:
    # pylint: disable=R0913
    def __init__(self, account_sid, auth_token, twilio_num, sender_email, sender_password):
        self.mobile_service = CreateMobileService(account_sid, auth_token)
        self.email_service = CreateEmailService(account_sid, auth_token, sender_email, sender_password)  # Pass sender_email and sender_password here
        self.mobile_service.sender_email = sender_email
        self.email_service.sender_email = sender_email
        self.mobile_service.sender_password = sender_password
        self.email_service.sender_password = sender_password
        self.mobile_service.twilio_num = twilio_num
    # pylint: enable=R0913

    def test_send_otp(self, receiver, send_twilio=True, target_mobile=None):
        generated_otp = CreateCommunicatingService.test_generate_otp(6)

        if send_twilio:
            self.mobile_service.test_send_otp(target_mobile, generated_otp)

        self.email_service.test_send_otp(receiver, generated_otp)

if __name__ == "__main__":  # Corrected "__main__" instead of "_main_"
    print("Welcome to Random OTP sender!!\nHere, we send random OTPs to phone number and mails.\n")
    # pylint: disable=W0621
    account_sid_value = 'AC1a01a4fd1cc7cdbb358e19fe12b9ce93'  # pylint: disable=C0103
    auth_token_value = '1fbcb17dfe649c3d4476b8d0330e07dc'  # pylint: disable=C0103
    twilio_number = '+15735944610'  # pylint: disable=C0103
    sender_email = os.getenv('SENDER_EMAIL')  # pylint: disable=C0103
    sender_password = os.getenv('SENDER_PASSWORD')  # pylint: disable=C0103
    # pylint: enable=W0621
    otp_services = GenerateOTPServices(account_sid_value, auth_token_value, twilio_number, sender_email, sender_password)

    receiver_email = input("Enter mail: ")
    send_twilio = input("\nDo you want to send OTP via SMS: ")

    if send_twilio.lower() == "yes":
        target_mobile = input("Enter mobile: ")
        otp_services.test_send_otp(receiver_email, send_twilio=True, target_mobile=target_mobile)
    else:
        otp_services.test_send_otp(receiver_email, send_twilio=False)
