# -*- coding: utf-8 -*-

# Делаем базовые настройки
from chatterbot import ChatBot
# Способ записать, что делает нейросеть (логинрование)
# logging.basicConfig(level=logging.INFO)

# Создаем чатбота
bot=ChatBot(
    "Feedback Bot",
    # Адаптор памяти
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # указываем по какой логике будет работать нейросеть (логический адаптор)
    logic_adapters=['chatterbot.logic.BestMatch'],
    # Адаптер ввода
    input_adapter='chatterbot.input.TerminalAdapter',
    # Адаптер вывода
    output_adapter='chatterbot.output.TerminalAdapter'
)
# Создаем константу
CONVERSATION_ID=bot.storage.create_conversation()
# СОздаем функцию для получения отзыва от пользователя
def get_feedback():
    from chatterbot.utils import input_function

    text = input_function()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Try again: yes or no?')
        return get_feedback()

# Сделаем пользователя инициатором разговора
print('Ask the network something!')

# заставляет работать непрерывно
while True:
    # Защита от дурака, то есть обработка запроса ввода
    try:
        input_statement = bot.input.process_input_statement()

        statement, response = bot.generate_response(input_statement, CONVERSATION_ID)

       # Форматированный вывод
        print('\n Is "{}" a correct response to "{}"? \n'.format(response, input_statement))

        if get_feedback():
            bot.learn_response(response, input_statement)
            bot.storage.add_to_conversation(CONVERSATION_ID, statement)

        # Нейросеть на выходе обработывает свой ответ
        bot.output.process_response(response)

      # Прекращение работы программы, если пользователь вызвал прерываение нажатием комбинаций клавиш на клавиатуре Сtrl+C  или Ctrl+D
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
