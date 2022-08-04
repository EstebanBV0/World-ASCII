import numpy as np
import validacion as v
import creaturas as c
import usuario as u
import mundo as m


dim = 32
#diccionario de las creaturas 
c_escogidas = {}
#solicitud de numero de criaturas
n_hostiles = int(input('Ingrese el numero de creaturas hostiles: '))
n_pasivas = int(input('Ingrese el numero de creaturas pasivas: '))
#validación    
validación = v.validar_c(n_hostiles,n_pasivas)
print(validación)
#creacion de lista de creaturas a partir del diccionario
crhostiles,crpasivas = c.creacion()
# return de las dos colas tipo FIFO con creaturas hostiles y pasivas
cr_hostiles,cr_pasivas = c.colasf(crhostiles,crpasivas,n_hostiles,n_pasivas)
#retorna el diccionario donde se alojan las creaturas descoladas que estan dentro del mundo
criatura_escog = c.creaturas_load(cr_hostiles,c_escogidas)
# se crea un jugador con ciertas caracteristicas
n_jugador =  u.personaje()
# esta función retorna el jugador en un diccionario a partir del alias dado en consola
alias_s = u.usuario_s(n_jugador)
#Reporte del juego:

#se llama la funcion world donde se creará el mundo y se retornará

#Cant = int(input('Ingrese el numero de muros que tendrá el mundo: '))

# se crean las listas de fila,columna,ancho y largo para hubicarlas en el mundo
Fila = [0,3,5,6]
Columna = [1,3,11,12]
Ancho = [2,9,1,4]
Largo =[5,2,2,1]
"""""
#se solicita elemento por elemento la fila, columna largo y ancho de la determinada muralla.
for i in range(Cant):
    # Recuerda que range comenzará desde 0, así que imprimimos el número solicitado pero + 1
    Fila_a = int(input(f"Ingresa la posición de la fila {i + 1}: "))
    Columna_a = int(input(f"Ingresa la posición de la columna {i + 1}: "))    
    Ancho_a = int(input(f"Ingrese el ancho de la muralla {i + 1}: "))
    Largo_a = int(input(f"Ingresa el largo de la columna {i + 1}: "))  
    Fila.append(Fila_a)
    Columna.append(Columna_a)
    Ancho.append(Ancho_a)
    Largo.append(Largo_a)
                            
print("--------------------------------------------")
print(" ")
"""""

# esta función crea el mundo vacio
world = m.mundo_r(dim)
# esta función con el mundo creado, enviar las murallas con sus respectivas localizaciones al igual que la creatura desencolada y el jugador y los pone en el mundo en un lugar aleatorio ""PRIMERA FUNCIÓN""
world = m.muros(world, Fila, Columna, Ancho, Largo, alias_s,criatura_escog) 
#""SEGUNDA FUNCIÓN""
n_muros,n_vidas,nt_criaturas = m.sondeo_mundo(world,alias_s)

# se imprime el mundo linea por linea
# se pasa de una lista de listas a un array para imprimirlo de forma conveniente
print(n_muros,n_vidas,nt_criaturas)
print('\n')
mura = np.array(world, dtype=object)
for line in mura:
        print ('  '.join(map(str, line)))



