import pygame
from TileLoader import Tile_Loader
import spritesheet
pygame.init()


class Power_Up():
    """ Class for power up """
    def __init__(self):
        """ Set base variables and load image """
        self.filename_power_up = "images/power_up_EDIT_2.png"
        self.rect_x = 32
        self.rect_y = 32
        self.power_up_x = 704
        self.power_up_y = 416
        self.frame = 0

        self.power_up = pygame.image.load("images/Single power up.png") # load image
        
        self.rect = pygame.Rect(self.power_up_x, self.power_up_y, self.rect_x, self.rect_y) # set rectangle
        
        
    def update(self, world_shift):
        """ Updates position """
        self.power_up_x + world_shift
        self.rect = pygame.Rect(self.power_up_x + world_shift, self.power_up_y, self.rect_x, self.rect_y)
        
        
    def draw(self, screen):
        """ Blits image onto screen  """
        screen.blit(self.power_up, self.rect)
        
        
class Level_One():
    """ Class for Level One and its methods """
    def __init__(self, player):
        """ Sets base variables for map and creates map layout """
        self.level = [[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  3, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9, 12, 12, 12, 12, 12, 12, 12,  3, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  3, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11,  8,  8,  8,  8, 10, 12, 12, 12, 12, 12, 12, 11,  8,  8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11,  8,  8, 10, 12, 12, 12, 12, 12, 12, 12, 12, 11,  8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12, 12, 12, 12, 12, 12, 12],
                      [12,  5,  6,  6,  6,  4, 12, 12, 12, 12, 12, 12, 12, 12, 12,  8,  8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  8,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  8,  8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  8,  8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  9,  9,  9, 12, 12,  8,  8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  8,  8,  8, 12, 12,  8,  8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  8,  8,  8, 12, 12,  8,  8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  8,  8,  8, 12, 12,  8,  8, 12, 12, 12, 12, 12,  9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [ 1,  1,  1,  1,  1,  1,  1, 12, 12, 12,  8,  8,  8,  0,  0,  8,  8,  9,  9,  9,  9,  9,  8,  9,  9,  9,  9,  9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                      [ 2,  2,  2,  2,  2,  2,  2,  0,  0,  0,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  8,  9,  0,  0,  9,  0,  0,  9,  0,  0,  0,  9,  9,  9,  9,  9,  9,  9,  9],
                      ]
        self.filename_background = "images/background_tilesheet_EDIT_3.png" # tile sheet
        self.rect_x = 32
        self.rect_y = 32
        self.total_row = 17
        self.total_column = 46
        self.block_list = pygame.sprite.Group()
        
        self.heart = pygame.image.load("images/life_heart_EDIT_1.png") # life heart
        self.life_rect = pygame.Rect(5, 5, 16, 16)
    
            
    def create_level(self, screen):
        """ Cycles through array and places block according to value """        
        for row in range(self.total_row): # row in grid
            for column in range(self.total_column): # column in grid
                if not self.level[row][column] == 12: # if block number isn't 13
                    tile = Tile_Loader(self.rect_x, self.rect_y) # Create tile
                    block = self.level[row][column] # Gets value of block  
                    self.block_list.add(tile) # list of blocks
                    tile.get_place_image(block, screen, row, column) # Puts image onto screen
                    
        for increment in range(3): # places hearts onto screen
            screen.blit(self.heart, self.life_rect)
            self.life_rect.x += 21
            
        self.life_rect.x = 5


                    

                    
        