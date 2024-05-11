import unittest
import pytest
import test_otp_swanand_2130331245033 as otp
# pylint: disable=duplicate-code
class ComputeOTPFunctions(unittest.TestCase):

    def test_generate_otp_function(self):
        """Test the generate_otp function."""
        result = otp.CreateCommunicatingService.test_generate_otp(8)
        expected_len = 8

        result_isint = result.isdigit()
        expected_isint = True #if number contains all digits

        self.assertEqual(len(result), expected_len)
        self.assertEqual(result_isint, expected_isint)

    def test_validate_emailid_function(self):
        """Test validate Email."""
        result = otp.CreateEmailService.test_validate_email("test@gmail.com")
        expected = True

        self.assertEqual(result, expected)

        result = otp.CreateEmailService.test_validate_email("test@dbatu.ac.in")
        self.assertEqual(result, expected)

    def test_validate_mobile_function(self):
        """Test validate Mobile number."""
        mobile = "8625847883"
        result = otp.CreateMobileService.test_validate_mobile(mobile)
        expected = True

        self.assertEqual(result, expected)

if __name__ == "__main__":
    pytest.main()
