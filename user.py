from typing import Any
from user_manager import User_manager
from message import Message


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.inbox = []
        self.followers = []
        self.following = []

    def follow(self, other_user) -> Any | None:
        self.following.append(other_user)
        other_user.followers.append(self)

    def send_message(self, text: str, reciever: int) -> None:
        message = Message(self.username, text, self.following[reciever].username)
        self.following[reciever].inbox.append(message)

    def view_inbox(self , only_read) -> None:
        for message in self.inbox:
            message.show_message(only_read)

    def get_username(self):
        return self.username

    def print_followers(self):
        for i, user in enumerate(self.followers):
            print(f"{i + 1}. {user.username}")

    def print_following(self):
        for i, user in enumerate(self.following):
            print(f"{i + 1}. {user.username}")




