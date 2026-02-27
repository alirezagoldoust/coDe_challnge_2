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

def print_menu():
    print("1.Follow")
    print("2.List of followers")
    print("3.List of following ")
    print("4.Send message")
    print("5.List of message")
    print("0.Exit")

def preview_menu(user_manager : User_manager):
    print("1.login")
    print("2.signup")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")
        auth = Auth(user_name, password, user_manager)
        return auth.login()

    elif choice == 2:
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")
        auth = Auth(user_name, password, user_manager)
        return auth.signup()

def main():
    user_manager = User_manager()
    while True:
        active_user = preview_menu(user_manager)
        active_user: User
        while active_user:
            print_menu()
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Bye")
                active_user = None
                break
            elif choice == "1":
                user_name = input("Enter your username: ")
                user = user_manager.search_user(user_name)
                if user:
                    active_user.follow(user)

            elif choice == "2":
                active_user.print_followers()

            elif choice == "3":
                active_user.print_following()

            elif choice == "4":
                active_user.print_following()
                receiver = int(input("Enter your receiver: ")) - 1
                message = input("Enter your message: ")
                active_user.send_message(message, receiver)

            elif choice == "5":
                active_user.view_inbox(only_read=True)

main()

