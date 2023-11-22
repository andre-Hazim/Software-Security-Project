import os
import bcrypt

class User:
    def __init__(self, username:str, password:str, group_id:int, user_id:int,home_dir:str):
        self.username = username
        self.salt = bcrypt.gensalt()
        self.salted_hash = bcrypt.hashpw(password.encode('utf-8'), self.salt)
        self.group_id = group_id
        self.user_id = user_id
        self.home_dir = home_dir

    def verify_password(self, entered_password):
        hashed_entered_password = bcrypt.hashpw(entered_password.encode('utf-8'), self.salt)
        return hashed_entered_password == self.salted_hash

    def to_string(self):
        return f"{self.username}:{self.salt.decode('utf-8')}:{self.salted_hash.decode('utf-8')}:{self.group_id}:{self.user_id}:{self.home_dir}"

def write_pass_word_file(users):
    passfile = "passwd.txt"
    
    print(os.path.isfile(passfile))
    
    # Check if the file exists; if not, create it
    if not os.path.isfile(passfile):
        open(passfile, 'w').close()

    # Check file permissions
    if not os.access(passfile, os.W_OK):
        raise PermissionError(f"You don't have permission to write to {passfile}.")

    with open(passfile, "a") as file:
        for user in users:
            file.write(user.to_string() + "\n")

existing_users = []
new_user = User("new_user", "new_password", "new_group", "new_id", "/home")
existing_users.append(new_user)
new_user = User("new_user2", "new_password", "new_group", "new_id","/home")
existing_users.append(new_user)

write_pass_word_file(existing_users)
