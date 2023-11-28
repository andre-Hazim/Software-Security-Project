from enrollUser import UserInterface
from passwordFile import User, read_password_file 
from accessMatrix import AccessControlMatrix, Roles

def loginscreen():
    answer = input("Type “enroll” to enroll a user or “login” to login:").lower()
    if answer == "enroll":
        UserInterface.enrollUser()
        login()
    elif answer == "login":
        login()
    while not(answer == "enroll" or answer == "login"):
        if answer == "enroll":
            UserInterface.enrollUser()
            login()
        elif answer == "login":
            login()


def login():
    userid = input("User ID:")
    password = input("Password:")
    users = read_password_file('passwd.txt')
    can_login = False
    for u in users: 
        can_login = u.user_id == userid and u.verify_password(password)
        if can_login:
            good_u = u
    if can_login:
        print(good_u.user_id)
        
        acm = AccessControlMatrix()
        for r in Roles:
            if good_u.group == r.value:
                print(r)
                print(acm.get_role(r))

loginscreen()



