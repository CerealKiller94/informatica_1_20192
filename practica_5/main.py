import triqui as tr
import os 
""" El módulo os se utiliza para obtener 
la variable date del sistema *nix"""

"""
Nombre: Yonathan López Mejía
Documento: 1017220389
Variables adicionales:
    * player_name = nombre del jugador humano
    * user_win = contador para cuando el usuario gana
    * computer_win = contador para cuando el ordenador gana
    * tied_game = contador para cuando se da un empate
    * tablero = lista con 10 posiciones donde se almacenan
    las jugadas
    * marca_usuario: almacena el símbolo que usará el usuario para marcar el tablero
    * marca_computadora: almacena el símbolo que usará la computadora para marcar el tablero
    * finalizar: esta variable booleana almacena True si se va a terminar
    el programa y False si todavía se ejecutará al menos una vez más otra partida
    * file: variable que tiene la referencia en memoria al archivo de texto a escribir
    
"""
tr.printIntro('intro.txt')
player_name = input('Nombre del jugador: \n')
user_win = 0
computer_win = 0
tied_game = 0

turn ="" # Indica quién tiene el turno para jugar, el usuario o la computadora.
while True:
    """
    En esta primera parte del ciclo principal se crea el tablero,
    se definen las marcas del usuario y la computadora y se muestran en consola;
    se elije el turno para saber quién empieza y se inicia
    el juego. Además, se muestra el marcador actual
    """
    print('''
    Marcador:
        Victorias humanas:     {0}
        Victorias computadora: {1}
        Empates:               {2}
    '''.format(user_win, computer_win, tied_game))
    tablero = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    marca_usuario, marca_computadora = tr.inputPlayerLetter().split(',')
    print('La marca del usuario es:', marca_usuario)
    print('La marca de la computadora es:',marca_computadora)
    turn = tr.whoGoesFirst()
    print(turn + ' va primero.')
    jugando = True

    while jugando:
        if turn == 'Usuario':
            """
            Cuando el turno lo tiene el usuario se ejecuta esta parte en
            este orden:
                1. Se muestra el tablero en el estado actual
                2. Se actualiza el tablero con las siguientes condiciones
                    *se recibe el tablero actualizado por parte
                    de la función getPlayerMove en el módulo triqui
                    * Se valida si el jugador ganó con la jugada anterior,
                    en ese caso se muestra el tablero, se cuenta una victoria
                    para el humano, se muestra un mensaje de victoria y se termina la partida
                    *Si no, se valida si hay un empate preguntando si ya no hay
                    espacios disponibles en el tablero, en caso de darse
                    muestra el estado final del tablero, se cuenta un empate más
                    se muestra un mensaje de empate y se termina la partida.
                   * Si no hay victoria o empate entonces el computador
                   toma el siguiente turno
            """
            
            tr.drawBoard(tablero)
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
        
            turn = 'Computadora'

        else: 
            """
            Cuando la computadora tiene el turno se ejecuta esta parte
            1. Se actualiza el tablero con el retorno de la función
            getComputerMove() del módulo triki y se verifican las siguientes condiciones:
                * Si la jugada anterior fue la ganadora entonces
                se muestra el estado final del tablero, se cuenta 
                una victoria para la computadora, se muestra un mensaje
                de victoria y se termina la partida.
                * Si no, se valida si hay espacios vacíos en el tablero,
                en caso de que no hayan significa que hay un empate, por tanto,
                se muestra el estado final del tablero, se cuenta un empate más
                y se muestra un mensaje de empate
                * En caso de que no haya jugada ganadora, ni empate, entonces
                el jugador humano toma el turno
            """
            tablero = tr.getComputerMove(tablero, marca_computadora)
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

         
            turn = 'Usuario'
            

    while True:
        """Cuando se termina una partida se ejecuta la siguiente parte:
       Se pregunta si quiere volver a jugar.
        * En caso de querer volver a jugar se actualiza la variable
        finalizar con el valor False y comienza una nueva partida para el mismo jugador
        * En caso de querer terminar con el programa se escribe
        en un archivo de texto externo el formato definido en la guía,
        se escribe: la fecha en formato del sistema, el nombre del usuario,
        la cantidad de victorias del usuario, de la máquina y el número de empates.
        Finalmente se actualiza la variable finalizar con True y se rompe el ciclo
    """
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
                
            finalizar = True
            break
        if opc == 's':
            finalizar = False
            break
        print('Opción no válida')
    """
    En caso de querer terminar el juego luego de romper el ciclo principal
    se valida el valor de variable finalizar. Si la variable es True
    significa que se quiere acabar con todo el programa y se rompe el ciclo principal,
    en caso de que la variable tenga el valor False significa que no se quiere
    terminar la partida y se ignora.
    """
    if finalizar:
        break

