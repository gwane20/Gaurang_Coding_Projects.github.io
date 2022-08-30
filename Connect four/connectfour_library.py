"""
    Cong Khang Le (ID: 27444345)
    Gaurang Wanere (ID: 58573754)
"""

import connectfour


def get_symbol(player) -> str:
    """Receives the player's symbol for state of game"""
    if player == connectfour.RED:
        return 'R'
    elif player == connectfour.YELLOW:
        return 'Y'
    else:
        return '.'


def get_name(player) -> str:
    """Get's the player's color"""
    if player == connectfour.RED:
        return 'Red'
    elif player == connectfour.YELLOW:
        return 'Yellow'

    
def print_gamestate(state) -> None:
    """Prints out the current game state"""
    print('1  2  3  4  5  6  7')
    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            if col == 0:
                print(get_symbol(state.board[col][row]), end='')
            else:
                print('  ' + get_symbol(state.board[col][row]), end='')
        print('')


def print_turn(state) -> None:
    """Shows whose turn it is"""
    print('It is the ' + get_name(state.turn) + ' player\'s turn')

    
def execute_move(state, col, choice) -> 'state':
    """Will execute the move and sends an error if incorrect"""
    if choice == "DROP":
        return connectfour.drop(state, (col - 1))
    elif choice == "POP":
        return connectfour.pop(state, (col -1))
    else:
        raise connectfour.InvalidMoveError()


def get_move() -> str:
    """Prompts the user to put in a move necessary for the game"""
    while True:
        print('Input either drop or pop, followed by a column number from 1 to 7. EX: "pop 4"')

        move = input()

        choice = move[:4].strip()
        
        try:
            col = int(move[4:].strip())
        except:
            print('Invalid move try again')
            continue

        if col < 1 or col > 7:
            print('Invalid move try again')
            continue
        
        if choice == 'drop':
            return col, "DROP"
        elif choice == 'pop':
            return col, "POP"
        else:
            print('Invalid move try again')
