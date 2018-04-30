# -*- coding: utf-8 -*-

from chatterbot import ChatBot

from random import randint
from time import sleep

response_bot = ChatBot(
    'Charlie',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        {'import_path' : 'chatterbot.logic.BestMatch'},
        # Адаптор слабой уверенности
        {'import_path' : 'chatterbot.logic.LowConfidenceAdapter',
         'treshold' : 0.1,
         'default_response' : 'Извините, я не знаю ответа.'
         }
    ],

    trainer = 'chatterbot.trainers.ListTrainer'
)

response_bot.train(
    [
        'Как я могу вам помочь?',
        'Я хочу есть',
        'Ты смотрел меню?',
        'Нет, не смотрел',
        'Ознакомься с меню: mafia.ua',
        'Спасибо! Это лучшая пиццерия в городе'
    ]
)

while True:
    try:
        question = input('Спроси у меня что-нибудь: ')
        response = response_bot.get_response(question)
        sleep(randint(1, 5))
        print(response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break