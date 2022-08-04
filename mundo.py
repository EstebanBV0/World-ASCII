
#funcion donde se crea el mundo con la dimensión necesaria e inicialmente en cada espacio se agrego un gión '-'
def mundo_r(dim):
 murallas = []
 for i in range (dim):
    murallas.append([])
    for j in range (dim):
        valor  = '-'
        murallas [i].append(valor)
 return murallas

#función donde se tiene como paramentro de entrada el mundo creado en la anterior función, la ubicación de cada muralla asi como su ancho y largo, dicha función retornara el mundo construido.
def muros(murallas, fila, columna, ancho, largo,alias_s,criatura_escog):
  
  for m in range( len(fila) ):
      for i in range( ancho[m] ):
          for j in range ( largo[m] ):
              murallas[fila[m]+j][columna[m]+i]='#'
  murallas[alias_s['Fila']][alias_s['Columna']] = alias_s['simbolo']
  murallas[criatura_escog['fila']][criatura_escog['columna']] = criatura_escog['simbolo']
  
  return murallas

# Esta función lee cada uno de los # en el mundo. Ademas, busca el simolo del jugador por si se encuentra en el mundo dado el caso seguira teniendo 10 vidas de lo contrario se le restara una, tambien retornara el numero de criaturas desencoladas dentro del mundo.

def sondeo_mundo(world,alias_s):
  
  nt_criaturas = 0
  n_vidas = 0
  n_muros = 0
  for i in range(32):
    for j in range (32):
        if world[i][j] != '#' and world[i][j] != '-':
          if world[i][j] == alias_s['simbolo']:
            n_vidas += 1
          else:
            nt_criaturas += 1
        elif world[i][j] == '#':
          n_muros += 1
        else:
          pass
 
  if n_vidas == 0:
    n_vidas == 9
  else:
    n_vidas = 10
  return n_muros,n_vidas,nt_criaturas









