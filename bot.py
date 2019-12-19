import telebot
from telebot import types
from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from includes import *
import time

bot = telebot.TeleBot(TOKEN)
act = 1
chapter = 1
quest = 1
lock = False
the_end = False

@bot.message_handler(commands=['start'])
def start_bot(message):
	bot.send_photo(message.chat.id, startmessage[0])
	bot.send_message(message.chat.id, startmessage[1])

	global act
	global chapter
	global quest
	global lock
	global the_end
	while the_end == False:
		if maintext[act][chapter] == 'the end':
			the_end = True
		if maintext[act][chapter] == 'check':
			lock = True
			keyboard = telebot.types.ReplyKeyboardMarkup(True, row_width = 1, one_time_keyboard = True)
			keyboard.row(question[act][0])
			keyboard.row(question[act][1])
			bot.send_message(message.chat.id, '?', reply_markup = keyboard)
			while lock == True:
				@bot.message_handler(func=lambda message: True, content_types=['text'])
				def check_answer(message):
					global act
					global chapter
					global quest
					global lock
					if message.text == question[quest][0]:
						keyboard_hider = types.ReplyKeyboardRemove()
						bot.send_message(message.chat.id, '...', reply_markup = keyboard_hider)
						chapter += 1
						quest += 1
						lock = False
					if message.text == question[quest][1]:
						keyboard_hider = types.ReplyKeyboardRemove()
						bot.send_message(message.chat.id, '...', reply_markup = keyboard_hider)
						act += 1
						chapter = 1
						quest += 1
						lock = False
		else:
			try:
				bot.send_photo(message.chat.id, photos[act][chapter])
			except: pass
			bot.send_message(message.chat.id, maintext[act][chapter])
			chapter += 1

bot.polling()