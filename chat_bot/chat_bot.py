from message import Message


class ChatBot:
    def handle_message(self, incomming_message: Message):
        return Message(f"You said: {incomming_message.body}")
