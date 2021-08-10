from message import message
from . import theme_manager, role_manager


class ChatBot(object):
    def __init__(self):
        self.theme_manager = theme_manager.ThemeManager()
        self.role_manager = role_manager.RoleManager()

    def parse_message(self, incomming_message):
        if (incomming_message.body.lower() == "theme"):
            return self.makeResponse(
                self.theme_manager.getTheme(incomming_message.sentIn),
                incomming_message.sentIn)

        if (incomming_message.body.lower().startswith("set theme")):
            if self.role_manager.isAdmin(incomming_message.sentBy):
                return self.makeResponse(
                    self.theme_manager.setTheme(incomming_message.body[10:],
                                            incomming_message.sentIn),
                incomming_message.sentIn)
            else:
                return self.makeResponse("You're not allowed to do that",
                                         incomming_message.sentIn)

        if (incomming_message.body.lower().startswith("make admin")):
            if incomming_message.sentBy == "owner":
                id = incomming_message.body[11:]
                if self.role_manager.isAdmin(id):
                    return self.makeResponse("{} is already an Admin".format(id),
                                         incomming_message.sentIn)   
                else:
                    self.role_manager.setAdmin(id)
                    return self.makeResponse("{} is now an Admin".format(id),
                                         incomming_message.sentIn)
            else:
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
