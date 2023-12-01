import re
import accessMatrix
from passwordFile import User, read_password_file,write_pass_word_file
class UserInterface():
    def __init__(self) -> None:
        self.userid = str()
        self.group = str()
        self.password = str()

    
    def _print_instructions(self):
        print("Passwords must be least 8-12 characters in length")
        print("Password must include at least:")
        print("one upper-case letter;")
        print("one lower-case letter;")
        print("one numerical digit, and")
        print("one special character from the set: {!, @, #, $, %, ?, ∗}")
        print("Passwords found on a list of common weak passwords (e.g., Password1, Qwerty123, or Qaz123wsx)")
        print("are be prohibited")
        print("Passwords matching the format of calendar dates, license plate numbers, telephone numbers, or other")
        print("common numbers are be prohibited")
        print("Passwords matching the user ID are be prohibited")


    def checkGroup(self):
        good_group = False;
        for r in accessMatrix.Roles:
                if self.group == str(r.value):
                    good_group = True
        if not good_group:
            print("group not found\npick from these:")
            for r in accessMatrix.Roles:
                print(r.value)
        return good_group

    def enrollUser(self):
        self.userid = len(read_password_file("passwd.txt"))
        self.username = input('Enter your username:')
        self.group = input('Enter your group:')
        good_group= False
        while not good_group:
            good_group = self.checkGroup()
            if not good_group:
                self.group = input('Enter your group:')    
        self.password = input('Enter your password:')
        double_pass = input ("Enter password again:")
        while not self.password == double_pass:
            print("passwords do not match")
            self.password = input('Enter your password:')
            double_pass = input ("Enter password again:")
        pass_checker = PassChecker()
        while not pass_checker.checkPass(self.password,self.userid):
            self._print_instructions()
            self.password = input('Enter your password:')
            double_pass = input ("Enter password again:")

        enrolled_user = [User(self.username,self.password,self.group,self.userid)]
        write_pass_word_file(enrolled_user)
        print(f"account sucesfully created with id: {self.userid}")
class PassChecker():
    def checkPass(self, password:str,userid:str) -> bool:
            #Check from proper length 
            if len(password) < 8 or len(password) > 12:
                return False
            
            # Check for at least one upper-case letter
            if not any(char.isupper() for char in password):
                return False

            # Check for at least one lower-case letter
            if not any(char.islower() for char in password):
                return False

            # Check for at least one numerical digit
            if not any(char.isdigit() for char in password):
                return False

            # Check for at least one special character
            special_characters = {'!', '@', '#', '$', '%', '?', '*'}
            if not any(char in special_characters for char in password):
                return False

            # Check against common weak passwords
            if self.is_common_weak_password(password):
                return False

            # Check for prohibited formats (e.g., calendar dates, license plate numbers)
            if self.is_prohibited_format(password):
                return False

            # Check if the password matches the user ID
            if self.matches_user_id(password,userid):
                return False

            # If all checks pass, the password is valid
            return True
    
    def is_common_weak_password(self,password):
        with open("commonpass.txt", 'r') as file:
            lines = file.readlines()
        
        return password in lines

    def is_prohibited_format(self,password):
        # Check for calendar date format (MM/DD/YYYY or YYYY-MM-DD) first part is month and day(1 or 2 digits) and year(4 digits) 
        # after | is the other format
        date_formats = re.compile(r'\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b')
        if date_formats.search(password):
            return True

        # Check for license plate number format (e.g., ABC123 or 123ABC)
        license_plate_formats = re.compile(r'\b[A-Za-z]{3}\d{3}\b|\b\d{3}[A-Za-z]{3}\b')
        if license_plate_formats.search(password):
            return True

        # Check for telephone number format (e.g., (123) 456-7890)
        telephone_formats = re.compile(r'\(?\d{3}\)?[ -]?\d{3}[-]?\d{4}')
        if telephone_formats.search(password):
            return True

        # Check for other common number patterns (e.g., 1234567)
        common_number_formats = re.compile(r'\b\d{8,12}\b')
        if common_number_formats.search(password):
            return True

        # If no prohibited format is detected, return False
        return False
    def matches_user_id(self,password,userid):
        return password == userid
