class Message:
    def __init__(self, body: str, sentBy: str = None, sentIn:str = None):
        self.sentBy = sentBy
        self.sentIn = sentIn
        self.body = body

    def __eq__(self, other):
        if isinstance(other, Message):
            return self.body == other.body and self.sentBy == other.sentBy and self.sentIn == other.sentIn
        return False
