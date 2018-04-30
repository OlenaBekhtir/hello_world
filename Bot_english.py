# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Модуль через pip от chatterbot import ChatBot

# Создали новый объект бота
chatbot = ChatBot(
    # Как назовем?
    "Run odinary",
    # Какой тип тренировки нейросети?
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Проведем тренировки на основе английских yml-файлов
chatbot.train("chatterbot.corpus.english")

# Запустим бота: будем писать вопросы и получать ответы
while True:
    print(chatbot.get_response(input('Введите свой вопрос:')))