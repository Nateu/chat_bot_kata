'''
Simple script to emulate a bot
'''
import command_parser
import message

def bot():
    commandParser = command_parser.CommandParser()
    exit_loop = False
    print("Hello! I'm a bot")
    while not exit_loop:
        console_input = str(input())
        new_message = message.Message(console_input, "owner", "group A")
        parsedMessageResponse = commandParser.parse(new_message)
        if parsedMessageResponse:
            print(parsedMessageResponse)
        else:
            print("You said: {}".format(console_input))

if __name__ == '__main__':
    bot()
