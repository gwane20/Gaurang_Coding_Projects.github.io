"""
    Cong Khang Le (ID: 27444345)
    Gaurang Wanere (ID: 58573754)
"""

import connectfour
import connectfour_library as library
import connectfour_socket as sockets


def start_game() -> None:
    """Starts the game and all other operations of the game"""
    print("ICS 32 Connect Four")
    print('Input an IP address or host to connect to')
    host = input().strip()
    print('Enter a port to connect to on the given host')
    port = int(input())
    username = get_username()

    if sockets.connect(host, port) is False:
        print('Connection couldn\'t be made with the server')
        return 0
    else:
        connection = sockets.connect(host, port)

    if sockets.server(username, connection) is False:
        print('Connection couldn\'t be made with the server')

    print('Connection to server was successful. Starting game.')
    state = connectfour.new_game()

    print('You are the Red player')
    while connectfour.winner(state) == connectfour.NONE:
        print()
        if state.turn == connectfour.RED:
            library.print_gamestate(state)
            print('It\'s your turn')
            move = False
            while move is False:
                col, choice = library.get_move()
                response = sockets.send_move(choice, col, connection)
                if response == 'INVALID':
                    print('Invalid move. Enter the correct moves')
                elif response == 'END':
                    exit_connection(connection)
                    return
                else:
                    state = library.execute_move(state, col, choice)
                    move = True
            
        else:
            library.print_gamestate(state)
            choice, col = sockets.receive_move(connection)
            if choice == 'END':
                exit_connection(connection)
                return
            state = library.execute_move(state, col, choice)
            print('Yellow\'s move was', choice, col)

    winner = connectfour.winner(state)
    print()
    library.print_gamestate(state)
    if winner == connectfour.RED:
        print('You\'ve won the game!')
    else:
        print('Yellow player has won the game!')
    sockets.close_connection(connection)


            
def exit_connection(connection) -> None:
    """Closes all the connection and shows the conenction closing"""
    sockets.close_connection(connection)
    print('Connection closed')


def get_username() -> str:
    """Gets the username from player and checks if spaces occur in name"""
    while True:
        print('Enter a username without any spaces')
        username = input()
        if ' ' in username:
            print('There was a space in username. Try again')
        else:
            return username
            
        
if __name__ == '__main__':
    start_game()

























    
