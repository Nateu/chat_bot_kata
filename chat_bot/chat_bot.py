from message import message
from . import theme_manager


class ChatBot(object):
    def __init__(self):
        self.theme_manager = theme_manager.ThemeManager()

    def parse_message(self, incomming_message):
        if (incomming_message.body.lower() == "theme"):
            return self.makeResponse(
                self.theme_manager.getTheme(incomming_message.sentIn),
                incomming_message.sentIn)

        if (incomming_message.body.lower().startswith("set theme")):
            return self.makeResponse(
                self.theme_manager.setTheme(incomming_message.body[10:],
                                            incomming_message.sentIn),
                incomming_message.sentIn)

        if (incomming_message.body.lower().startswith("make admin")):
            if incomming_message.sentBy != "owner":
                return self.makeResponse("You're not allowed to do that",
                                         incomming_message.sentIn)

        return self.makeResponse(
            "{} said: {}".format(incomming_message.sentBy,
                                 incomming_message.body),
            incomming_message.sentIn)

    def makeResponse(self, body, sentIn):
        if sentIn is None:
            return message.Message(body)
        else:
            return message.Message(body, "bot", sentIn)
