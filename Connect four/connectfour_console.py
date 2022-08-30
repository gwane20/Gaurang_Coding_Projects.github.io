"""
    Cong Khang Le (ID: 27444345)
    Gaurang Wanere (ID: 58573754)
"""

import connectfour
import connectfour_library as library

def startGame() -> None:
    """Starts the game and all other functions of the game"""
    print('ICS 32 Connect Four')
    state = connectfour.new_game()
    while connectfour.winner(state) == connectfour.NONE:
        print()
        library.print_gamestate(state)
        library.print_turn(state)
        turn = False
        while turn is False:
            col, choice = library.get_move()
            try:
                state = library.execute_move(state, col, choice)
                turn = True
            except:
                if choice == 'DROP':
                    print('Can\'t drop in this column')
                elif choice == 'POP':
                    print('Can\'t pop in this column')
    winner = connectfour.winner(state)
    print()
    library.print_gamestate(state)
    print(library.get_name(winner), 'has won the game!')

    

if __name__ == '__main__':
    startGame()
