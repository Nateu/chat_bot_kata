'''
Simple script to emulate a bot
'''

def bot():
    exit_loop = False
    print("Hello! I'm a bot")
    while not exit_loop:
        message = str(input())
        print("You said: {}".format(message))

if __name__ == '__main__':
    bot()
