import os
import bcrypt
from accessMatrix import Roles
from typing import List
class User:
    def __init__(self, username:str, password:str, group:Roles, user_id:int, salt=bcrypt.gensalt()):
        self.username = username
        self.salt = salt
        self.salted_hash = bcrypt.hashpw(password.encode('utf-8'), self.salt)
        self.group= group
        self.user_id = user_id
        self.home_dir = f'/home/{self.username}'

    def verify_password(self, entered_password):
        hashed_entered_password = bcrypt.hashpw(entered_password.encode('utf-8'), self.salt)
        return hashed_entered_password == self.salted_hash

    def to_string(self):
        return f"{self.username}:{self.salt.decode('utf-8')}:{self.salted_hash.decode('utf-8')}:{self.group}:{self.user_id}:{self.home_dir}"

def read_password_file(file_path)-> List[User]:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    users = []
    if not len(lines) ==0:
        for line in lines:
            parts = line.strip().split(':')
            username, salt, salted_hash, group, user_id, homedir = parts
            group_Enum = None
            for r in Roles:
                if r.value == group:
                    group_Enum= r
            user = User(username, '', group_Enum, user_id)
            user.salt = salt.encode('utf-8')
            user.salted_hash = salted_hash.encode('utf-8')
            users.append(user)

        return users
    else:
        return []

def write_pass_word_file(users, passfile= "passwd.txt"):

    
    # Check if the file exists; if not, create it
    if not os.path.isfile(passfile):
        open(passfile, 'w').close()

    # Check file permissions
    if not os.access(passfile, os.W_OK):
        raise PermissionError(f"You don't have permission to write to {passfile}.")

    with open(passfile, "a") as file:
        for user in users:
            file.write(user.to_string() + "\n")


