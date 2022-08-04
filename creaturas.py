from collections import deque
from datetime import datetime
import random


# se tiene "criaturas" el diccionario donde se agregó manualmente todas las criaturas hostiles y pasivas del juego, en esta función se llama al diccionario y se separan los dos tipos de creaturas en dos listas diferentes ordenadas aleatoriamente.
def creacion ():
 criaturas = {}
 criaturas = {'ahogado': {'nombre':'ahogado','tipo': 'hostil', 'simbolo':'°l°','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')},
              'aldeano_zombie': {'nombre':'aldeano_zombie','tipo': 'hostil', 'simbolo':'°d°','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')},
              'anima': {'nombre':'anima','tipo': 'hostil', 'simbolo':'°l°','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')},
              'devastador': {'nombre':'devastador','tipo': 'hostil', 'simbolo': '|°°|','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')},
              'guardian': {'nombre':'guardian','tipo': 'hostil', 'simbolo': '°°','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')}, 
              'invocador': {'nombre':'invocador','tipo': 'hostil', 'simbolo': ':)','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')}
              ,'jinete': {'nombre':'jinete','tipo': 'hostil', 'simbolo': ':S','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')}, 
              'ajolote': {'nombre':'ajolote','tipo': 'hostil', 'simbolo': ':W','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')},
              'aldeano': {'nombre':'aldeano','tipo': 'pasivo', 'simbolo': ':^','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')},
              'bacalao': {'nombre':'bacalao','tipo': 'pasivo', 'simbolo': '😀','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')},
              'caballo': {'nombre':'caballo','tipo': 'pasivo', 'simbolo': '😀','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')},
              'calamar': {'nombre':'calamar','tipo': 'pasivo', 'simbolo': '😀','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')}, 
              'cerdo': {'nombre':'cerdo','tipo': 'pasivo', 'simbolo': '😀','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')}
              ,'conejo': {'nombre':'conejo','tipo': 'pasivo', 'simbolo': '😀','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')}, 
              'tilapia': {'nombre':'tilapia','tipo': 'pasivo', 'simbolo': '😀','fila': random.randint(0, 32),'columna': random.randint(0, 32),'fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')}}
 crpasivas = []
 crhostiles = []
 for clave in criaturas:
  valor = criaturas[clave]['tipo'] 
  if valor == 'hostil':
    crhostiles.append(criaturas[clave])
  else:
    crpasivas.append(criaturas[clave])
 crhostiles = random.sample(crhostiles, len(crhostiles))
 crpasivas = random.sample(crpasivas, len(crpasivas))
  
 return crhostiles,crpasivas

#En esta función se crean las dos colas FIFO de creaturas hostiles y pasivas a partir de las listas de la funcion "creacion"
def colasf (crhostiles,crpasivas,n_hostiles,n_pasivas):
 colah = deque()
 colap = deque()
 for i in range(n_hostiles):
  colah.append(crhostiles[i])
 for i in range(n_pasivas):
  colap.append(crpasivas[i])

 return colah,colap

#diccionario con las creaturas escogidas
def creaturas_load(cola, c_escogidas):
  c_escogidas = cola.popleft()
  
  return c_escogidas