from mamba import description, context, it, before
from expects import expect, equal
from bot import command_parser

'''
Feature 1:
The bot should be able to parse a message for a command 
to retrieve and set a theme of the day.
'''

with description("Given a CommandParser") as self:
    with context("When a message is 'Theme'"):
        with it("Should return 'No theme set.'"):
            my_command_parser = command_parser.CommandParser()
            expect(
                my_command_parser.parse("Theme")
            ).to(
                equal("No theme set.")
            )

    with context("When a message starts with 'Set theme'"):
        with it("Should store the remainder of the message as the theme"):
            my_command_parser = command_parser.CommandParser()
            expect(
                my_command_parser.parse("Set theme Disney movie songs")
            ).to(
                equal("Disney movie songs")
            )
