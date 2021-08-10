from mamba import description, context, it, before
from expects import expect, equal
from chat_bot import chat_bot
from message import message

with description("Given a ChatBot") as self:
    with before.each:
        self.chat_bot = chat_bot.ChatBot()

    with context("when a member speaks that is not 'owner'"):
        with context("and a message is 'Hi'"):
            with it("should echo the message body prefaced with 'You said: '"):
                expect(
                    self.chat_bot.parse_message(
                        message.Message("Hi", "user", "group A"))).to(
                            equal(
                                message.Message("user said: Hi", "bot",
                                                "group A")))

        with context("and a message is 'Theme'"):
            with it("should return 'No theme set.'"):
                expect(self.chat_bot.parse_message(
                    message.Message("Theme"))).to(
                        equal(message.Message("No theme set.")))

        with context("and a message starts with 'Set theme'"):
            with it("should store the remainder of the message as the theme"):
                expect(
                    self.chat_bot.parse_message(
                        message.Message("Set theme Disney movie songs"))).to(
                            equal(message.Message("Disney movie songs")))

        with context("and a theme is set"):
            with it("should remember it a moment later"):
                self.chat_bot.parse_message(
                    message.Message("Set theme Disney movie songs"))
                expect(self.chat_bot.parse_message(
                    message.Message("Theme"))).to(
                        equal(message.Message("Disney movie songs")))

        with context("and a message is 'thEme'"):
            with it("it should ignore case"):
                expect(self.chat_bot.parse_message(
                    message.Message("thEme"))).to(
                        equal(message.Message("No theme set.")))

        with context("and a starts with 'seT tHeme'"):
            with it("it should ignore case"):
                expect(
                    self.chat_bot.parse_message(
                        message.Message("seT tHeme Disney movie songs"))).to(
                            equal(message.Message("Disney movie songs")))

        with context("and a theme is set in context of Group A"):
            with it("it should be set for Group A"):
                set_theme = message.Message("Set theme Disney movie songs",
                                            "user", "Group A")
                response = message.Message("Disney movie songs", "bot",
                                           "Group A")
                response = self.chat_bot.parse_message(set_theme)
                expect(self.chat_bot.parse_message(set_theme)).to(
                    equal(response))

            with context("and another theme is set in context of Group B"):
                with it("it should track each groups theme"):
                    self.chat_bot.parse_message(
                        message.Message("Set theme Disney movie songs", "user",
                                        "Group A"))
                    self.chat_bot.parse_message(
                        message.Message("Set theme Horror movies", "user",
                                        "Group B"))
                    themeA = message.Message("theme", "user", "Group A")
                    themeB = message.Message("theme", "user", "Group B")
                    response_group_A = self.chat_bot.parse_message(themeA)
                    response_group_B = self.chat_bot.parse_message(themeB)
                    expect(response_group_A.sentIn).to(equal("Group A"))
                    expect(response_group_A.body).to(
                        equal("Disney movie songs"))
                    expect(response_group_B.sentIn).to(equal("Group B"))
                    expect(response_group_B.body).to(equal("Horror movies"))

        with context("and the message is 'Make admin usr_123'"):
            with it("should respond with: 'You're not allowed to do that'"):
                expect(
                    self.chat_bot.parse_message(
                        message.Message(
                            "Make admin usr_123", "random_user",
                            "Group A"))).to(
                                equal(
                                    message.Message(
                                        "You're not allowed to do that", "bot",
                                        "Group A")))

    with context("when a member speaks that is 'owner'"):
        with context("and the message is 'Make admin usr_123'"):
            with it("should respond with: 'usr_123 is now an Admin'"):
                expect(
                    self.chat_bot.parse_message(
                        message.Message("Make admin usr_123", "owner",
                                        "Group A"))).to(
                                            equal(
                                                message.Message(
                                                    "usr_123 is now an Admin",
                                                    "bot", "Group A")))

        with context("and usr_123 is an admin"):
            with context("and the message is 'Make admin usr_123' is said in another group"):
                with it("should state: 'usr_123 is already an Admin"):
                    self.chat_bot.parse_message(
                            message.Message("Make admin usr_123", "owner",
                                            "Group A"))
                    expect(self.chat_bot.parse_message(
                            message.Message("Make admin usr_123", "owner",
                                            "Group B"))
                        ).to(
                                                equal(
                                                    message.Message(
                                                        "usr_123 is already an Admin",
                                                        "bot", "Group B")))

# def log(m):
#     print("Group: {} Sender: {} Body: {}".format(m.sentIn, m.sentBy, m.body))
