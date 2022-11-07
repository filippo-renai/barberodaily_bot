#il mio primo bot telegram
import telepot
import time
import urllib3
import random

db = 'database.txt'

#data un giorno restituisce il link della puntanta se presente
def cercaPuntata(giorno):
   with open(db) as f:
      datafile = f.readlines()
   for line in datafile:
      link = line.split('|')
      if link[0] == giorno: #ha trovato la puntata
         return link[1]
   return 'Puntata non trovata'

#aggiornare il db delle puntate
def aggiornaDB(link):
   link += '\n'
   file_object = open(db, 'a')
   file_object.write(link)

#restituisce l'ultima puntata
def ultimaPuntata():
   with open(db) as f:
      for line in f:
         pass
      return line

#restituisce numero ultima puntata
def ultimaPuntataGiorno():
   with open(db) as f:
      for line in f:
         pass
      return line.split('|')[0]



def on_chat_message(msg):
   content_type, chat_type, chat_id = telepot.glance(msg)

   if content_type == 'text': #ultimo video
      if msg['text'] == '/1':
         bot.sendMessage(chat_id,'ciao')

      elif msg['text'] == '/2': #aiuto
         mess2 = 'Il bot è molto semplice basta scegliere nel menu a tendina /1 per avere un video random del professore.'
         bot.sendMessage(chat_id, mess2)

      elif msg['text'] == '/3': #crediti
         mess3 = 'Bot creato da  @filippo1996 , un appassionato di storia, per permettere a tutti gli appassionati di godere dei contenuti del professore con un semplice click.'
         bot.sendMessage(chat_id, mess3)

      elif msg['text'] == '/start': #inizio dell'uso del bot
         bot.sendMessage(chat_id, 'Benvenuto/a: scrivere /1 per avere la tua dose di cerbero quotidiana.')

      else: #comando sbagliato
         bot.sendMessage(chat_id, 'scegliere un comando')


TOKEN = "inserire il token"
ric = 0
bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print('Ascolto ...')

import time
while 1:
   time.sleep(10)
