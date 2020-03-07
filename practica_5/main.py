import triqui as tr
import sys

tr.printIntro('intro.txt')

turn ="" # Indica quién tiene el turno para jugar, el usuario o la computadora.
while True:

    tablero = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    marca_usuario, marca_computadora = tr.inputPlayerLetter().split(',')
    print('La marca del usuario es:', marca_usuario)
    print('La marca de la computadora es:',marca_computadora)
    #4. Quién va primero el usuario o la computadora?
    turn = tr.whoGoesFirst()
    print(turn + ' va primero.')
    jugando = True # El juego ha iniciado

    while jugando:
        if turn == 'Usuario': # 5. Turno del usuario

            # a. Mostrar tablero
            tr.drawBoard(tablero)
            # c. Actualizar el tablero
            tablero = tr.getPlayerMove(tablero, marca_usuario)
            if tr.isWinner(tablero, marca_usuario):
                tr.drawBoard(tablero)
                print('¡El humano ha vencido a la máquina!')
                break
            elif not tr.isBoardFull(tablero):
                tr.drawBoard(tablero)
                print('Empate')
                break
        
            # d. Verificar si el usuario ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.

            # e. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno

            turn = 'Computadora'

        else: # 6. Turno de la computadora.
            tablero = tr.getComputerMove(tablero, marca_computadora)
            # a. Computadora hace jugada.
            # b. Actualizar el tablero.
            # c. Verificar si la computadora ha ganado el juego.
            if tr.isWinner(tablero, marca_computadora):
                tr.drawBoard(tablero)
                print('La máquina ha vencido al humano. Skynet se acerca')
                break
            elif not tr.isBoardFull(tablero):
                tr.drawBoard(tablero)
                print('Empate')
                break
                
            
           
            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.

            # d. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.
            turn = 'Usuario'
            

    # 7. Preguntar si el usuario quiere jugar una vez mas
    while True:
        opc = input('¿Quiere volver a jugar? s/n\n')
        if opc == 'n':
            sys.exit()
        if opc == 's':
            break
        print('Opción no válida')
            
    #    Si no, finalizar el programa.
