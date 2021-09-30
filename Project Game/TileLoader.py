import pygame
import spritesheet

pygame.init()

class Tile_Loader(pygame.sprite.Sprite):
    """ Loads and places tiles at a grid location """
    
    def __init__(self, rect_x, rect_y):
        """ Sets base variables for tiles """
        super().__init__()
        ss = spritesheet.spritesheet("images/background_tilesheet_EDIT_3.png") # loads spritesheet
        self.sheet = ss
        self.rect_x = rect_x 
        self.rect_y = rect_y
        self.rect = pygame.Rect(0, 0, self.rect_x, self.rect_y) # rectangle and location

        
    def get_place_image(self, block, surface, row, column):
        """ Gets image from sprite sheet and sets rectangle location for image """
        tile = self.sheet.image_at([block * self.rect_x, 0, self.rect_x, self.rect_y]) # gets image
        
        self.rect.x = (column * self.rect_x)  # sets x location of rectangle
        self.rect.y = row * self.rect_y # sets y location of rectangle

        self.draw(surface, tile)
    
    
    def draw(self, surface, tile):
        """ Blits tile onto rectangle """
        surface.blit(tile, self.rect)
        
      
        
        
        
        

