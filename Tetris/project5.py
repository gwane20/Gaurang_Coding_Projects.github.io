'''
Gaurang Wanere
58573754
'''

import project4_logic as game
import pygame
import random

rows = 13
cols = 6
ref_speed = 12 # 12 frames per second

jewels = ['S', 'T', 'V', 'W', 'X', 'Y', 'Z']


def color(jewels: str) -> (int, int, int):
    ''' Assigns colors to jewels '''

    if jewels == 'S': # Sea Green
        return (46, 139, 87)
    elif jewels == 'T': # Tangerine
        return (242, 133, 0)
    elif jewels == 'V': # Violet
        return (238, 130, 238)
    elif jewels == 'W': # Wild Orchid
        return (212, 112, 162)
    elif jewels == 'X': # Xanadu
        return (115, 134, 120)
    elif jewels == 'Y': # Sea Green
        return (255, 255, 0)
    elif jewels == 'Z': # Zaffre
        return (0, 20, 168)

class Game_State:

    def __init__(self):
        ''' Assigns fields with default values'''

        self._state = game.Game(rows, cols)
        self._ticker = ref_speed
        self._running = True

        self._backgroundColor = pygame.Color(0, 0, 0) # Black background
        self._jewelColor = pygame.Color(208, 240, 192) # Tea Green

        self._bufferY = 0.04
        self._size = (1.0 - self._bufferY) / self._state.get_rows()
        self._bufferX = (1.0 - (self._size * self._state.get_columns()))


    def game_starting(self) -> None:
        ''' Starts the game '''

        pygame.init()

        try:
            clock = pygame.time.Clock()

            self.create_surface((600, 600))
            
            while self._running:
                clock.tick(ref_speed)

                self.handle_events()

                self._ticker -= 1

                if self._ticker == 0:
                    self.ticker_game()
                    self._ticker = ref_speed

                self.draw_frame()

        finally:
            pygame.quit()


    def ticker_game(self) -> None:
        ''' Ticks teh state of the game, i.e, duration of the game'''

        self._running = not self._state.count()

        if not self._state.faller_check():
            content = random.sample(jewels, 3)
            column = random.randint(1, cols)
            self._state.faller_start(column, content)


    def create_surface(self, size: (int, int)) -> None:
        ''' Generates game board to play on '''

        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)


    def draw_frame(self) -> None:
        ''' Draws a frame for the game screen '''
        
        self._surface.fill(self._backgroundColor)
        self.draw_game_objects()
        pygame.display.flip()

        
    def handle_events(self) -> None:
        ''' Manages events from pygame '''

        for event in pygame.event.get():
            self._handle_event(event)

        self.key_presses()
        
        
    def _handle_event(self, event: pygame.event.EventType) -> None:
        ''' Handles the QUIT and VIDEORESIZE event from pygame '''

        if event.type == pygame.QUIT:
            self.stop_running()
        elif event.type == pygame.VIDEORESIZE:
            self.create_surface(event.size)


    def key_presses(self) -> None:
        ''' Handles inputs from the player '''

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self._state.move_faller_side(game.LEFT)

        if keys[pygame.K_RIGHT]:
            self._state.move_faller_side(game.RIGHT)

        if keys[pygame.K_SPACE]:
            self._state.faller_rotation()

            

    def draw_game_objects(self) -> None:
        ''' Draws all game objects and states '''
        topleftX = self.frac_x_to_pixel_x((self._bufferX / 2))
        topleftY = self.frac_y_to_pixel_y((self._bufferY / 2))

        width = self.frac_x_to_pixel_x((self._size * self._state.get_columns()) - 0.001)
        height = self.frac_y_to_pixel_y((self._size * self._state.get_rows()))

        # Draws outline box 
        outlineRect = pygame.Rect(topleftX, topleftY, width, height)
        pygame.draw.rect(self._surface, self._jewelColor, outlineRect, 0)

        # Draws individual jewels
        for row in range(self._state.get_rows()):
            for col in range(self._state.get_columns()):
                self.draw_jewel(row, col)


    def draw_jewel(self, row: int, col: int) -> None:
        ''' Draws a jewel and its state '''

        jewel = self._state.get_cell_content(row, col)
        if jewel is game.EMPTY:
            return

        rawColor = None
        state = self._state.get_cell_state(row, col)
        if state == game.MATCHED_CELL:
            rawColor = (255, 255, 255)
        else:
            rawColor = color(jewel)
        colors = pygame.Color(rawColor[0], rawColor[1], rawColor[2])

        jewelX = (col * self._size) + (self._bufferX / 2)
        jewelY = (row * self._size) + (self._bufferY / 2)

        topleftX = self.frac_x_to_pixel_x(jewelX)
        topleftY = self.frac_y_to_pixel_y(jewelY)

        width = self.frac_x_to_pixel_x(self._size)
        height = self.frac_y_to_pixel_y(self._size)

        rect = pygame.Rect(topleftX, topleftY, width, height)

        pygame.draw.rect(self._surface, colors, rect, 0)

        if state == game.FALLER_STOPPED:
            pygame.draw.rect(self._surface, pygame.Color(255, 255, 255), rect, 2)


    def frac_x_to_pixel_x(self, frac_x: float) -> int:
        ''' Converts fractional x value to pixel value'''

        return self.frac_to_pixel(frac_x, self._surface.get_width())


    def frac_y_to_pixel_y(self, frac_y: float) -> int:
        ''' Converts fractional y value to pixel value'''
        return self.frac_to_pixel(frac_y, self._surface.get_height())


    def frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        ''' Converts fractional value to integer value fromm given max pixel value'''

        return int(frac * max_pixel)


    def stop_running(self) -> None:
        ''' Game exits on the next frame after the function is called '''

        self._running = False


if __name__ == '__main__':
    Game_State().game_starting()

        

        
    
