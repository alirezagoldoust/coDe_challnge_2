from user_manager import  User_manager
from user import User



class Auth:
    def __init__(self,username, password,  db : User_manager):
        self.password = password
        self.username = username
        self.db = db

    def login(self):
        u = self.db.search_by_username(self.username)

        if u.password == self.password:
                print("Login Successful")
                return u

        return None

    def signup(self):
        if self.db.duplicate_user(self.username):
            return None
        else:
            self.db.add_user(User(self.username, self.password, []))


    def logout(self):
        print("logout success")
        return  None





def print_menu():
    print("1.Follow")
    print("2.List of followers")
    print("3.List of following ")
    print("4.Send message")
    print("5.List of message")
    print("0.Exit")

def main():
    logout = False
    while not logout:
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")
        user = Auth(user_name, password, User_manager)
        if user.logout() == None:
            logout = True

        if user.login() == None:
            user.signup()
            user.login()
        while True:
            print_menu()
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Bye")
                break
            elif choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass


