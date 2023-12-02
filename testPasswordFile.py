import unittest
import tempfile
import os
from passwordFile import *
class TestPasswordFileIO(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        # Close the file explicitly before removing it
        self.temp_file.close()

        # Remove the temporary file after testing
        os.remove(self.temp_file.name)

    def test_read_password_file_empty_file(self):
        users = read_password_file(self.temp_file.name)
        self.assertEqual(users, [])

    def test_read_password_file_nonempty_file(self):
        # Create a temporary file with sample data
        sample_data = "user1:salt1:hash1:group1:1:/home/user1\nuser2:salt2:hash2:group2:2:/home/user2\n"
        with open(self.temp_file.name, 'w') as file:
            file.write(sample_data)

        users = read_password_file(self.temp_file.name)
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, "user1")
        self.assertEqual(users[1].salt, b"salt2") 

    def test_write_pass_word_file(self):
        # Create some sample users
        user1 = User("user1", "password1", "group1", 1)
        user2 = User("user2", "password2", "group2", 2)
        users = [user1, user2]

        # Write users to the temporary file
        write_pass_word_file(users, passfile=self.temp_file.name)

        # Read the file and check if the content matches
        with open(self.temp_file.name, 'r') as file:
            written_content = file.read()

        self.assertTrue("user1" in written_content)

    def test_verify_password(self):
        user = User("User", "password","group", 1)
        self.asserTrue(user.verify_password("password"))
    
    def test_verify_password(self):
        user = User("User", "password","group", 1)
        self.assertFalse(user.verify_password("wrong"))
    

if __name__ == '__main__':
    unittest.main()