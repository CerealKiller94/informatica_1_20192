import random

"""
Nombre: Yonathan López Mejía
Documento: 1017220389
"""

def printIntro(introFile):
    '''
        Firma:
            (string) -> ()

        Sinopsis:
            función que imprime el contenido de un archivo en pantalla, en este
    		caso, el mensaje de bienvenida al juego

        Entradas y salidas:
            - inputFile: Nombre del archivo que contiene la presentación del juego
            - returns: None, solo imprime el archivo leído en pantalla

        Ejemplos de uso:

            >>> printIntro("intro.txt")

            ████████╗██████╗ ██╗ ██████╗ ██╗   ██╗██╗
            ╚══██╔══╝██╔══██╗██║██╔═══██╗██║   ██║██║
               ██║   ██████╔╝██║██║   ██║██║   ██║██║
               ██║   ██╔══██╗██║██║▄▄ ██║██║   ██║██║
               ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║
               ╚═╝   ╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝
        '''

    with open(introFile) as message:
        for line in message:
            print(line, end='')
    

def drawBoard(board):
    """ Esta función imprime el tablero en la consola
     Argumentos:
     Board: Lista de strings que representa el estado del tablero """

    print(''' 
     {6}  | {7}  | {8}
    ----+----+---
     {3}  | {4}  | {5}
    ----+----+---
     {0}  | {1}  | {2}        
    '''.format(*board[1:]))

def inputPlayerLetter():
    """
    Esta función le permite escoger al usuario entre la letra "X" y la letra "O".
    retorna una lista de strings donde la letra escogida por el usuario
    ocupa la primera posición y la letra que le corresponde a la computadora
    ocupa la segunda posición.
    """
    while True:
        opc = input('Seleccione X o O para jugar\n').upper()
        if opc == 'X':
            letras = 'X,O'
        elif opc == 'O':
            letras = 'O,X'
        else:
            print('No seleccionó un símbolo valido')
            continue
            
        return letras
    
    

    # Desarrolle el cuerpo de la función aquí...
    
def whoGoesFirst():
    """
    Esta función escoge de forma aleatoria quien inicial el juego.
    Retorna el string "Usuario" si el usuario inicia el juego o
    el string "Computadora" si la computadora inicia el juego.
    """
    return random.choice(['Usuario', 'Computadora'])

def makeMove(board, letter, move):
    """
    Esta función agrega la marca del jugador o la computadora en la lista
    que representa el estado actual del tablero y luego
    retorna el tablero
    Argumentos:
    board: Lista de strings que almacena el estado del tablero.
    letter: Es la marca que se desea poner en el tablero ("X" o "O").
    move: Es el número de la casilla donde se desea poner la marca.
    """
    
    board[move] = letter
    return board


def isWinner(board, letter):
    
    """
    Esta función verifica si hay una jugada ganadora en el tablero.
    Valida cada una de las posibles formas de ganar definidas
    por las combinaciones en las posiciones de la lista
    Argumentos:
    board: Lista de strings que almacena el estado del tablero.
    letter: La marca que se desea verificar ("X" o "O").
    Esta función retorna el valor lógico True, si hay una jugada ganadora o
    retorna el valor lógico False, si no hay una jugada ganadora.
    """
    if board[1:4] == [letter, letter, letter]:
        return True
    
    if board[4:7] == [letter, letter, letter]:
        return True
    
    if board[7:10] == [letter, letter, letter]:
        return True
    
    if board[1] == letter and board[5] == letter and board[9] == letter:
        return True
    
    if board[7] == letter and board[5] == letter and board[3] == letter:
        return True
    
    if board[7] == letter and board[4] == letter and board[1] == letter:
        return True
    
    if board[8] == letter and board[5] == letter and board[2] == letter:
        return True
    
    if board[9] == letter and board[6] == letter and board[3] == letter:
        return True
    
    return False
   
 

def isSpaceFree(board, move):
    """
    Esta función verifica si hay una casilla vacía 
    en una posición de la lista que representa el tablero.
    Argumentos:
    board: Lista de strings que almacena el estado del tablero.
    move: Es el número de la casilla que se desea verificar.

    Esta función retorna el valor lógico True, si la casilla está vacía
    en caso contrario, retorna el valor lógico False.
    """
    return board[move].isspace()
    

def getPlayerMove(board, marca_usuario):
    
    """
    Esta función le pide al usuario que ingrese el número de la casilla
    que quiere marcar definida por un número entre 1 y 9.
    Se pide el número y se valida usando la función isSpaceFree si el tablero
    en esa posición está vacío, en caso de estar vacío
    envía el estado del tablero, la marca del usuario y la posición
    a la función makeMove, en caso de que no lo esté muestra un mensaje
    y vuelve a pedir ingresar la información. El ciclo
    se repite hasta que el usuario ingrese el número correcto
    
    Argumentos:
    board: Lista de strings que almacena el estado del tablero.
    marca_usuario: el símbolo que representa la marca del usuario
    en la partida actual.
    Esta función retorna el tablero con el movimiento ejecutado.
    """
    while True:
        numero = int(input('Escriba el número de la casilla (1-9): '))
        if 1 <= numero <= 9:
            is_free = isSpaceFree(board, numero)
            if is_free:
                break
            else:
                print('El número está ocupado')
        else:
            print('Digite un número entre 1 y 9')
    
    return makeMove(board, marca_usuario, numero)
    
 
def chooseRandomMoveFromList(board, movesList):
    
    """
    Esta función escoge de forma aleatoria una casilla vacía del tablero.
    Argumentos:
    board: Lista de strings que almacena el estado del tablero.
    moveList: Lista que contiene los números de las casillas a verificar.
    Esta función retorna alguno de los números de casillas en moveList
    desde que dicha casilla esté vacía. Si ninguna de las casillas está vacía,
    esta función retorna el valor None.
    """
    
    while len(movesList) > 0:
        move = random.choice(movesList)
        if isSpaceFree(board, move):
            return move
        else:
            del movesList[movesList.index(move)]
    return None
    

def getComputerMove(board, computerLetter):
    
    
    """
    Esta función hace una copia del tablero e implementa la estrategia de juego de la computadora.
    1. Verifica si la computadora puede ganar, en caso afirmativo realiza la jugada y retorna el tablero
    con la jugada
    2. Si no, verifica si el usuario puede ganar en la siguiente jugada, en caso de que 
    sí, bloquea la jugada del usuario y retorna el tablero actualizado
    3. Si no, trata de poner una marca en alguna de las esquinas
    4. Si no, trata de marcar la casilla del centro
    5. Si no, tratar de poner una marca en alguna de las casillas de los lados
    si se cumple 3, 4, o 5 o ninguna, igualmente retorna el tablero con la jugada
    o sin ella si no puede realizarla
    
    Argumentos:
    board: Lista de strings que almacena el estado del tablero.
    computerLetter: La marca que está usando la computadora.
    """
    
    copy_of_board = board #Copia del estado del tablero
    i = 1
    while i < len(copy_of_board):
        if isSpaceFree(copy_of_board, i):
            copy_of_board[i] = computerLetter
            if isWinner(copy_of_board, computerLetter):
                board[i] = computerLetter
                return board
            else:
                copy_of_board[i] = " "
        i += 1
    
    i = 0
    
    if computerLetter == 'O':
        userLetter = 'X'
    else:
        userLetter = 'O'
        
    while i < len(copy_of_board):
        if isSpaceFree(copy_of_board, i):
            copy_of_board[i] = userLetter
            if isWinner(copy_of_board, userLetter):
                board[i] = computerLetter
                return board
            else:
                copy_of_board[i] = " "
        i += 1
    
    movimientos = [[1, 3, 7, 9], [5], [2, 4, 6, 8]]
    
    for moves_list in movimientos:
        move = chooseRandomMoveFromList(board, moves_list)
        if move is not None:
            board[move] = computerLetter
            break
       
    return board



def isBoardFull(board):
    """
    Esta función verifica si el tablero está lleno.
    Argumentos:
    board: Lista de strings que almacena el estado del tablero.
    Esta función retorna el valor lógico True, si el tablero está lleno.
    En caso contrario retorna el valor lógico False.
    """
    return ' ' in board[1:]
    