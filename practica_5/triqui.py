import random


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
            print(line)
    

def drawBoard(board):
    # Esta función imprime el tablero en la consola
    # Argumentos:
    # Board: Lista de strings que representa el estado del tablero

    # Desarrolle el cuerpo de la función aquí...
    print(''' 
     {6}  | {7}  | {8}
    ----+----+---
     {3}  | {4}  | {5}
    ----+----+---
     {0}  | {1}  | {2}        
    '''.format(*board[1:]))

def inputPlayerLetter():
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
    
    # Esta función le permite escoger al usuario entre la letra "X" y la letra "O".

    # retorna una lista de strings donde la letra escogida por el usuario
    # ocupa la primera posición y la letra que le corresponde a la computadora
    # ocupa la segunda posición.

    # Desarrolle el cuerpo de la función aquí...
    
def whoGoesFirst():
    # Esta función escoge de forma aleatoria quien inicial el juego.

    # Retorna el string "Usuario" si el usuario inicia el juego o
    # el string "Computadora" si la computadora inicia el juego.

    # Desarrolle el cuerpo de la función aquí...
    return random.choice(['Usuario', 'Computadora'])

def makeMove(board, letter, move):
    board[move] = letter
    return board

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: Es la marca que se desea poner en el tablero ("X" o "O").
    # move: Es el número de la casilla donde se desea poner la marca.

    # Desarrolle el cuerpo de la función aquí...

def isWinner(board, letter):
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
    # Esta función debe verificar si hay una jugada ganadora en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: La marca que se desea verificar ("X" o "O").

    # Esta función debe retornar el valor lógico True, si hay una jugada ganadora o
    # debe retornar el valor lógico False, si no hay una jugada ganadora.

    # Desarrolle el cuerpo de la función aquí...
    pass

def isSpaceFree(board, move):
    return board[move].isspace()
    # Esta función verifica si hay una casilla vacía en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # move: Es el número de la casilla que se desea verificar.

    # Esta función debe retornar el valor lógico True, si la casilla está vacía
    # en caso contrario, debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...

def getPlayerMove(board, marca_usuario):
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
    # Esta función le pide al usuario que ingrese el número de la casilla
    # que quiere marcar.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función retorna el número de la casilla seleccionada por el usuario.


    # Desarrolle el cuerpo de la función aquí...

def chooseRandomMoveFromList(board, movesList):
    
    # Esta función escoge de forma aleatoria una casilla vacía del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # moveList: Lista que contiene los números de las casillas a verificar (ver documento de la práctica).

    # Esta función debe retornar alguno de los números de casillas en moveList
    # desde que dicha casilla esté vacía. Si ninguna de las casillas está vacía,
    # esta función debe retornar el valor None.

    # Desarrolle el cuerpo de la función aquí...
    while len(movesList) > 0:
        move = random.choice(movesList)
        if isSpaceFree(board, move):
            return move
        else:
            del movesList[movesList.index(move)]
    return None
    

def getComputerMove(board, computerLetter):
    
    copy_of_board = board
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
        
    move = chooseRandomMoveFromList(board, list(range(1,10)))
    
    if move is not None:
        board[move] = computerLetter
        
    return board

    # Esta función implementa la estrategia de juego de la computadora.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # computerLetter: La marca que está usando la computadora.

    # Desarrolle el cuerpo de la función aquí...

    # 1. Verificar si la computadora puede ganar...

    # 2. Si no, verificar si el usuario puede ganar en la siguiente jugada, si si, bloquear esta jugada...

    # 3. Si no, tratar de poner una marca en alguna de las esquinas, si alguna está vacía...

    # 4. Si no, tratar de marcar la casilla del centro, si esta está vacía...

    # 5. Si no, tratar de poner una marca en alguna de las casillas de los lados...


def isBoardFull(board):
    return ' ' in board[1:]
    # Esta función verifica si el tablero está lleno.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función debe retorna el valor lógico True, si el tablero está lleno.
    # En caso contrario debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    