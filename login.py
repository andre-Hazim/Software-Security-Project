from enrollUser import UserInterface
from passwordFile import User, read_password_file 
from accessMatrix import AccessControlMatrix, Roles, Resources
from datetime import datetime, time

global_user = User("None","None","None",-1)
global_acm = AccessControlMatrix()
def loginscreen():
    ui = UserInterface()
    answer = ""
    while True:
        answer = input("Type 'enroll' to enroll a user or 'login' to login or 'exit' to exit:").lower()
        if answer == "enroll":
            ui.enrollUser()
        elif answer.lower() == "login":
            userid = input("User ID:")
            password = input("Password:")
            if(login(userid, password)):
                resource = ""
                print("enter resource or 'help' for list")
                print("Type 'logout' to logout")
                while not resource == "logout":
                    resource = input("Request Resource: ")
                    response = logged_in(resource.upper())
                    print(response)
            else:
                print("Wrong Username/Password")
        elif answer.lower() == "exit":
            exit()
       


def login(userid, password, passwordFilePath='passwd.txt'):
    global global_user
    users = read_password_file(passwordFilePath)
    can_login = False
    for u in users: 
        if u.user_id == userid and u.verify_password(password):
            can_login = True
            global_user = u
    if can_login and global_user.group == Roles.TELLER:
         # Get the current time
            currentTime = datetime.now().time()

            # Define business hours range
            businessStartTime = time(9, 0)
            businessEndTime = time(17, 0)

            # Check if the current time is outside business hours
            outsideHours = currentTime < businessStartTime or currentTime > businessEndTime
            if outsideHours:
                print("Tellers cannot login after/before work hours")
                return False
        
                
                
    return can_login

def logged_in(resource:str):
    global global_user, global_acm
    right = str()
    if resource == "HELP":
        return str(list(r.value for r in Resources))
    elif resource == "LOGOUT":
        return ""
    right = global_acm.get_access(global_user.group, resource)
    if (right == '---'):
        return 'no access'
    else: return(right)

