from re import search
from typing import Any


class User_manager:
    def __init__(self):
        self.users = []
    def search_user(self, username) -> Any | None:
        for user in self.users:
            if user.get_username() == username:
                return user
        else:
            return None

    def duplicate_user(self, username)-> bool:
        for user in self.users:
            if user.get_username() == username:
                return True
        else:
            return False

    def add_user(self, User)-> bool:
        if self.duplicate_user(User.username) == False:
            self.users.append(User)
            return True
        else:
            return False

