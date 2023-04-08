import random, os, sys, time, copy

#Declaramos todas las variables globales que se ocuparan
#Dos tableros, uno con las respuestas y otro en blanco
tablero=[]
newTablero=[]
#Victorias de los jugadores
vicPrimero=0
vicSegundo=0
#Pares juntados, se reinician al acabar el juego
parPrimero=0
parSegundo=0
#Los tiros de cada jugador, turno_player
opcion1_1=' '
opcion2_1=' '
opcion1_2=' '
opcion2_2=' '
#Saber si acaba de iniciar 
inicio=True
#Saber si acabo el juego
gameOver=False
#Para saber si gana atina el jugador sigue siendo su turno
continuaPrimero=True
continuaSegundo=True
#Saber el numero de partida para mostrar instructivo solo la primera vez
partidas = 0

#############################################################
#Definimos Instructivo, se usa de la variable partidas
def Instructivo():
  global partidas
  #Mostrar en pantalla hasta que el usuario ponga 0
  while True:
    print('\t\t\tMEMORAMA\n')
    print('INSTRUCTIVO\n\n')
    print('1: Cada jugador tiene 2 tiros por turno\n2: Si sus dos tiros coinciden continúa siendo su turno\n3: Gane quien tenga más pares al finalizar el juego\n\nPara comenzar ingrese 0')
    comenzar=input()
    if comenzar == '0':
      partidas=partidas+1
      break
    #Si el usuario pone otra cosa que no sea 0
    while comenzar != '0':
      print('Para comenzar inngresa 0')
      comenzar = input()
      if comenzar == '0':
        break
    partidas=partidas+1
    break

#############################################################
#Crear tablero, revolverlo, poner uno en blanco
def Revolver():
  global tablero
  global newTablero
  global continuaPrimero
  global continuaSegundo
  #Aquí mencionamos que sigue siendo l turno de ambos para cuando llegue su turno
  continuaPrimero=True
  continuaSegundo=True
  tablero=['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I']
  #Revuelve los datos
  random.shuffle(tablero)
  #Se guarda en un tablero a parte
  newTablero=copy.copy(tablero)
  #Tablero original se pone en blanco
  for i in range(len(tablero)):
    tablero[i] = ' '

#############################################################
#Mostramos el tablero en blanco, pero hay cambios y actualizaciones
def Mostrar():
  #Al entrar se borra todo y aparece el tablero
  os.system('clear')
  global tablero
  global newTablero
  global opcion1_1
  global opcion2_1
  global opcion1_2
  global opcion2_2
  #Se checa si alguna de las opciones tiene un valor diferente a ' ', se pide al tablero guardado que nos mande ese valor para mostrarlo en pantalla
  if opcion1_1 != ' ':
    tablero[opcion1_1] = newTablero[opcion1_1]
  if opcion2_1 != ' ':
    tablero[opcion2_1] = newTablero[opcion2_1]
  if opcion1_2 != ' ':
    tablero[opcion1_2] = newTablero[opcion1_2]
  if opcion2_2 != ' ':
    tablero[opcion2_2] = newTablero[opcion2_2]
  #Se imprime el tablero actualizado con las tiradas o sin ellas
  print('MEMORAMA\n')
  print('S para salir\n')
  print('Jugador 1: ', vicPrimero, ' Jugador 2: ', vicSegundo, '\n')
  print('Pares 1: ', parPrimero, ' Pares 2: ', parSegundo, '\n')
  print('Casillas:')
  print('0  1  2  3  4  5\n6  7  8  9  10 11\n12 13 14 15 16 17\n')
  print(tablero[0] + '|' + tablero[1] + '|' + tablero[2] + '|' + tablero[3] + '|' + tablero[4] + '|' + tablero[5])
  print('-+-+-+-+-+-')
  print(tablero[6] + '|' + tablero[7] + '|' + tablero[8] + '|' + tablero[9] + '|' + tablero[10] + '|' + tablero[11])
  print('-+-+-+-+-+-')
  print(tablero[12] + '|' + tablero[13] + '|' + tablero[14] + '|' + tablero[15] + '|' + tablero[16] + '|' + tablero[17])
  print()

#############################################################
#Para checar se comprueba que todas las casillas ya tengan un valor diferente a ' ', y si es asi se acaba
def Chequeo():
  global gameOver
  global parPrimero
  global parSegundo
  global vicPrimero
  global vicSegundo
  if tablero[0] != ' ' and tablero[1] != ' ' and tablero[2] != ' ' and tablero[3] != ' ' and tablero[4] != ' ' and tablero[5] != ' ' and tablero[6] != ' ' and tablero[7] != ' ' and tablero[8] != ' ' and tablero[9] != ' ' and tablero[10] != ' ' and tablero[11] != ' ' and tablero[12] != ' ' and tablero[13] != ' ' and tablero[14] != ' ' and tablero[15] != ' ' and tablero[16] != ' ' and tablero[17] != ' ':
    gameOver=True
    print('Game Over')
    #Se comparan los pares juntados por cada jugador para definir un ganador y sumarle una victoria con espera de 2 segundos (Al ser 9 pares, no hay empates)
    if parPrimero > parSegundo:
      vicPrimero = vicPrimero + 1
      print('Player 1 WINS')
      time.sleep(2)
    if parPrimero < parSegundo:
      vicSegundo = vicSegundo + 1
      print('Player 2 WINS')
      time.sleep(2)
    GameOver()

#############################################################
#Para finalizar el juego, los pares se reincia, se declara el el inciio es verdadero para reiniciar tablero
def GameOver():
  global inicio
  global parPrimero
  global parSegundo
  global continuaPrimero
  global continuaSegundo
  continuaPrimero=False
  continuaSegundo=False
  parPrimero = 0
  parSegundo = 0
  inicio=True

#############################################################
#Turno del jugador 1:
def Player1():
  global opcion1_1
  global opcion2_1
  global parPrimero
  global continuaPrimero
  global continuaSegundo
#Se pide su opcion
#------------------------------------------------------------
  print('Player 1 escoge opcion 1: ')
  opcion1_1=input()
  #Se manda a comprobar que sea un numero de 0-17
  opcion1_1=DatoInvalido(opcion1_1, 1, 1)
  #Ya que la opcion es valido y esté entre 0-17 se comprueba si la casilla esta vacía. Se pedirá un valor hasta que esté vacío, sinedo la opción un número entre 0-17
  while tablero[opcion1_1] != ' ':
    print('Valor en uso')
    print('Player 1 escoge opcion 1: ')
    opcion1_1=input()
    opcion1_1=DatoInvalido(opcion1_1, 1, 1)
  #Ya que es válido y esté entre 0-17 se manda al tablero para mostrar
  if tablero[opcion1_1] == ' ':
    Mostrar()
#Se pide su opcion
#------------------------------------------------------------
  print('Player 1 escoge opcion 2: ')
  opcion2_1 = input()
  #Se manda a comprobar que sea un numero de 0-17
  opcion2_1=DatoInvalido(opcion2_1, 1, 2)
  while tablero[opcion2_1] != ' ':
    print('Valor en uso')
    print('Player 1 escoge opcion 2: ')
    opcion2_1 = input()
    opcion2_1=DatoInvalido(opcion2_1, 1, 2)
  #Ya que es válido y esté entre 0-17 se manda al tablero para mostrar
  if tablero[opcion2_1] == ' ':
    Mostrar() 
  time.sleep(2)
#------------------------------------------------------------
  if tablero[opcion1_1] == tablero[opcion2_1]:
    print('Cual es el elemento?')
    elemento = input()
    if (tablero[opcion1_1] == 'H' and elemento == 'Hidrogeno') or (tablero[opcion1_1] == 'I' and elemento == 'Yodo'): 
      parPrimero = parPrimero + 1
      opcion1_1 = ' '
      opcion2_1 = ' '
      Mostrar()
      Chequeo()
  else:
    tablero[opcion1_1] = ' '
    tablero[opcion2_1] = ' '
    opcion1_1=' '
    opcion2_1 = ' '
    continuaPrimero=False
    continuaSegundo=True
    Mostrar()

#############################################################
#Turno del jugador 2:
def Player2():
  global opcion1_2
  global opcion2_2
  global parSegundo
  global continuaSegundo
  global continuaPrimero
#Se pide su opcion
#------------------------------------------------------------
  print('Player 2 escoge opcion 1: ')
  opcion1_2 = input()
  #Se manda a comprobar que sea un numero de 0-17
  opcion1_2=DatoInvalido(opcion1_2, 2, 1)
  while tablero[opcion1_2] != ' ':
    print('Valor en uso')
    print('Player 2 escoge opcion 1: ')
    opcion1_2 = input()
    opcion1_2=DatoInvalido(opcion1_2, 2, 1)
  #Ya que es válido y esté entre 0-17 se manda al tablero para mostrar
  if tablero[opcion1_2] == ' ':
    Mostrar()
#Se pide su opcion
#------------------------------------------------------------
  print('Player 2 escoge opcion 2: ')
  opcion2_2 = input()
  #Se manda a comprobar que sea un numero de 0-17
  opcion2_2=DatoInvalido(opcion2_2, 2, 2)
  while tablero[opcion2_2] != ' ':
    print('Valor en uso')
    print('Player 2 escoge opcion 2: ')
    opcion2_2 = input()
    opcion2_2=DatoInvalido(opcion2_2, 2, 2)
  #Ya que es válido y esté entre 0-17 se manda al tablero para mostrar
  if tablero[opcion2_2] == ' ':
    Mostrar()
  time.sleep(2)
#------------------------------------------------------------
  if tablero[opcion1_2] == tablero[opcion2_2]:
    parSegundo = parSegundo + 1
    opcion1_2 = ' '
    opcion2_2 = ' '
    Mostrar()
    Chequeo()
  else:
    tablero[opcion1_2] = ' '
    tablero[opcion2_2] = ' '
    opcion1_2=' '
    opcion2_2 = ' '
    continuaSegundo=False
    continuaPrimero=True
    Mostrar()

#############################################################
#Comprobar el dato, hasta que sea un numero del 0-17
#Se pide la opcion, número del player y el turno
def DatoInvalido(a, player, turno):
  #Si se detecta que es 'S', se sale
  if a == 'S':
    sys.exit()
  #Lo guardamos en una variable temporal
  guardar=a
  #Si el valor no es un numero del 0-17, saldrá de aquí hasta ser válido
  while guardar!='0' and guardar!='1' and guardar!='2' and guardar!='3' and guardar!='4' and guardar!='5' and guardar!='6' and guardar!='7' and guardar!='8' and guardar!='9' and guardar!='10' and guardar!='11' and guardar!='12' and guardar!='13' and guardar!='14' and guardar!='15' and guardar!='16' and guardar!='17':
    #Se le pide ingresar un valor
    print('Dato invalido')
    print('Player ', player,' escoge opcion ', turno, ':')
    guardar=input()
    if guardar == 'S':
      sys.exit()
    #Cuando sea número del 0-17 se pasará a la variable principal
    if guardar=='0' or guardar=='1' or guardar=='2' or guardar=='3' or guardar=='4' or guardar=='5' or guardar=='6' or guardar=='7' or guardar=='8' or guardar=='9' or guardar=='10' or guardar=='11' or guardar=='12' or guardar=='13' or guardar=='14' or guardar=='15' or guardar=='16' or guardar=='17':
      a=guardar
  #Se convierte a netero el valor y se envía
  a=int(a)
  return a
      
#############################################################
#Loop infinito hasta que no ponga 'S'
while True:
  #Si el inicio es verdadero entra, se revuelve el tablero y se borra todo
  if inicio == True:
    #Si será la primera partida se mostrará el instructivo
    if partidas == 0:
      Instructivo()
    os.system('clear')
    gameOver = False
    Revolver()
  #Terminado de revolver y declarar que no es fin de juego se declara que inicio es falso para no revolver más veces
  inicio=False
  #Mientras el juego no ha finalizado se muestra tablero
  while gameOver == False:
    Mostrar()
    #Si el juego no ha finalizado sepide turnos de los jugadores 
    #Mientras su continuación este en verdadero será su turno, se convertirá en falso cuando no le atinen
    while continuaPrimero == True:
      if gameOver == False:
        Player1()
    while continuaSegundo == True:
      if gameOver == False:
        Player2()