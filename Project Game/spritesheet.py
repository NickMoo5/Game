
 
import pygame

# create a spritesheet class that will have it's own functions
class spritesheet(object):
    def __init__(self, filename):
        ''' initialize itself '''
        try: # fail if the spritesheet.png file isn't found
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            print ('Unable to load spritesheet image:'), filename
            raise SystemExit
        
    def image_at(self, rectangle, colorkey = None):
        """ Loads spritesheet image from x,y,x+offset,y+offset"""
        # The colorkey is the color contained in the
        # upper left pixel of the image.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    
    def images_at(self, rects, colorkey = None):
        ''' Load a whole bunch of images and return them as a list ''' 
        return [self.image_at(rect, colorkey) for rect in rects]
    
    def load_strip(self, rect, image_count, colorkey = None):
        ''' Loads a strip of images and returns them as a list '''
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)