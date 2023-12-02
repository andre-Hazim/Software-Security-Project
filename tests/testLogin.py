import unittest
from login import login
from unittest.mock import patch
import datetime

class TestLoginFunction(unittest.TestCase):

    def setUp(self):
        # Assuming you have an instance of the class containing checkPass
        self.passwordFile = "testPasswordFile.txt"

    def test_successful_login(self):
        self.assertTrue(login("0", "Sample!2", self.passwordFile ))

    @patch('login.datetime')
    def test_teller_out_hours(self,mock_datetime):
        # Mock the current time for the duration of this test
        mock_time = datetime.datetime(2023, 1, 1, 8, 0, 0)
        
        mock_datetime.now.return_value = mock_time
        self.assertFalse(login("0", "Sample!2", self.passwordFile ))
        
    def test_unsuccessful_login(self):
        self.assertFalse(login("1","Testpass1@", self.passwordFile))
        self.assertFalse(login("1", "Sample!2", self.passwordFile))

if __name__ == '__main__':
    unittest.main()
