import telebot
import random
random.seed()

API_TOKEN = ''  # TODO: Вставьте сюда API_TOKEN вашего бота

START_STICKER = 'CAACAgIAAxkBAAEDAAE6YVgzq4Jb5NibZisRshiQnAl01TMAAocCAAJWnb0KQu10K0BX0JAhBA'  # @Stiker_id_bot поможет
WIN_STICKER = 'CAACAgIAAxkBAAEDAAE9YVgzvRi4Ej8ZNzxQnx2xqK0-Y6QAAooCAAJWnb0KPlJuixPFQGchBA'
BAD_STICKER = 'CAACAgIAAxkBAAEDAAE1YVgzgtRTh16cvcMIxKSSJjOWcU0AAiQLAAIEv_FLFuD22fNmUL0hBA'
WAIT_STICKER = 'CAACAgIAAxkBAAEDU4dhmMg7t8g7pvSYosWeZR571OBUBAACMgADmWuhLT0uAyXSw_MmIgQ'

RIGHT_ANSWER = 1

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, START_STICKER)
    bot.send_message(message.from_user.id, """Здравствуйте! Это игра по мотивам доски Гальтона.
Правила этой игры просты.
1. Вы вводите команду '/launching'.
2. В ответном сообщении вам будет отправлено число шариков.
3. Всего у нас есть 2 ряда штырьков.
Расположены они так: 
 1
2 2
А также у нас есть 3 стакана, в которые шарики падают.
Вы должны угадать сколько будет шариков в каждом стакане)
4. По очереди вводите количество шариков в каждом стакане. Прошу вводить в разных строках.
5. Ждите отработки модели
6. Вам будет отправлен результат.
*Правильне ответы*
*Ваши ставки*
*Разница в процентах*
Удачи""")
count = random.randint(1, 10000)

@bot.message_handler(commands=['launching'])
def start_message(message):
    bot.send_message(message.from_user.id, "Количество шариков " + str(count))
    bot.send_sticker(message.chat.id, WAIT_STICKER)

@bot.message_handler(content_types=['text'])
def start(message):
    try:
        a = int(message.text)
        b = int(message.text)
        c = int(message.text)
        a1 = count / 4
        c1 = a1
        b1 = count / 4 * 2
        a1 = int(a1 + (0.5 if a1 > 0 else -0.5))
        b1 = int(b1 + (0.5 if b1 > 0 else -0.5))
        c1 = int(c1 + (0.5 if c1 > 0 else -0.5))
        bot.send_message(message.from_user.id, "Правильные ответы: " + str(a1) + ", " + str(b1) + ", " + str(c1))
        bot.send_message(message.from_user.id, "Ваши ставки: " + str(a) + ", " + str(b) + ", " + str(c))
        bot.send_message(message.from_user.id, "Процент ваших ставок от правильных ответов: " + str(a/(a1/100)) + ", " + str(b/(b1/100)) + ", " + str(c/(c1/100)))
        if(abs(100 - a/(a1/100)) < 20 and abs(100 - b/(b1/100)) < 20 and abs(100 - c/(c1/100)) < 20):
            bot.send_sticker(message.chat.id, WIN_STICKER)
            bot.send_message(message.from_user.id, "Вы молодец!")
        else:
            bot.send_sticker(message.chat.id, BAD_STICKER)
            bot.send_message(message.from_user.id, "В этот раз не получилось... Но в следующий раз вам точно повезет!")
    except ValueError:
        bot.send_sticker(message.chat.id, WAIT_STICKER)
        bot.send_message(message.from_user.id, "Я жду адекватности...")


@bot.message_handler(content_types=['voice'])
def start_message(message):
    bot.send_message(message.from_user.id, "Не слышуууу. Ничего не слышу. Глуховат я :(")


@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_message(message.from_user.id, "Симпатичный стикер - сохраню себе.")


@bot.message_handler(content_types=['document'])
def start_message(message):
    bot.send_message(message.from_user.id, "Ой, вот только файлы мне тут не надо слать!")

bot.polling()