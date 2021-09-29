'''
Simple script to emulate a chat room
'''
from message import Message
from chat_bot import ChatBot

class Colors:
    GREY      = '\033[90m'
    RED       = '\033[91m'
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    BLUE      = '\033[94m'
    MAGENTA   = '\033[95m'
    CYAN      = '\033[96m'
    WHITE     = '\033[97m'
    Default   = '\033[99m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

def respond (text):
    print(Colors.MAGENTA + f"🤖 {text}" + Colors.ENDC)

def checkMessage(text):
    return text == "bye" or text.startswith("change user") or text.startswith("change group")

def bot():
    chatBot = ChatBot()
    exit_loop = False
    group = "group A"
    user = "owner"

    respond("Hello! I'm a bot")
    while not exit_loop:
        console_input = str(input(Colors.CYAN + f"{user} @ [{group}] : " + Colors.ENDC))
        checkString = console_input.casefold()
        if checkMessage(checkString):
            if checkString == "bye":
                respond("Bye Bye!")
                exit_loop = True
            elif checkString.startswith("change user"):
                user = console_input[12:]
                respond(f"You're now known as {user}")
            elif checkString.startswith("change group"):
                group = console_input[13:]
                respond(f"You're now in group {group}")
        else:
            parsedMessageResponse = chatBot.handle_message(Message(console_input, user, group))
            respond(parsedMessageResponse.body)

if __name__ == '__main__':
    bot()
