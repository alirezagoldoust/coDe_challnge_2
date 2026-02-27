from user_manager import  User_manager
from user import User



class Auth:
    def __init__(self,username, password,  db : User_manager):
        self.password = password
        self.username = username
        self.db: User_manager = db

    def login(self):
        u = self.db.search_user(self.username)

        if u.password == self.password:
                return u

        return None

    def signup(self):
        if self.db.duplicate_user(self.username):
            return None
        else:
            u = User(self.username, self.password)
            self.db.add_user(u)
            return u


    def logout(self):
        return  None





def print_menu():
    print("1.Follow")
    print("2.List of followers")
    print("3.List of following ")
    print("4.Send message")
    print("5.List of message")
    print("0.Exit")

def preview_menu():
    print("1.login")
    print("2.signup")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")
        user = Auth(user_name, password, User_manager)
        return user.login()

    elif choice == 2:
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")
        user = Auth(user_name, password, User_manager)
        return user.signup()

def main():
        active_user = preview_menu()
        while True:
            print_menu()
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Bye")
                break
            elif choice == "1":
                user = User(user_name, password, [])

            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass


