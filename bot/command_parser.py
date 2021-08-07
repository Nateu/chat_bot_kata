class CommandParser(object):
    def __init__(self):
        self.theme = "No theme set."

    def parse(self, message):
        if (message == "Theme"):
            return self.theme

        if (message.startswith("Set theme")):
            self.theme = message[10:]
            return message[10:]
