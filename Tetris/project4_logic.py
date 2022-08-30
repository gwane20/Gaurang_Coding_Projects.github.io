#Cell States
EMPTY_CELL = 'EMPTY STATE'
FALLER_MOVING = 'FALLER_MOVING STATE'
FALLER_STOPPED = 'FALLER_STOPPED STATE'
OCCUPIED_CELL = 'OCCUPIED STATE'
MATCHED_CELL = 'MATCHED STATE'

#If a cell matches with any other cell

def state_match(state: str) -> bool:
    '''
    Returns if a given state can be matched
    '''
    return state == OCCUPIED_CELL or state == MATCHED_CELL

# Direction of actions
LEFT = -1
RIGHT = 1
DOWN = 0
DOWN_LEFT = 2

# Colors of cells
NONE = 'NONE'
EMPTY = ' '
S = 'S'
T = 'T'
V = 'V'
W = 'W'
X = 'X'
Y = 'Y'
Z = 'Z'

class Game:
    def __init__(self, rows: int, columns: int):
        '''
        Creates new gameboard with assigned number of rows and columns
        '''

        self._rows = rows
        self._columns = columns
        self._boardRows = []
        self._boardStates = []
        self.faller = Faller()
        for i in range(rows):
            row_info = []
            row_state = []
            for j in range(columns):
                row_info.append(EMPTY)
                row_state.append(EMPTY_CELL)
            self._boardRows.append(row_info)
            self._boardStates.append(row_state)

    def board_info(self, content: [[str]]) -> None:
        '''
        Adds info to the board as suggested by the player
        '''
        for row in range(self.get_rows()):
            for col in range(self.get_columns()):
                 val = content[row][col]
                 if val is EMPTY:
                    self.set_cell(row, col, EMPTY, EMPTY_CELL)
                 else:
                    self.set_cell(row, col, val, OCCUPIED_CELL)

        self.faller_gravity()
        self.match()

    def count(self) -> bool:
        '''
        Counts one time unit, makes faller move and find matching color as well
        True if faller runs out of space
        '''
        if self.faller.active:
            if self.faller.state == _FALLER_STOPPED:
                self.update_faller_state()

                if self.faller.state == _FALLER_STOPPED:
                    result = False

                    if self.faller.get_row() - 2 < 0:
                        result = True

                    for i in range(3):
                        self.set_cell(self.faller.get_row() - i, self.faller.get_col(), self.faller.contents[i], OCCUPIED_CELL)

                    self.faller.active = False

                    self.match()
                    return result

            self.move_faller_down()
            self.update_faller_state()

        self.match()

        return False


    def faller_check(self) -> bool:
        '''
        Checks if the game state has an active faller or not
        '''

        return self.faller.active


    def faller_start(self, column: int, faller: [str, str, str]) -> None:
        '''
        Initiates a faller in the given column
        '''
        if self.faller.active:
            return

        self.faller.active = True
        self.faller.contents = faller
        self.faller.set_row(0)
        self.faller.set_col(column - 1)
        self.set_cell(0, self.faller.get_col(), self.faller.contents[0], FALLER_MOVING)

        self.update_faller_state()
    

    def move_faller_down(self) -> None:
        '''
        Moves faller down by one step
        '''
        if self.solid_base(self.faller.get_row() + 1, self.faller.get_col()):
            return

        self.move_cell(self.faller.get_row(), self.faller.get_col(), DOWN)

        if self.faller.get_row() - 1 >= 0:
            self.move_cell(self.faller.get_row() - 1, self.faller.get_col(), DOWN)
            if self.faller.get_row() - 2 >= 0:
                    self.move_cell(self.faller.get_row() - 2, self.faller.get_col(), DOWN)
            else:
                self.set_cell(self.faller.get_row() - 1, self.faller.get_col(), self.faller.contents[2], FALLER_MOVING)
        else:
            self.set_cell(self.faller.get_row(), self.faller.get_col(), self.faller.contents[1], FALLER_MOVING)

        self.faller.set_row(self.faller.get_row() + 1)
    

    def faller_rotation(self) -> None:
        '''
        Rotates the faller in a way that the first eelment becomes the last and second element becomes the first
        '''
        if not self.faller.active:
            return
        color1 = self.faller.contents[0]
        color2 = self.faller.contents[1]
        color3 = self.faller.contents[2]

        self.faller.contents = [color2, color3, color1]

        for i in range(3):
            self.set_cell_content(self.faller.get_row() - i, self.faller.get_col(), self.faller.contents[i])

        self.update_faller_state()


    def faller_gravity(self) -> None:
        '''
        Keeps the character moving until the cell below them is solid
        '''
        for col in range(self.get_columns()):
            for row in range(self.get_rows() - 1, -1, -1):
                state = self.get_cell_state(row, col)

                if state == FALLER_MOVING or state == FALLER_STOPPED:
                    continue
                if state == OCCUPIED_CELL:
                    i = 1

                    while not self.solid_base(row + i, col):
                        self.move_cell(row + i - 1, col, DOWN)
                        i += 1                
                

    def move_faller_side(self, direction: int) -> None:
        '''
        Moves the faller in the given direction
        '''
        if not self.faller.active:
            return
        
        if not direction == RIGHT and not direction == LEFT:
            return

        if (direction == LEFT and self.faller.get_col() == 0) or (
                direction == RIGHT and self.faller.get_col() == self.get_columns() - 1):
            return

        col_target = self.faller.get_col() + direction

        for i in range(3):
            if self.faller.get_row() - i < 0:
                break

            if self.get_cell_state(self.faller.get_row() - i, col_target) == OCCUPIED_CELL:
                return

        for i in range(3):
            if self.faller.get_row() - i < 0:
                break

            self.move_cell(self.faller.get_row() - i, self.faller.get_col(), direction)

        self.faller.set_col(col_target)

        self.update_faller_state()


    def update_faller_state(self) -> None:
        '''
        updtaes the faller's state according to the current condition
        '''
        state = None
        row_target = self.faller.get_row() + 1
        if self.solid_base(row_target, self.faller.get_col()):
            state = FALLER_STOPPED
            self.faller.state = _FALLER_STOPPED
        else:
            state = FALLER_MOVING
            self.faller.state = _FALLER_MOVING
        for i in range(3):
            row = self.faller.get_row() - i
            if row < 0:
                return
            self.set_cell(row, self.faller.get_col(), self.faller.contents[i], state)

    def get_rows(self) -> int:
        '''Returns the number of rows'''
        return self._rows
    

    def get_columns(self) -> int:
        '''Returns the number of columns'''
        return self._columns

    
    def get_cell_state(self, row: int, col: int) -> str:
        '''Identifies cell state based on row and column'''
        return self._boardStates[row][col]
    

    def get_cell_content(self, row: int, col: int) -> str:
        '''Gets the content of the identified cell'''
        return self._boardRows[row][col]

    
    def set_cell(self, row: int, col: int, contents: str, state: str) -> None:
        '''Sets the content and state of cell identified by row and column'''
        if row < 0:
            return
        self.set_cell_content(row, col, contents)
        self.set_cell_state(row, col, state)

        
    def set_cell_content(self, row: int, col: int, contents: str) -> None:
        '''Sets the content of the identified cell'''
        if row < 0:
            return
        self._boardRows[row][col] = contents

        
    def set_cell_state(self, row: int, col: int, state: str) -> None:
        '''Sets the state of the identified cell'''
        if row < 0:
            return
        self._boardStates[row][col] = state
        
    
    def match(self) -> None:
        '''
        If cells are already matching then they are destroyed and the other elements move down into their place
        '''
        for row in range(self.get_rows()):
            for col in range(self.get_columns()):
                if self.get_cell_state(row, col) == MATCHED_CELL:
                    self.set_cell(row, col, EMPTY, EMPTY_CELL)

        self.faller_gravity()

        self.x_axis_match()
        self.y_axis_match()
        self.diagonal_match()

    def x_axis_match(self) -> None:
        '''Checks for matches on the x-axis, i.e., horizontally'''
        for row in range(self.get_rows() - 1, -1, -1):
            num_match = 0
            color = NONE
            for col in range(0, self.get_columns()):
                contents = self.get_cell_content(row, col)
                gamestate = self.get_cell_state(row, col)
                cellMatch = (contents == color and state_match(gamestate))
                if cellMatch:
                    num_match += 1

                if col == self.get_columns()-1:
                    if num_match >= 3:
                        if cellMatch:
                            self.matched_cells(row, col, LEFT, num_match)
                        else:
                            self.matched_cells(row, col-1, LEFT, num_match)
                elif not cellMatch:
                    if num_match >= 3:
                        self.matched_cells(row, col-1, LEFT, num_match)

                    if state_match(gamestate):
                        color = contents
                        num_match = 1
                    
                    else:
                        color = NONE
                        num_match = 1
                
                
        
    def y_axis_match(self) -> None:
        '''Checks for matches on the y-axis, i.e., vertically'''
        for col in range(0, self.get_columns()):
            num_match = 0
            color = NONE
            for row in range(self.get_rows() - 1, -1, -1):
                contents = self.get_cell_content(row, col)
                gamestate = self.get_cell_state(row, col)
                cellMatch = (contents == color and state_match(gamestate))

                if cellMatch:
                    num_match += 1

                if row == 0:
                    if num_match >= 3:
                        if cellMatch:
                            self.matched_cells(row, col, DOWN, num_match)
                        else:
                            self.matched_cells(row + 1, col, DOWN, num_match)

                elif not cellMatch:
                    if num_match >= 3:
                        self.matched_cells(row + 1, col, DOWN, num_match)

                    if state_match(gamestate):
                        color = contents
                        num_match = 1
                    else:
                        color = NONE
                        num_match = 1
        
    def diagonal_match(self) -> None:
        '''Checks for matches on the diagonal-axis'''
        for currentRow in range(self.get_rows() - 1, -1, -1):
            for currentCol in range(0, self.get_columns()):
                matches = 0
                color = NONE
                rowCount = 0
                colCount = 0
                while True:
                    row = currentRow - rowCount
                    col = currentCol + colCount

                    contents = self.get_cell_content(row, col)
                    state = self.get_cell_state(row, col)
                    cellMatches = (contents == color and state_match(state))
                    # This cell matches our current sequence
                    if cellMatches:
                        matches += 1

                    # This is the last column so we have to terminate the matching for this row
                    if col == self.get_columns()-1 or row == 0:
                        if matches >= 3:
                            if cellMatches:
                                self.matched_cells(row, col, DOWN_LEFT, matches)
                            else:
                                self.matched_cells(row + 1, col - 1, DOWN_LEFT, matches)
                    elif not cellMatches:
                        if matches >= 3:
                            self.matched_cells(row + 1, col - 1, DOWN_LEFT, matches)

                        if state_match(state):
                            color = contents
                            matches = 1
                        else:
                            color = NONE
                            matches = 1

                    rowCount += 1
                    colCount += 1

                    if currentRow-rowCount < 0 or currentCol+colCount >= self.get_columns():
                        break
        
    def matched_cells(self, row: int, col: int, direction: int, amount: int) -> None:
        '''Marks the cells as matching cells in any given direction'''
        if direction == LEFT:
            for col_target in range(col, col - amount, -1):
                self.set_cell_state(row, col_target, MATCHED_CELL)
        elif direction == DOWN:
            for row_target in range(row, row + amount):
                self.set_cell_state(row_target, col, MATCHED_CELL)
        elif direction == DOWN_LEFT:
            for i in range(amount):
                self.set_cell_state(row + i, col - i, MATCHED_CELL)
        
    def solid_base(self, row: int, col: int) -> bool:
        '''
        Checks if a cell is solid
        '''
        if row >= self.get_rows():
            return True

        if self.get_cell_state(row, col) == OCCUPIED_CELL:
            return True
 

        
    def move_cell(self, row: int, col: int, direction: int) -> None:
        '''
        Moves cells in assigned directions
        '''
        value = self._boardRows[row][col]
        state = self._boardStates[row][col]
        self._boardRows[row][col] = EMPTY
        self._boardStates[row][col] = EMPTY_CELL

        if direction == DOWN:
            row_target = row + 1
            self._boardRows[row_target][col] = value
            self._boardStates[row_target][col] = state
        else:
            col_target = col + direction
            self._boardRows[row][col_target] = value
            self._boardStates[row][col_target] = state



        
_FALLER_STOPPED = 0
_FALLER_MOVING = 1


class Faller:
    def __init__(self):
        """
        Constructs a new faller object
        """
        self.active = False
        self._row = 0
        self._col = 0
        self.contents = [EMPTY, EMPTY, EMPTY]
        self.state = FALLER_MOVING

    def get_row(self) -> int:
        """
        Gets the row value for the faller
        """
        return self._row

    def get_col(self) -> int:
        """
        Gets the column value for the faller
        """
        return self._col

    def set_row(self, row: int) -> None:
        """
        Sets the row value for the faller
        """
        self._row = row

    def set_col(self, col: int) -> None:
        """
        Sets the column value for this faller
        """
        self._col = col
                
