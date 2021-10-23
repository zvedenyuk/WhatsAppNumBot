# -*- coding: utf-8 -*-
import sys
import os
import telebot
reload(sys)
sys.setdefaultencoding('utf-8')

appdir = os.path.dirname(__file__)

bot = telebot.TeleBot('XXXXXXXXX:yyyyyYYYyyyyyYYYyyyyYYyyyyyy')

def msg(id,txt,mode="text",parse_mode="Markdown",disable_web_page_preview=False):
	fl=0
	while fl==0:
		try:
			if mode=="text":
				bot.send_message(id,str(txt),parse_mode=parse_mode,disable_web_page_preview=disable_web_page_preview)
			elif mode=="photo":
				bot.send_photo(id,txt)
			elif mode=="video":
				bot.send_video(id,txt)
		except: time.sleep(2)
		else: fl=1

@bot.message_handler(content_types=['text'])
def main(message):
	if message.text.count("/")==0:
		phone=message.text
		phone=phone.replace(" ","").replace("(","").replace(")","").replace("-","")
		if phone.startswith("8"):
			phone=phone[1:]
		if not phone.startswith("+") and not phone.startswith("7"):
			phone="+7"+phone
		msg(message.chat.id,"http://api.whatsapp.com/send?phone="+phone,disable_web_page_preview=True) #reply_to_message_id=message.message_id)

while True:
	bot.polling(none_stop=True,interval=5,timeout=100)