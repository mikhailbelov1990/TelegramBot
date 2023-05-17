import telebot
bot = telebot.TeleBot('6273827092:AAG3ALU314-8-999cC0Ytjd84SOeleFn2nc')

name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == 'да':
        bot.send_message(message.from_user.id, "Молодец! Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    elif message.text.lower() == 'нет':
        bot.send_message(message.from_user.id, "ЛОХ!");
    else:
        bot.send_message(message.from_user.id, 'Привет! Ты ходишь на кружок по программированию? (да/нет)');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    print(name);
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    print(surname);
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
        str1 = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+' и ты ходишь на кружок по программированию!';
        print(str1)
        bot.send_message(message.from_user.id, str1)

bot.polling(none_stop=True, interval=0)
