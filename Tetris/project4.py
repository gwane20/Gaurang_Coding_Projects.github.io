import project4_logic as game


def run() -> None:
    '''
    This starts the game
    '''
    rows = size()
    colm = size()
    g_play = game.Game(rows, colm)
    command = operation()
    
    if command == 'CONTENTS':
        rows_Lst = []
        for i in range(rows):
            rows_info = []
            command = next_move()
            for index in range(colm):
                rows_info.append(command[index])
            rows_Lst.append(rows_info)
        g_play.board_info(rows_Lst)

    while True:
        board(g_play)
        command = operation()
        if command == 'Q':
            return
        if command == '':
            if g_play.count():
                board(g_play)
                break
        else:
            control_command(command, g_play)
    print('GAME OVER')


def control_command(action: str, g_play) -> None:
    '''
    Performs the action given by the user during gameplay
    '''
    if action == 'R':
        g_play.faller_rotation()
    elif action == '<':
        g_play.move_faller_side(game.LEFT)
    elif action == '>':
        g_play.move_faller_side(game.RIGHT)
    elif action[0] == 'F':
        try:
            arg = action.split(' ')
            colm_num = int(arg[1])
            faller = [arg[4], arg[3], arg[2]]
            g_play.faller_start(colm_num, faller)
        except:
            return


def board(g_play) -> None:
    '''
    Displays the game board at any situation of the game
    '''
    for row in range(g_play.get_rows()):
        rowStr = "|"
        for col in range(g_play.get_columns()):
            cellValue = g_play.get_cell_content(row, col)
            cellState = g_play.get_cell_state(row, col)
            if cellState == game.EMPTY_CELL:
                rowStr += '   '
            elif cellState == game.OCCUPIED_CELL:
                rowStr += (' ' + cellValue + ' ')
            elif cellState == game.FALLER_MOVING:
                rowStr += ('[' + cellValue + ']')
            elif cellState == game.FALLER_STOPPED:
                rowStr += ('|' + cellValue + '|')
            elif cellState == game.MATCHED_CELL:
                rowStr += ('*' + cellValue + '*')
        rowStr += '|'
        print(rowStr)

    bottom = ' '
    for col in range(g_play.get_columns()):
        bottom += '---'
    bottom += ' '
    print(bottom)

   
def size() -> int:
    '''
    Returns integer inputs for rows and colums that
    determine the size of the game board
    '''
    num = input().strip()
    return int(num)


def operation() -> str:
    '''
    Returns EMPTY or CONTENTS without any leading/trailiing whitespaces
    '''
    return input().strip()


def next_move() -> str:
    '''
    Gets the next move from the player
    '''
    return input()


if __name__ == "__main__":
    run()
