class CommandParser(object):
    def __init__(self):
        self.theme = "No theme set."

    def parse(self, message):
        if (message.lower() == "theme"):
            return self.theme

        if (message.lower().startswith("set theme")):
            self.theme = message[10:]
            return message[10:]
