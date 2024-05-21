# pylint: disable=wrong-import-order
import random
import re
import smtplib
# pylint: enable=wrong-import-order
# pylint: disable=import-error
import streamlit as st
# pylint: enable=import-error


class CreateCommunicatingService:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    @staticmethod
    def generate_otp(n=6):
        return ''.join(str(random.randint(0, 9)) for _ in range(n))

    def send_otp(self, receiver_email):
        raise NotImplementedError("Subclasses must implement this method.")

class CreateEmailService(CreateCommunicatingService):
    @staticmethod
    def validate_email(receiver):
        validation_condition = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.search(validation_condition, receiver))

    def send_otp(self, receiver_email):
        # pylint: disable=duplicate-code
        if self.validate_email(receiver_email):
            otp = self.generate_otp()
            body = f"Your OTP is {otp}. Valid for next 15 minutes."
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, receiver_email, body)
            return otp
        return None

class VerifyOTPServices:
    def __init__(self, sender_email, sender_password):
        self.email_service = CreateEmailService(sender_email, sender_password)

    def verify_otp(self, entered_otp, generated_otp):
        return generated_otp == entered_otp

def main():
    st.title("OTP Verification")

    # Initialize session state
    session_state = st.session_state

    sender_email = "swanandbhuskute567@gmail.com"
    sender_password = "gvkguusgyahnhnfe"

    receiver_email = st.text_input("Enter your email:")
    if st.button("Send OTP"):
        otp_service = CreateEmailService(sender_email, sender_password)
        generated_otp = otp_service.send_otp(receiver_email)
        if generated_otp:
            session_state.generated_otp = generated_otp
            st.write("OTP sent to your email.")

    entered_otp = st.text_input("Enter the OTP received on your email:")
    if st.button("Verify OTP"):
        if hasattr(session_state, 'generated_otp'):
            otp_verifier = VerifyOTPServices(sender_email, sender_password)
            if otp_verifier.verify_otp(entered_otp, session_state.generated_otp):
                st.write("OTP verified successfully!")
                st.write("and here we go")
            else:
                st.write("OTP verification failed. Please check your OTP and try again.")
        else:
            st.write("Please send OTP first.")

if __name__ == "__main__":
    main()
