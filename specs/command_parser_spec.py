from mamba import description, context, it, before
from expects import expect, equal
from bot import command_parser

with description("Given a CommandParser") as self:
    with before.each:
        self.command_parser = command_parser.CommandParser()

    '''
    Feature 1:
    The bot should be able to parse a message for a command 
    to retrieve and set a theme of the day.
    '''

    with context("when a message is 'Theme'"):
        with it("should return 'No theme set.'"):
            expect(
                self.command_parser.parse("Theme")
            ).to(
                equal("No theme set.")
            )

    with context("when a message starts with 'Set theme'"):
        with it("should store the remainder of the message as the theme"):
            expect(
                self.command_parser.parse("Set theme Disney movie songs")
            ).to(
                equal("Disney movie songs")
            )

    with context("when a theme is set"):
        with it("should remember it a moment later"):
            self.command_parser.parse("Set theme Disney movie songs")
            expect(
                self.command_parser.parse("Theme")
            ).to(
                equal("Disney movie songs")
            )

    '''
    Feature 2:
    The bot should handle commands ignoring upper/lower case differences.
    '''

    with context("when a message is 'thEme'"):
        with it("it should ignore case"):
            expect(
                self.command_parser.parse("thEme")
            ).to(
                equal("No theme set.")
            )
