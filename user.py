class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.inbox = []
        self.followers = []
        self.following = []

    def follow(self, user) -> None:
        pass

    def add_message_to_inbox(self, message: Message) -> None:
        pass

    def view_message(self ,sender) -> None:
        pass





