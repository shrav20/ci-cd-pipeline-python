# Import your functions here

import pytest
import otp_swanand_2130331245033 as otp
import unittest


class TestOTPFunctions(unittest.TestCase):

    def test_generateOtp(self):
        """Test the generateOtp function."""
        result = otp.generateOtp(8)
        expected_len = 8

        result_isint = result.isdigit()
        expected_isint = True #if number contains all digits

        self.assertEqual(len(result), expected_len)
        self.assertEqual(result_isint, expected_isint)
        

    def test_validateEmailID(self):
        """Test validate Email."""
        result = otp.validateEmailID("test@gmail.com")
        expected = True

        self.assertEqual(result, expected)

        result = otp.validateEmailID("test@dbatu.ac.in")

        self.assertEqual(result, expected)
        

    def test_validateMobile(self):
        """Test validate Mobile number."""
        mobile = "8625847883"
        result = otp.validateMobile(mobile)
        expected = True

        self.assertEqual(result, expected)
    

    
if __name__ == "__main__":
    pytest.main()
