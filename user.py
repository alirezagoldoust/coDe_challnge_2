from typing import Any
from user_manager import User_manager
from message import Message
from auth import Auth

import user_manager
from re import search



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.inbox = []
        self.followers = []
        self.following = []

    def follow(self, username) -> Any | None:
        if username not in self.following:
            if User_manager.search_user(username) != None:
                self.following.append(User_manager.search_user(username))
        else:
            return False

    def send_message(self, text: str, reciever: int) -> None:
        message = Message(self.username, text, User_manager.users[reciever].username)
        User_manager.users[reciever].inbox.append(message)

    def view_inbox(self , only_read) -> None:
        for message in self.inbox:
            message.show_message(only_read)

    def get_username(self):
        return self.username




