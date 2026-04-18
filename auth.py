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



