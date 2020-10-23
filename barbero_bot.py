#!/usr/bin/python3.6
import telepot
import time
import urllib3
import random

# parte di codice relativa all'hosting
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# fine


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        info = msg['from']
        utente = info['username']
        print("richiesta:",utente)
        if msg['text'] == '/1': #video random
            bot.sendMessage(chat_id, random.choice(list(open('database.txt'))))

        elif msg['text'] == '/2': #aiuto
            mess2 = 'Il bot è molto semplice basta scegliere nel menu a tendina /1 per avere un video random del professore.'
            bot.sendMessage(chat_id, mess2)

        elif msg['text'] == '/3': #crediti
            mess3 = 'Bot creato da  @filippo1996 , un appassionato di storia, per permettere a tutti gli appassionati di godere dei contenuti del professore con un semplice click.'
            bot.sendMessage(chat_id, mess3)

        elif msg['text'] == '/start': #inizio dell'uso del bot
            bot.sendMessage(chat_id, 'Benvenuto/a: scrivere /1 per avere la tua dose di Barbero quotidiana.')

        else: #comando sbagliato
            bot.sendMessage(chat_id, 'scegliere un comando')

TOKEN = "1278488007:AAFt3acOIg9_5axLkRzcEaH58CPgqN1AG2U" #token
bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print('Listening ...')

import time
while 1:
    time.sleep(10)