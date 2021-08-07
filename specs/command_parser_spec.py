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
        with it("should return 'No theme set.'"):
            my_command_parser = command_parser.CommandParser()
            expect(
                my_command_parser.parse("Theme")
            ).to(
                equal("No theme set.")
            )

    with context("When a message starts with 'Set theme'"):
        with it("should store the remainder of the message as the theme"):
            my_command_parser = command_parser.CommandParser()
            expect(
                my_command_parser.parse("Set theme Disney movie songs")
            ).to(
                equal("Disney movie songs")
            )

    with context("When a theme is set"):
        with it("should remember it a moment later"):
            my_command_parser = command_parser.CommandParser()
            my_command_parser.parse("Set theme Disney movie songs")
            expect(
                my_command_parser.parse("Theme")
            ).to(
                equal("Disney movie songs")
            )
