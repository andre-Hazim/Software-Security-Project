from enrollUser import * 
import accessMatrix 
import unittest

class TestPasswordChecker(unittest.TestCase):

    def setUp(self):
        # Assuming you have an instance of the class containing checkPass
        self.password_checker = PassChecker()
        self.ui = UserInterface()

    def test_valid_password(self):
        # Test with a valid password
        result = self.password_checker.checkPass("SuperCool1!", "user123")
        self.assertTrue(result)

    def test_short_password(self):
        # Test with a password shorter than 8 characters
        result = self.password_checker.checkPass("Short1!", "user123")
        self.assertFalse(result)

    def test_long_password(self):
        # Test with a password longer than 12 characters
        result = self.password_checker.checkPass("VeryLongPassword123!", "user123")
        self.assertFalse(result)

    def test_missing_uppercase(self):
        # Test with a password missing an uppercase letter
        result = self.password_checker.checkPass("nopassword123!", "user123")
        self.assertFalse(result)

    def test_missing_lowercase(self):
        # Test with a password missing a lowercase letter
        result = self.password_checker.checkPass("NOPASSWORD123!", "user123")
        self.assertFalse(result)

    def test_missing_digit(self):
        # Test with a password missing a numerical digit
        result = self.password_checker.checkPass("NoPassword!", "user123")
        self.assertFalse(result)

    def test_missing_special_character(self):
        # Test with a password missing a special character
        result = self.password_checker.checkPass("NoPassword123", "user123")
        self.assertFalse(result)

    def test_common_weak_password(self):
        # Test with a common weak password
        result = self.password_checker.checkPass("password", "user123")
        self.assertFalse(result)

    def test_prohibited_format(self):
        # Test with a password in a prohibited format
        result = self.password_checker.checkPass("20211201", "user123")
        self.assertFalse(result)

    def test_calendar_date_format(self):
        # Test with a password containing a calendar date format
        result = self.password_checker.is_prohibited_format("20211201")
        self.assertTrue(result)

    def test_license_plate_format(self):
        # Test with a password containing a license plate number format
        result = self.password_checker.is_prohibited_format("ABC123")
        self.assertTrue(result)

    def test_telephone_number_format(self):
        # Test with a password containing a telephone number format
        result = self.password_checker.is_prohibited_format("(123) 456-7890")
        self.assertTrue(result)

    def test_common_number_format(self):
        # Test with a password containing a common number format
        result = self.password_checker.is_prohibited_format("123456789")
        self.assertTrue(result)


    def test_matches_user_id(self):
        # Test with a password that matches the user ID
        result = self.password_checker.checkPass("user123", "user123")
        self.assertFalse(result)

    def test_check_group(self):
        good_group = []
        for r in accessMatrix.Roles:
            self.ui.group = r.value
            good_group.append(self.ui.checkGroup())
        self.assertTrue(all(good_group))
    
    def test_check_group_not_in(self):
        self.ui.group = "super client"
        self.assertFalse(self.ui.checkGroup())

            

if __name__ == '__main__':
    unittest.main()
