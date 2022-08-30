"""
    Cong Khang Le (ID: 27444345)
    Gaurang Wanere (ID: 58573754)
"""

import socket
import connectfour_library as library
import collections

cfConnection = collections.namedtuple(
    'cfConnection',
    ['socket', 'input', 'output'])



def connect(host, port) -> 'cfConnect':
    """Connects to the host, if fails will return False"""
    try:
        cf_socket = socket.socket()
        cf_socket.connect((host, port))
        
        cf_input = cf_socket.makefile('r')
        cf_output = cf_socket.makefile('w')

        return cfConnection(
            socket = cf_socket,
            input = cf_input,
            output = cf_output)
    except:
        return False


def server(username, connection) -> bool:
    """Will communicate with the server, if anything is incorrect
       will return False"""
    _write_stream('I32CFSP_HELLO ' + username + '\r\n', connection)
    
    response = _read_line(connection)
    if response[:7] != 'WELCOME' or response[8:] != (username):
        return False

    _write_stream('AI_GAME\r\n', connection)

    response = _read_line(connection)
    if response != ('READY'):
        return False
    
    return True

    
def send_move(choice, col, connection) -> str:
    """Will send a move to the server and see if valid move or not"""
    try:
        if choice == 'DROP':
            _write_stream('DROP ' + str(col) + '\r\n', connection)
        elif choice == 'POP':
            _write_stream('POP ' + str(col) + '\r\n', connection)

        response = _read_line(connection)
        if response == 'INVALID':
            response = _read_line(connection)
            if response != ('READY'):
                close_connection(connection)
                return 'END'
            return 'INVALID'
        elif response != 'OKAY' and response != 'WINNER_RED' and response != 'WINNDER_YELLOW':
            close_connection(connection)
            return 'END'

        return response
    except:
        close_connection(connection)
        return 'END'


def receive_move(connection) -> str:
    """Receives a move from the server and returns a move and colum"""
    try:
        response = _read_line(connection)
        if response.startswith('DROP'):
            choice = 'DROP'
            col = int(response[5:].strip())
        elif response.startswith('POP'):
            choice = 'POP'
            col = int(response[4:].strip())
        else:
            close_connection(connection)
            return 'END', 0

        response = _read_line(connection)
        if response == 'WINNER_RED' or response == 'WINNER_YELLOW':
            close_connection(connection)
        elif response != ('READY'):
            close_connection(connection)
            return 'END', 0
        return choice, col
    except:
        close_connection(connection)
        return 'END', 0


def close_connection(connection) -> None:
    """Close all connections when needed"""
    connection.input.close()
    connection.output.close()
    connection.socket.close()


def _write_stream(text, connection) -> None:
    """Write whatever's needed to the server"""
    connection.output.write(text)
    connection.output.flush()


def _read_line(connection) -> str:
    """Read whatever the server sends without the client end of line"""
    line = connection.input.readline()[:-1]

    return line
