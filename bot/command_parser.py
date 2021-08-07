class CommandParser(object):
    def __init__(self):
        self.theme = "No theme set."

    def parse(self, message):
        if (message.body.lower() == "theme"):
            return self.theme

        if (message.body.lower().startswith("set theme")):
            self.theme = message.body[10:]
            return message.body[10:]
