class CommandParser(object):

    def parse(self, message):
        if (message == "Theme"):
            return "No theme set."
        if (message.startswith("Set theme")):
            return message[10:]
