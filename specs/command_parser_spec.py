from mamba import description, context, it, before
from expects import expect, equal
from bot import command_parser, message

with description("Given a CommandParser") as self:
    with before.each:
        self.command_parser = command_parser.CommandParser()

    with context("when a message is 'Theme'"):
        with it("should return 'No theme set.'"):
            new_message = message.Message("Theme")
            expect(
                self.command_parser.parse(new_message)
            ).to(
                equal("No theme set.")
            )

    with context("when a message starts with 'Set theme'"):
        with it("should store the remainder of the message as the theme"):
            new_message = message.Message("Set theme Disney movie songs")
            expect(
                self.command_parser.parse(new_message)
            ).to(
                equal("Disney movie songs")
            )

    with context("when a theme is set"):
        with it("should remember it a moment later"):
            set_message = message.Message("Set theme Disney movie songs")
            self.command_parser.parse(set_message)
            theme_message = message.Message("Theme")
            expect(
                self.command_parser.parse(theme_message)
            ).to(
                equal("Disney movie songs")
            )

    with context("when a message is 'thEme'"):
        with it("it should ignore case"):
            theme_message = message.Message("thEme")
            expect(
                self.command_parser.parse(theme_message)
            ).to(
                equal("No theme set.")
            )

    with context("when a starts with 'seT tHeme'"):
        with it("it should ignore case"):
            set_message = message.Message("seT tHeme Disney movie songs")
            expect(
                self.command_parser.parse(set_message)
            ).to(
                equal("Disney movie songs")
            )
