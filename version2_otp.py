import unittest
import pytest
import otp_swanand_2130331245033 as otp

class ComputeOTPFunctions(unittest.TestCase):

    def test_generate_otp(self):
        """Test the generate_otp function."""
        result = otp.CreateCommunicatingService.generate_otp(8)
        expected_len = 8

        result_isint = result.isdigit()
        expected_isint = True #if number contains all digits

        self.assertEqual(len(result), expected_len)
        self.assertEqual(result_isint, expected_isint)

    def test_validate_emailid(self):
        """Test validate Email."""
        result = otp.EmailService.validate_email("test@gmail.com")
        expected = True

        self.assertEqual(result, expected)

        result = otp.EmailService.validate_email("test@dbatu.ac.in")
        self.assertEqual(result, expected)

    def test_validate_mobile(self):
        """Test validate Mobile number."""
        mobile = "8625847883"
        result = otp.MobileService.validate_mobile(mobile)
        expected = True

        self.assertEqual(result, expected)

if __name__ == "__main__":
    pytest.main()
