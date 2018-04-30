# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Charlie',
    trainer='chatterbot.trainers.ListTrainer'
)

chatbot.train(
    [
        "Hello. How are you?",
        "I really like the new album of Shinedown",
        "I have already booked a ticket to Ireland",
        "Yep, I have visited MWC this year"
    ]
)

while True:
    print(
        chatbot.get_response(
            input("What do you want to ask: ")
        )
    )