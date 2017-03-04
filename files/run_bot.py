#!/usr/bin/env python3

import telebot
import re
import os
import random
import sys

api_key = str(sys.argv[1])

def get_bayn_image(path):
    images = []
    for  (dirpath, dirnames, filenames) in os.walk(path + "/images"):
      for i in filenames:
        print("")
        a = open(path + "/images/" + i, "rb")
        images.append(a)
    return random.choice(images)    

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    bot = telebot.TeleBot(api_key)
    @bot.message_handler(regexp='(?i)боян|баян')
    def echo_msg(message):
        bot.send_photo(message.chat.id, get_bayn_image(path))
    bot.polling()
    
if __name__ == '__main__':
    main()
