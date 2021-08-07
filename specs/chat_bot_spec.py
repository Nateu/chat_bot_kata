from mamba import description, context, it, before
from expects import expect, equal
from bot import chat_bot, message

with description("Given a ChatBot") as self:
    with before.each:
        self.chat_bot = chat_bot.ChatBot()

    with context("when a message is 'Theme'"):
        with it("should return 'No theme set.'"):
            theme_message = message.Message("Theme")
            expect(
                self.chat_bot.parse_message(theme_message)
            ).to(
                equal("No theme set.")
            )

    with context("when a message starts with 'Set theme'"):
        with it("should store the remainder of the message as the theme"):
            set_theme_message = message.Message("Set theme Disney movie songs")
            expect(
                self.chat_bot.parse_message(set_theme_message)
            ).to(
                equal("Disney movie songs")
            )

    with context("when a theme is set"):
        with it("should remember it a moment later"):
            set_theme_message = message.Message("Set theme Disney movie songs")
            self.chat_bot.parse_message(set_theme_message)
            theme_message = message.Message("Theme")
            expect(
                self.chat_bot.parse_message(theme_message)
            ).to(
                equal("Disney movie songs")
            )

    with context("when a message is 'thEme'"):
        with it("it should ignore case"):
            theme_message = message.Message("thEme")
            expect(
                self.chat_bot.parse_message(theme_message)
            ).to(
                equal("No theme set.")
            )

    with context("when a starts with 'seT tHeme'"):
        with it("it should ignore case"):
            set_theme_message = message.Message("seT tHeme Disney movie songs")
            expect(
                self.chat_bot.parse_message(set_theme_message)
            ).to(
                equal("Disney movie songs")
            )
