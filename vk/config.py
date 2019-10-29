import sys

module = sys.modules[__name__]

def setCell( name, value ):
	module.table[name] = value

def getCell( name ):
	return module.table.get( name )

def initConfig():
	module.table = {}


	#############################################################
	########                                             ########
	########           Основные настройки бота           ########
	########                                             ########
	#############################################################

	setCell( "vk_msgForPick", 1 ) # Сколько сообщений за раз обрабатывать? Просто не трогай...

	setCell( "vk_AddFriends", False ) # Автоматически добавлять новых пользователей в друзья?

	setCell( "vk_login", "78005553535" ) # Логин от аккаунта ВК
	setCell( "vk_password", "Password" ) # Пароль от аккаунта ВК

	setCell( "telegram_token", "12345678:ABcDeFgHeVzS-6543-dWEdGAJ1234" ) # Токен ботинка в Telegram

	setCell( "telegram_SendName", False ) # Отправлять в ВК текст с именем отправителя из Telegram

	#############################################################
	########                                             ########
	########      Настройки стикеров Telegram--> VK      ########
	########                                             ########
	#############################################################


	setCell( "vk_EnableStickers", True ) # Включить отправку стикеров из Telegram в ВК?

	setCell( "vk_album_id", 254179516 ) # ID альбома, куда будут заливаться стикеры из тележки
	setCell( "vk_detelestickers", True ) # Удалять загруженные стикеры с компьютера?
	# После загрузки в ВК они ни на что не влияют, так что при желании можно оставить
	# Они будут скапливаться в папке 'stickers'
	setCell( "vk_sticker_EnableScale", True ) # Включить уменьшение стикера в ВК?
	# Можно и не включать, но тогда стикер будет просто огромный
	setCell( "vk_sticker_size", 200 ) # Развер стикера в ВК.
	# Можно поэксперементировать с размерами, но 200 мне показался самым удачным
	# P.S. Не забываем про то, что размер у залитых ранее стикеров не изменится!

	#############################################################
	########                                             ########
	########                   Прокси                    ########
	########         (Если не нужно - пропускаем)        ########
	########                                             ########
	#############################################################

	setCell( "telegram_useProxy", True ) # Использовать прокси для телеграма?

	setCell( "p_type", "socks5") # Протокол прокси-сервера
	# P.S. Для работы socks необходимо установить их поддержку:
	# pip3 install -U requests[socks]
	
	setCell( "p_host", "u0k12.tgproxy.me" ) # Адрес
	setCell( "p_port", "1080" ) # Порт
	setCell( "p_user", "" ) # Имя пользователя. Если не нужно - оставить пустым
	setCell( "p_password", "" ) # Пароль. Если не нужно - оставить пустым

	#############################################################
	########                                             ########
	########     Настройка тоннелей ВК <--> Telegram     ########
	########                                             ########
	#############################################################

	setCell( "vk_417110104", '-236472090' ) # Пример переадресации ЛС ВК в Telegram
	setCell( "t_-236472090", '417110104' ) # Пример переадресации ЛС ВК в Telegram

	setCell( "vk_1", '-249416176' ) # Пример переадресации из чата ВК в Telegram
	setCell( "t_-249416176", '1' ) # Пример переадресации из чата ВК в Telegram
	# P.S. В нашем случае 1 - 'локальный' ID чата для аккаунта ВК
	
	# P.S.S. Не забываем изменить/удалить примеры, а то может что-то пойти не так...

	#setCell( "vk_", '-' ) # Шаблон
	#setCell( "t_-", '' ) # Шаблон