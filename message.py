class Message:
    def __init__(self, sender, text , reciver):
        self.sender = sender
        self.text = text
        self.read = False
        self.reciver = reciver

    
    
    def show_message(self, only_unread=True):
        if (not self.read) or (not only_unread):
            print(f"{self.sender} : {self.text}")
            self.read = True    
        
