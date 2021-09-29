from mamba import description, context, it, before
from expects import expect, equal
from chat_bot import ChatBot
from message import Message

with description("Given a chat room with a ChatBot") as self:
    with before.each:
        self.chat_bot = ChatBot()

    with context("when someone in the chat room says 'Hi'"):
        with it("should echo the message body prefaced with 'You said: '"):
            expect(self.chat_bot.handle_message(Message("Hi"))).to(
                equal(Message("You said: Hi")))
