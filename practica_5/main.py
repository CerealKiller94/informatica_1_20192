import triqui as tr
import sys
import os

tr.printIntro('intro.txt')
player_name = input('Nombre del jugador: \n')
user_win = 0
computer_win = 0
tied_game = 0

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
                user_win += 1
                print('¡El humano ha vencido a la máquina!')
                break
            elif not tr.isBoardFull(tablero):
                tr.drawBoard(tablero)
                tied_game += 1
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
                computer_win += 1
                print('La máquina ha vencido al humano. Skynet se acerca')
                break
            elif not tr.isBoardFull(tablero):
                tr.drawBoard(tablero)
                tied_game += 1
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
            with open('estadisticas.txt', 'a') as file:
                message = '''
                ------------------------------ Triqui -----------------------------
                
                {0}
                
                Nombre del jugador: {1}
                
                Juegos ganados por el usuario: {2}
                Juegos ganados por el computador: {3}
                Juegos empatados: {4}
                
                -------------------------------------------------------------------
                '''.format(os.popen('date').read(), player_name, user_win, computer_win, tied_game)
                file.write(message)
                
            sys.exit()
        if opc == 's':
            break
        print('Opción no válida')
            
    #    Si no, finalizar el programa.
