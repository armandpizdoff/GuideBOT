import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['guide'])
def helper(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='Python', callback_data='python')
    button2 = telebot.types.InlineKeyboardButton(text='Ubuntu', callback_data='ubuntu')
    button3 = telebot.types.InlineKeyboardButton(text='GIT', callback_data='git')
    button4 = telebot.types.InlineKeyboardButton(text='Telegram', callback_data='telegram')
    button5 = telebot.types.InlineKeyboardButton(text='Django', callback_data='django')
    button6 = telebot.types.InlineKeyboardButton(text='VIM', callback_data='vim')
    button7 = telebot.types.InlineKeyboardButton(text='PostgreSQL', callback_data='pg')
    button8 = telebot.types.InlineKeyboardButton(text='Nginx', callback_data='nginx')
    markup.row(button1, button2, button3, button7)
    markup.row(button4, button5, button6, button8)
    bot.send_message(message.chat.id,
                     text='<s>Пельменная Виктора Чипотловича</s> Справочная "<b>Старый+</b>". Чем вам помочь?',
                     parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def spravochnik(call):
    if call.data == 'guide':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Python', callback_data='python')
        button2 = telebot.types.InlineKeyboardButton(text='Ubuntu', callback_data='ubuntu')
        button3 = telebot.types.InlineKeyboardButton(text='GIT', callback_data='git')
        button4 = telebot.types.InlineKeyboardButton(text='Telegram', callback_data='telegram')
        button5 = telebot.types.InlineKeyboardButton(text='Django', callback_data='django')
        button6 = telebot.types.InlineKeyboardButton(text='VIM', callback_data='vim')
        button7 = telebot.types.InlineKeyboardButton(text='PostgreSQL', callback_data='pg')
        button8 = telebot.types.InlineKeyboardButton(text='Nginx', callback_data='nginx')
        markup.row(button1, button2, button3, button7)
        markup.row(button4, button5, button6, button8)
        bot.send_message(call.message.chat.id,
                         text='<s>Пельменная Виктора Чипотловича</s> Справочная "<b>Старый+</b>". Чем вам помочь?',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'python':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='*Python:* '
                              '\n\n1) *pip install googletrans==3.1.0a0* - последняя версия google-переводчика '
                              '(она не устанавливается автоматически и не описана в документации google). '
                              '\n2) *pip install python-dotenv* - ПОРА БЫ И ЗАПОМНИТЬ ЭТОТ СРАНЫЙ МОДУЛЬ, БЛЯТЬ. '
                              '\n\n*Виртуальная среда:* '
                              '\n1) *virtualenv myprojectenv* - создать каталог для виртуальной среды. Необходимо '
                              'находиться в папке вашего проекта. Вместо myprojectenv - можно вставить свое название. '
                              '\n2) *source myprojectenv/bin/activate* - активировать виртуальное окружение. '
                              '\n3) *deactivate* - выход из виртуальной среды. ',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'ubuntu':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Пользователи/роли', callback_data='ubuntu1')
        button2 = telebot.types.InlineKeyboardButton(text='Команды и навигация', callback_data='ubuntu2')
        button3 = telebot.types.InlineKeyboardButton(text='Горячие клавиши', callback_data='ubuntu3')
        button4 = telebot.types.InlineKeyboardButton(text='Полезные примечания', callback_data='ubuntu4')
        button5 = telebot.types.InlineKeyboardButton(text='Назад', callback_data='guide')
        markup.row(button1, button2)
        markup.row(button3, button4)
        markup.row(button5)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == 'ubuntu1':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='ubuntu'))
        bot.send_message(call.message.chat.id,
                         text='<b>Работа с пользователями: </b>'
                              '\n1) <b>adduser user</b> - создать нового пользователя. '
                              '\n2) <b>usermod -aG sudo user</b> - наделить его полномочиями. '
                              '\n3) <b>su user</b> - переключение на другого пользователя без перезахода на сервер. '
                              '\n4) <b>chown user:group filename</b> - передать права на файл такому-то пользователю '
                              'такой-то группы пользователей. Чтобы передать права на папку, нужно добавить ключ '
                              'рекурсии после chown - "-R". '
                              '\n5) <b>groups</b> - покажет, в каких группах состоит текущий пользователь. Команда '
                              '<b>groups *user*</b> - возвращает список групп пользователя user. '
                              '\n6) <b>sudo usermod -a -G group user</b> - добавить пользователя в такую-то группу '
                              'пользователей. Заменить *group* на название группы, а *user* - на имя пользователя. ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'ubuntu2':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='ubuntu'))
        bot.send_message(call.message.chat.id,
                         text='<b>Команды навигации и манипуляторы: </b>'
                              '\n1) <b>rm -R /home/user/directory/</b> - рекурсивное удаление указанного каталога '
                              'с содержимым. '
                              '\n2) <b>rmdir /directory/</b> - удаление пустого каталога. '
                              '\n3) <b>df -h</b> - отображение дискового пространства с критерием использования '
                              'памяти. '
                              '\n4) <b>mv * ../</b> - перемещает файлы в текущем каталоге на уровень выше. '
                              '\n5) <b>mv *.* ..</b> - перемещает ВСЕ ФАЙЛЫ в текущем каталоге на уровень выше '
                              '(в т.ч. и скрытые). '
                              '\n6) <b>cp user/file.txt /home/user/directory</b> - '
                              'скопировать файл. схема: cp + что копируем + куда скопировать. '
                              '\n7) <b>cp user/file.txt ./file_super</b> - . - копирует в текущую директорию. После '
                              'слэша - новое название для копии (если оно требуется). '
                              '\n8) <b>cp -r /home/user/directory/</b> - рекурсивное копирование непустого каталога. '
                              '\n9) <b>cat file.txt</b> - открыть текстовый файл. '
                              '\n10) <b>tail -4 file.txt</b> - показать указанное число последних записей в файле. '
                              '\n11) <b>nslookup *адрес*</b> - запрос на ДНС-сервер о резолве того или иного адреса. '
                              'Можно узнать IP ресурса. '
                              '\n12) <b>apt install имя_программы</b> - установка программы. '
                              '\n13) <b>apt remove имя_программы</b> - удаление программы. '
                              '\n14) <b>sudo poweroff</b> - выключить сервер. '
                              '\n15) <b>sudo reboot</b> - перезагрузка сервера. '
                              '\n16) <b>sudo systemctl daemon-reload</b> - перезапуск "Демона". Нужен в том случае, '
                              'если в файл активной службы вносились изменения. ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'ubuntu3':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='ubuntu'))
        bot.send_message(call.message.chat.id,
                         text='<b>Terminal HotKeys: </b>'
                              '\n1) <b>ctrl + L</b> - очистить экран терминала. '
                              '\n2) <b>ctrl + C</b> - прервать операцию. '
                              '\n3) <b>ctrl + ]</b> - выход из консоли телнета. '
                              '\n4) <b>ctrl + D</b> - exit. Возврат в консоль Linux. ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'ubuntu4':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='ubuntu'))
        bot.send_message(call.message.chat.id,
                         text='<b>Полезные примечания: </b>'
                              '\n1) Если папка содержит защищённый от перезаписи контент или какие-то команды выдают '
                              'ошибку доступа - добавьте в начало команды sudo - всегда помогает ;) '
                              '\n2) <b>..</b> - каталог на уровень выше. '
                              '\n3) <b>.</b> - текущий каталог. '
                              '\n4) <b>~</b> - домашний каталог. '
                              '\n5) <b>history</b> - выведет полную историю вводов команд от пользователя. '
                              '\n6) <b>uname</b> - показать ОС. <b>uname -a</b> - точная информация про ОС, версия '
                              'ядра и т.п. '
                              '\n7) <b>cat /proc/cpuinfo</b> - показать информацию о процессоре. '
                              '\n8) <b>cat /proc/meminfo</b> - показать информацию о RAM. '
                              '\n9) <b>free -h</b> - краткая сводка по RAM. '
                              '\n10) <b>top</b> - сводка потребления памяти и CPU. Kind of диспетчер задач. '
                              '\n11) <b>ifconfig</b> - покажет сетевые интерфейсы на сервере. '
                              '\n12) <b>nmap example.com</b> - прога покажет открытые порты у ресурса. Требует '
                              'предварительной установки apt. '
                              '\n13) <b>cat /etc/hostname</b> - показать имя сервера. '
                              '\n14) <b>sudo vim /etc/hostname</b> - открыть файл в vim для замены имени сервера. ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'git':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='*GIT:* '
                              '\n\nСинхронизация *git* с ПК и удалённым репозиторием: '
                              '\n1) *git fetch* --> *git merge* - фетч проверяет изменения в репозитории на GITHUB '
                              'и закачивает их на вашу банку/удалённый сервер. Мердж - применяет/заменяет текущие '
                              'локальные данные на те, что были закачены из репы GITHUB. В вопросе потери лишних '
                              'данных этот способ безопаснее, чем способ ниже. '
                              '\n2) *git pull* - то же самое, что первый способ, но в одно действие. Так сказать, '
                              'форсированное обновление локального репозитория. '
                              '\n3) *git push* - обратное действие к п.1 и п2. - он нужен, если вы произвели '
                              'обновление на вашем ПК/удалённом сервере и хотите залить изменения в репу на GITHUB. '
                              '\n\nСоздание репозитория git-> сервер: '
                              '\n*git clone git@github.com:your-nickname/your-project.git* - подставить свою УЗ и '
                              'название репозитория.',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'telegram':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='*Telegram:* '
                              '\n\n1) *username_to_id_bot* - подставь собаку перед названием. Этот бот позволяет '
                              'узнать свой ID или ID любого чата. Для этого его НЕ ОБЯЗАТЕЛЬНО добавлять в чат. '
                              '\n*PS* Я давно научил нашего Старого тоже это делать, но пусть будет. ',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'django':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='*Django:* '
                              '\n\n1) *./manage.py* - ваш друг и товарищ. Почти любые операции нужно производить, '
                              'находясь в одном каталоге с менеджем. '
                              '\n2) *./manage.py createsuperuser* - создать админку на ресурсе. '
                              '\n3) *./manage.py runserver* - запустить локальный сервер. '
                              '\n4) *./manage.py migrate* - миграция - запись изменений самой структуры таблиц в БД. '
                              '\n5) *./manage.py makemigrations* - подготовить миграцию к заливанию на контур. '
                              '\n6) *./manage.py startapp app1* - создание блока приложений. Вместо app1 подставить '
                              'название вашего будущего приложения. ',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'vim':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='<b>VIM:</b> '
                              '\n\nВнутри редактора все команды начинаются с "<b>:</b>" (двоеточия)! Забудешь '
                              'этот факт - навеки останешься в ловушке Джокера. А если сгоряча закроешь сервер - '
                              'КРИТИЧЕСКАЯ ОШИБКА ПРИ ЗАКРЫТИИ БУДЕТ ПРЕСЛЕДОВАТЬ ТЕБЯ ВЕЧНОСТЬ! '
                              '\nКоманды можно писать одной строкой подряд. Например: <b>:wq</b> '
                              '\n\n<b>vim имя_файла</b> - открыть файл в редакторе. '
                              '\n<b>:q</b> - выход из редактора. '
                              '\n<b>:q!</b> - выход из редактора без сохранения. '
                              '\n<b>a</b> - перейти в режим ввода. Внизу должна появиться надпись INSERT. '
                              '\n<b>ESC</b> - перейти в режим просмотра. '
                              '\n<b>:w</b> - записать изменения. Если документ новый - после "w" написать будущее '
                              'название файла. '
                              '\n<b>yy</b> - Горячая клавиша. Двойное нажатие на "y" копирует выбранную строку. '
                              '\n<b>p</b> - Горячая клавиша. Вставляет скопированную строку. ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'pg':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='<b>PostgreSQL: </b>'
                              '\n\n<b>sudo -u postgres psql</b> - вход в интерактивный интерфейс PG под '
                              'пользователем "Postgres". Он создался вместе с установкой БД. Так принято, так надо. '
                              '\n<b>\q</b> - выход из консоли БД PG. '
                              '\n<b>CREATE DATABASE "myproject";</b> - Создать БД. Убрать кавычки, название '
                              'подставить своё. '
                              '\n<b>DROP DATABASE *Имя базы данных*;</b> - удалить БД. '
                              '\n<b>CREATE USER myprojectuser WITH PASSWORD \'password\';</b> - создать пользователя '
                              'в базе. Логин и пароль вставьте желаемые. '
                              '\n<b>ALTER ROLE myprojectuser SET client_encoding TO \'utf8\';</b> - задать кодирову '
                              'по умолчанию в БД - UTF-8. '
                              '\n<b>ALTER ROLE myprojectuser SET default_transaction_isolation TO \'read committed\''
                              ';</b> - ограничивает чтение со стороны неподтверждённых транзакций. Я хз что это '
                              'пока что 🧐. '
                              '\n<b>ALTER ROLE myprojectuser SET timezone TO \'UTC\'</b>; - установить часовой '
                              'пояс +0 (UTC). Это наверное хороший тон, я хз. '
                              '\n<b>GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;</b> - передать все '
                              'права на администрирование выбранной БД выбранному пользователю. Заменить myproject '
                              'и myprojectuser на свои данные. '
                              '\n\n*Все команды внутри консоли PG должны заканчиваться знаком <b>;</b> '
                              '(точка с запятой) ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'nginx':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='<b>Nginx: </b>'
                              '\n\n<b>sudo nginx -t</b> - проверка конфигурации Nginx на ошибки синтаксиса. '
                              '\n<b>sudo tail -F /var/log/nginx/error.log</b> - лог ошибок nginx. ',
                         parse_mode='HTML', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
