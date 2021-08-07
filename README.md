Setup:

Run unit tests:
* click the __run__ button in replit

Or in a shell
* __mamba --format=documentation specs/*\_spec.py__

Run the bot in the shell tab:
* __python bot__


Use the message class to create a message that will be received,
for now only the body property (first arg) needs to be used!

__Feature 1: Theme__  
The bot should be able to parse a message for a command to retrieve 
and set a theme.

__Feature 2: Case insensitivity __  
The bot should handle commands ignoring upper/lower case differences.

__Feature 3: Multiple groups__  
The bot should be context aware, assume it's always in 2 or more groups
with multiple members that chat in the group.  

__Start using the full Message class from this point forward.__ 

Each message will come with a sentBy and a sentIn identifier,
denoting the user that spoke and in which group.  

__Feature 4: Group theme__  
When a theme is set it should be set only for the context of that group.  

__Feature 5: Let's put in some security__  
Introduce a role for administrators; these should be the same regardless
of group context. The bot owner is always an administrator and wil always
have the sentBy identifier "_owner_".  

__Feature 6: Administrator only options__  
Only an Admin set the theme for a group, anyone can retreive it.

__Feature 6: Only the owner can make someone administrator__  
Only an Admin set the theme for a group, anyone can retreive it.  
