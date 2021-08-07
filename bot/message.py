class Message(object):
    def __init__(self, body, sentBy = "unknown", sentIn = "unknown"):
        self.sentBy = sentBy
        self.sentIn = sentIn
        self.body = body