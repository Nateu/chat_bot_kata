# Basic usage

Run unit tests:
* click the _** run **_ button in replit

Or in a shell
* _** mamba --format=documentation specs/*_spec.py **_

Run the bot in the shell tab:
* _** python bot **_

To stop the bot:
* say _** bye ** _ in chat

# Kata - instructions and features
Use the message class to create a message that will be received,
for now only the body property (first arg) needs to be used!

## Feature 1: Theme
The bot should be able to parse a message for a command to retrieve 
and set a theme.

## Feature 2: Case insensitivity
The bot should handle commands ignoring upper/lower case differences.

## Feature 3: Multiple groups
The bot should be context aware, assume it's always in 2 or more groups
with multiple members that chat in the group.  

_** Note: Start using the full Message class from this point forward. **_

Each message will come with a sentBy and a sentIn identifier,
denoting the user that spoke and in which group.  

## Feature 4: Group theme
When a theme is set it should be set only for the context of that group.  

## Feature 5: Let's put in some security
Introduce a role for administrators; these should be the same regardless
of group context. The bot owner is always an administrator and wil always
have the sentBy identifier "_owner_".  

## Feature 6: Administrator only options
Only an Admin set the theme for a group, anyone can retreive it.

## Feature 7: Only the owner can make someone administrator
Only an Admin set the theme for a group, anyone can retreive it.  
