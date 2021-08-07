'''
Simple script to emulate a bot
'''

import command_parser

def bot():
    commandParser = command_parser.CommandParser()
    exit_loop = False
    print("Hello! I'm a bot")
    while not exit_loop:
        message = str(input())
        parsedMessage = commandParser.parse(message)
        if parsedMessage:
            print(parsedMessage)
        else:
            print("You said: {}".format(message))

if __name__ == '__main__':
    bot()
