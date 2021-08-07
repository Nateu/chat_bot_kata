from message import message


class ChatBot(object):
    def __init__(self):
        self.theme = dict()

    def parse_message(self, incomming_message):
        if (incomming_message.body.lower() == "theme"):
            return self.makeResponse(self.getTheme(incomming_message.sentIn),
                                     incomming_message.sentIn)

        if (incomming_message.body.lower().startswith("set theme")):
            return self.makeResponse(
                self.setTheme(incomming_message.body[10:],
                              incomming_message.sentIn),
                incomming_message.sentIn)

        return self.makeResponse(
            "{} said: {}".format(incomming_message.sentBy,
                                 incomming_message.body),
            incomming_message.sentIn)

    def setTheme(self, theme, sentIn):
        self.theme[sentIn] = theme
        return self.theme[sentIn]

    def getTheme(self, sentIn):
        if sentIn in self.theme:
            return self.theme[sentIn]
        else:
            return "No theme set."

    def makeResponse(self, body, sentIn):
        if sentIn is None:
            return message.Message(body)
        else:
            return message.Message(body, "bot", sentIn)
