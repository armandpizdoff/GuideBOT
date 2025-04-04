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
    button9 = telebot.types.InlineKeyboardButton(text='HTML', callback_data='html')
    button10 = telebot.types.InlineKeyboardButton(text='Projects', callback_data='projects')
    markup.row(button1, button2, button3, button7)
    markup.row(button4, button5, button6, button8)
    markup.row(button9, button10)
    bot.send_message(message.chat.id,
                     text='<s>Пельменная Виктора Чипотловича</s> Справочная "<b>Буйвол+</b>". Чем вам помочь?',
                     parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def spravochnik(call):
    bot.answer_callback_query(call.id)
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
        button9 = telebot.types.InlineKeyboardButton(text='HTML', callback_data='html')
        button10 = telebot.types.InlineKeyboardButton(text='Projects', callback_data='projects')
        markup.row(button1, button2, button3, button7)
        markup.row(button4, button5, button6, button8)
        markup.row(button9, button10)
        bot.send_message(call.message.chat.id,
                         text='<s>Пельменная Виктора Чипотловича</s> Справочная "<b>Буйвол+</b>". Чем вам помочь?',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'python':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='*Python:* '
                              '\n\n1) *python.exe -m pip install --upgrade pip* - обновить python '
                              '\n2) *pip install googletrans==3.1.0a0* - последняя версия google-переводчика '
                              '(она не устанавливается автоматически и не описана в документации google). '
                              '\n3) *pip install python-dotenv* - ПОРА БЫ И ЗАПОМНИТЬ ЭТОТ СРАНЫЙ МОДУЛЬ, БЛЯТЬ. '
                              '\n4) *pip install pyTelegramBotAPI* - установить библиотеку для Telegram '
                              '\n\n*Виртуальная среда:* '
                              '\n1) *virtualenv myprojectenv* - создать каталог для виртуальной среды. Необходимо '
                              'находиться в папке вашего проекта. Вместо myprojectenv - можно вставить свое название. '
                              '\n2) *source myprojectenv/bin/activate* - активировать виртуальное окружение. '
                              '\n3) *deactivate* - выход из виртуальной среды. '
                              '\n4) *pip freeze > requirements.txt* - сохраняем зависимости проекта в список пакетов. '
                              '\n5) *pip install -r requirements.txt* - установить требуемые пакеты одной командой. ',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'ubuntu':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Пользователи/роли', callback_data='ubuntu1')
        button2 = telebot.types.InlineKeyboardButton(text='Команды и навигация', callback_data='ubuntu2')
        button3 = telebot.types.InlineKeyboardButton(text='Горячие клавиши', callback_data='ubuntu3')
        button4 = telebot.types.InlineKeyboardButton(text='Полезные примечания', callback_data='ubuntu4')
        button5 = telebot.types.InlineKeyboardButton(text='Сетевая безопасность', callback_data='ubuntu5')
        button6 = telebot.types.InlineKeyboardButton(text='Назад', callback_data='guide')
        markup.row(button1, button2)
        markup.row(button3, button4)
        markup.row(button5, button6)
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
                              '\n<b>rm -R /home/user/directory/</b> - рекурсивное удаление указанного каталога '
                              'с содержимым. '
                              '\n<b>rmdir /directory/</b> - удаление пустого каталога. '
                              '\n<b>df -h</b> - отображение дискового пространства с критерием использования '
                              'памяти. '
                              '\n<b>mv * ../</b> - перемещает файлы в текущем каталоге на уровень выше. '
                              '\n<b>mv *.* ..</b> - перемещает ВСЕ ФАЙЛЫ в текущем каталоге на уровень выше '
                              '(в т.ч. и скрытые). '
                              '\n<b>mv oldname NewName</b> - переименовать папку/файл с сохранением прав и владельца. '
                              '\n<b>cp user/file.txt /home/user/directory</b> - '
                              'скопировать файл. схема: cp + что копируем + куда скопировать. '
                              '\n<b>cp user/file.txt ./file_super</b> - . - копирует в текущую директорию. После '
                              'слэша - новое название для копии (если оно требуется). '
                              '\n<b>cp -r /home/user/directory/</b> - рекурсивное копирование непустого каталога. '
                              '\n<b>cat file.txt</b> - открыть текстовый файл. '
                              '\n<b>tail -4 file.txt</b> - показать указанное число последних записей в файле. '
                              '\n<b>nslookup *адрес*</b> - запрос на ДНС-сервер о резолве того или иного адреса. '
                              'Можно узнать IP ресурса. '
                              '\n<b>apt-get update</b> - обновляет информацию о пакетах в репозиториях Ubuntu. '
                              '\n<b>apt update</b> - обновить локальный кеш пакетов (составление списка обновлений). '
                              '\n<b>apt upgrade</b> - установить новые пакеты. '
                              '\n<b>apt install имя_программы</b> - установка программы. '
                              '\n<b>apt remove имя_программы</b> - удаление программы. '
                              '\n<b>sudo poweroff</b> - выключить сервер. '
                              '\n<b>sudo reboot</b> - перезагрузка сервера. '
                              '\n<b>sudo systemctl daemon-reload</b> - перезапуск "Демона". Нужен в том случае, '
                              'если в файл активной службы вносились изменения. ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'ubuntu3':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='ubuntu'))
        bot.send_message(call.message.chat.id,
                         text='<b>Terminal HotKeys: </b>'
                              '\n<b>ctrl + L</b> - очистить экран терминала. '
                              '\n<b>ctrl + C</b> - прервать операцию. '
                              '\n<b>ctrl + ]</b> - выход из консоли телнета. '
                              '\n<b>ctrl + D</b> - exit. Возврат в консоль Linux. ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'ubuntu4':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='ubuntu'))
        bot.send_message(call.message.chat.id,
                         text='<b>Полезные примечания: </b>'
                              '\nЕсли папка содержит защищённый от перезаписи контент или какие-то команды выдают '
                              'ошибку доступа - добавьте в начало команды sudo - всегда помогает ;) '
                              '\n<b>..</b> - каталог на уровень выше. '
                              '\n<b>.</b> - текущий каталог. '
                              '\n<b>~</b> - домашний каталог. '
                              '\n<b>pip3 install --upgrade setuptools pip</b> - обновить установщик пакетов. '
                              '\n<b>history</b> - выведет полную историю вводов команд от пользователя. '
                              '\n<b>uname</b> - показать ОС. <b>uname -a</b> - точная информация про ОС, версия '
                              'ядра и т.п. '
                              '\n<b>cat /proc/cpuinfo</b> - показать информацию о процессоре. '
                              '\n<b>cat /proc/meminfo</b> - показать информацию о RAM. '
                              '\n<b>free -h</b> - краткая сводка по RAM. '
                              '\n<b>top</b> - сводка потребления памяти и CPU. Kind of диспетчер задач. '
                              '\n<b>ps axu</b> - открытые приложения на сервере. '
                              '\n<b>cat /etc/hostname</b> - показать имя сервера. '
                              '\n<b>sudo vim /etc/hostname</b> - открыть файл в vim для замены имени сервера. '
                              '\n<b>lsb_release -a</b> - выводит информацию о дистрибутиве Ubuntu, включая его '
                              'версию. ', parse_mode='HTML', reply_markup=markup)
    elif call.data == 'ubuntu5':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='ubuntu'))
        bot.send_message(call.message.chat.id,
                         text='<b>Сетевая безопасность: </b> '
                              '\n<b>ifconfig</b> - покажет сетевые интерфейсы на сервере. '
                              '\n<b>nmap example.com</b> - прога покажет открытые порты у ресурса. Требует '
                              'предварительной установки apt. '
                              '\n<b>sudo ufw enable</b> - включить МСЭ/межсетевой экран/брандмауэр. '
                              '\n<b>sudo ufw allow SSH</b> - добавить приложение в список МСЭ. '
                              '\n<b>sudo ufw app list</b> - список приложений, зарегистрированных в МСЭ. '
                              '\n<b>sudo ufw allow 80</b> - разрешить подключения по указанному порту. '
                              '\n<b>sudo ufw status numbered</b> - показать сетевые правила сервера (с нумерацией). '
                              '\n<b>sudo ufw status</b> - показать сетевые правила сервера (без нумерации). '
                              '\n<b>sudo ufw delete 3</b> - удалить правило под указанным номером. '
                              '\n<b>sudo ufw delete allow 443/tcp</b> - так же удаляет правило, без указания номера. '
                              '\n<b>sudo ufw disable</b> - выключить МСЭ/межсетевой экран/брандмауэр. ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'git':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='*GIT:* '
                              '\n\nСоздание репозитория git-> сервер: '
                              '\n*git clone git@github.com:your-nickname/your-project.git* - подставить свою УЗ и '
                              'название репозитория.'
                              '\n\nСинхронизация *git* с ПК и удалённым репозиторием: '
                              '\n1) *git fetch* --> *git merge* - фетч проверяет изменения в репозитории на GITHUB '
                              'и закачивает их на вашу банку/удалённый сервер. Мердж - применяет/заменяет текущие '
                              'локальные данные на те, что были закачены из репы GITHUB. В вопросе потери лишних '
                              'данных этот способ безопаснее, чем способ ниже. '
                              '\n2) *git pull* - то же самое, что первый способ, но в одно действие. Так сказать, '
                              'форсированное обновление локального репозитория. '
                              '\n3) *git status* - проверить статус репозитория. Здесь видно, если какая-то '
                              'директория/файлы не входят в репу (список "Untracked files"). '
                              '\n4) *git init* - создание репозитория на вашей ВМ (например для последующей отправки '
                              'на сервер GIT'
                              '\n5) *git add название_директории* - добавить новую директорию в индекс вашего Git. '
                              '\n6) *git commit -m "описание"* - подготовить изменения для заливки в репозиторий. '
                              '\n7) *git push* - обратное действие к п.1 и п2. - он нужен, если вы произвели '
                              'обновление на вашем ПК/удалённом сервере и хотите залить изменения в репу на GITHUB. ',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'telegram':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='*Telegram:* '
                              '\n\n1) *username_to_id_bot* - подставь собаку перед названием. Этот бот позволяет '
                              'узнать свой ID или ID любого чата. Для этого его НЕ ОБЯЗАТЕЛЬНО добавлять в чат. '
                              '\n*PS* Я давно научил нашего Старого тоже это делать, но пусть будет. '
                              '\n2)*pip install pyTelegramBotAPI* - установить py-библиотеку для Telegram ',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'django':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='*Django:* '
                              '\n\n*./manage.py* - ваш друг и товарищ. Почти любые операции нужно производить, '
                              'находясь в одном каталоге с менеджем. '
                              '\n*./manage.py createsuperuser* - создать админку на ресурсе. '
                              '\n*./manage.py runserver* - запустить локальный сервер. '
                              '\n*./manage.py migrate* - миграция - запись изменений самой структуры таблиц в БД. '
                              '\n*./manage.py makemigrations* - подготовить миграцию к заливанию на контур. '
                              '\n*./manage.py startapp app1* - создание блока приложений. Вместо app1 подставить '
                              'название вашего будущего приложения. '
                              '\n*django-admin.py* - это манипулятор для windows. А вот для mac и linux - '
                              '*django-admin*',
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
                              '\n<b>\c db_name usr_name</b> - подключиться к такой-то базе под таким-то пользователем. '
                              '\n<b>\q</b> - выход из консоли БД PG. '
                              '\n<b>CREATE DATABASE "myproject";</b> - Создать БД. Убрать кавычки, название '
                              'подставить своё. '
                              '\n<b>DROP DATABASE *Имя базы данных*;</b> - удалить БД. '
                              '\n<b>CREATE USER myprojectuser WITH PASSWORD \'password\';</b> - создать пользователя '
                              'в базе. Логин и пароль вставьте желаемые. '
                              '\n<b>ALTER ROLE myprojectuser SET client_encoding TO \'utf8\';</b> - задать кодировку '
                              'по умолчанию в БД - UTF-8. '
                              '\n<b>ALTER ROLE myprojectuser SET default_transaction_isolation TO \'read committed\''
                              ';</b> - ограничивает чтение со стороны неподтверждённых транзакций. Я хз что это '
                              'пока что 🧐. '
                              '\n<b>ALTER ROLE myprojectuser SET timezone TO \'UTC\'</b>; - установить часовой '
                              'пояс +0 (UTC). Это наверное хороший тон, я хз. '
                              '\n<b>GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;</b> - передать все '
                              'права на администрирование выбранной БД выбранному пользователю. Заменить myproject '
                              'и myprojectuser на свои данные. '
                              '\n <b>sudo netstat -pant | grep postgres</b> - проверить статус СУБД. '
                              '\n<b>sudo netstat -pant | grep postgres</b> - проверить статус СУБД. '
                              '\n<b>select * from pg_hba_file_rules;</b> - просмотреть правила настроек подключения '
                              '(в терминале). '
                              '\n<b>select * from pg_catalog.pg_user;</b> - просмотреть список пользователей БД. '
                              '<i>Позволяет выполнять запросы к базе данных из любого клиента или среды '
                              'программирования, поддерживающих PostgreSQL.</i>'
                              '\n<b>\du</b> - Просмотреть список пользователей БД - тоже самое, только в виде '
                              'bash-запроса. <i>Его можно использовать только в оболочке psql.</i> '
                              '\n<b>Postgres exporter</b> — сбор метрик работы сервера PostgreSQL. Порт для доступа по '
                              'умолчанию — <b>9187</b>; '
                              '\n<b>sudo service postgresql restart</b> - перезапуск БД. '
                              '\n\n*Все команды внутри консоли PG должны заканчиваться знаком <b>;</b> '
                              '(точка с запятой) ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'nginx':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='<b>Nginx: </b>'
                              '\n\n<b>sudo nginx -t</b> - проверка конфигурации Nginx на ошибки синтаксиса. '
                              '\n<b>sudo tail -F /var/log/nginx/error.log</b> - лог ошибок nginx. '
                              '\n<b>sudo systemctl restart nginx</b> - перезапуск службы. Может пригодится при '
                              'изменении конфигурации серверного блока Nginx. ',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'html':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='guide'))
        bot.send_message(call.message.chat.id,
                         text='<b>HTML: </b>'
                              '\n\n*<br>* - перенос строк в цикле. '
                              '\n*<li>* - элемент списка. Входит в <ol>, <ul> и <menu>. ',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'projects':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Алгоритм создания проектов', callback_data='algorithm')
        button2 = telebot.types.InlineKeyboardButton(text='Назад', callback_data='guide')
        markup.row(button1)
        markup.row(button2)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == 'algorithm':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Назад', callback_data='projects')
        markup.row(button1)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, text='Для начала стоит помнить, что проще всего создавать репозиторий '
                                                    'в GIT, а же потом загружать его на ПК/ВМ (см. раздел GIT). '
                                                    'Далее следует настроить файл .gitignore (раскомментировать или '
                                                    'добавить в конец *.idea/*.)'
                                                    '\nНа ПК и ВМ должны быть развёрнуты виртуальные окружения для '
                                                    'проектов: на ВМ будет боевой режим, а на ПК оно требуется для '
                                                    'тестов. Они должны быть идентичны, но добавлять модули и '
                                                    'библиотеки требуется и туда, и туда.',
                         parse_mode='markdown', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
