'''
Simple script to emulate a bot
'''
from message import message
from bot import chat_bot

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def respond (text):
    print(bcolors.OKGREEN + "🤖 {}".format(text) + bcolors.ENDC)

def checkMessage(text):
    return text == "bye" or text.startswith("change user") or text.startswith("change group")

def bot():
    chatBot = chat_bot.ChatBot()
    exit_loop = False
    group = "group A"
    user = "owner"

    respond("Hello! I'm a bot")
    while not exit_loop:
        console_input = str(input())
        checkString = console_input.lower()
        if checkMessage(checkString):
            if checkString == "bye":
                respond("Bye Bye!")
                exit_loop = True
            elif checkString.startswith("change user"):
                user = console_input[12:]
                respond("You're now known as {}".format(user))
            elif checkString.startswith("change group"):
                group = console_input[13:]
                respond("You're now in group {}".format(group))
        else:
            new_message = message.Message(console_input, user, group)
            parsedMessageResponse = chatBot.parse_message(new_message)
            respond(parsedMessageResponse.body)

if __name__ == '__main__':
    bot()
