import unittest
from login import login
class TestLoginFunction(unittest.TestCase):

    def setUp(self):
        # Assuming you have an instance of the class containing checkPass
        self.passwordFile = "testPasswordFile.txt"

    def test_successful_login(self):
        self.assertTrue(login("0", "Sample!2", self.passwordFile ))

    def test_unsuccessful_login(self):
        self.assertFalse(login("1","Testpass1@", self.passwordFile))
        self.assertFalse(login("1", "Sample!2", self.passwordFile))
if __name__ == '__main__':
    unittest.main()
