from datetime import datetime
import random

# esta función crea un personaje y retorna un diccionario
def personaje():
  tipo = input('Tipo: ')
  al = input('ingrese el alias del jugador: ')
  simb = input('ingrese un simbolo que representa su personaje: ')
  personaje = {'tipo': tipo, 'alias': al,'simbolo':simb ,'Fila': random.randint(0, 32) ,'Columna': random.randint(0, 32) , 'Fecha': datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'), 'N corazones': 10}
  
  return personaje
#esta función toma un diccionario de personajes, busca uno de ellos a partir de su alias y lo retorna en un diccionario aparte        
def usuario_s (personaje):
  datos = {}
  alias = input('Digite el alias que esta buscando: ')
  for clave in personaje: 
      if personaje[clave] == alias:
        datos = personaje
 
  return datos
