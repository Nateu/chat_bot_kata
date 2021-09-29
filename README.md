# Basic premise
Designed for replit, but should also run locally.
This Kata is meant te help with practising Behavior Driven Development on a unit test level.
Working in Python and with a test runner called Mamba, make a chat bot that uses a simple model for messages and has some basic features (see below).

### Running unit tests:
Click the **run** button in replit

Or locally in the shell
``` bash
$ make
```

### Running the bot in console mode:
```bash
$ python bot.py
```

* To chat simply write a message in the console prompt
* To change user, say **change user <user_name>**
* To change group, say **change group <group_name>**
* To stop the bot, say **bye** in chat

# Kata - instructions and features
Use the message class to create a message that will be received, for now only the body property (first arg) needs to be used!

## Feature 1: Theme
The bot should be able to parse a message for a command to retrieve and set a theme.

## Feature 2: Case insensitivity
The bot should handle commands ignoring upper/lower case differences.

## Stepping up
The bot should be context aware, assume it's always in 2 or more groups with multiple members that chat in the group.
It will respond to the group the message is originating from.

**_Note: Start using the full Message class from this point forward._**

Each message will come with a sentBy and a sentIn identifier, denoting the user that spoke and in which group.  

> Make sure to refactor any code you have so far before you move on.

## Feature 3: Group theme
When a theme is set it should be set only for the context of that group.  

## Let's put in some security
Introduce a role for administrators; these should be the same regardless of group context.
The bot owner is always an administrator and wil always have the sentBy identifier **owner**.  

**_Note: Assume the system will display the sentBy identifier, so it can be used by the owner as a reference._**

## Feature 4: Only the owner can make someone administrator
Only the Owner may make a group member into an Admin.  

## Feature 5: Administrator only options
Only an Admin may set the theme for a group, anyone can retreive it.

## Feature 6: Persistend storage of Admin identifiers and group Themes
Make sure you are able to store the Admin identifiers and group Themes in a persistend way, so when the bot boots up again it has the same data as before.
