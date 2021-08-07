'''
Simple script to emulate a bot
'''
import chat_bot
import message

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

def bot():
    chatBot = chat_bot.ChatBot()
    exit_loop = False
    print(bcolors.OKGREEN + "Botty: Hello! I'm a bot" + bcolors.ENDC)
    while not exit_loop:
        console_input = str(input())
        if console_input.lower() == "bye":
            print(bcolors.OKGREEN + "Bye Bye!" + bcolors.ENDC)
            exit_loop = True
        else:
            new_message = message.Message(console_input, "owner", "group A")
            parsedMessageResponse = chatBot.parse_message(new_message)
            if parsedMessageResponse:
                print(bcolors.OKGREEN + "Botty: {}".format(parsedMessageResponse) + bcolors.ENDC)
            else:
                print(bcolors.OKGREEN + "Botty: You said {}".format(new_message.body)+ bcolors.ENDC)

if __name__ == '__main__':
    bot()
