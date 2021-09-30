import spritesheet, pygame
 
class SpriteStripAnim(object):
    """ sprite strip animator
    This class provides an iterator (iter(), next(), and stop(), methods), 
    and a __add__() method for joining strips """
    
    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
        """construct a SpriteStripAnim
        """
        #-- Class Globals --#
        """ self is the SpriteStripAnim class """
        self.filename = filename
        ss = spritesheet.spritesheet(filename) # spritesheet.py module method
        self.images = ss.load_strip(rect, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
        
        #-- Class Methods --#
    def iter(self):
        """ advances to the next image """
        self.i = 0
        self.f = self.frames
        return self
    
    def next(self):
        """ returns the next image from the spritesheet """

        clock = pygame.time.Clock() 
        clock.tick(60)
        if self.i >= len(self.images):
            if not self.loop: #loop is a boolean
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image
    
    def stop(self):
        """ lands on the first image of the spritesheet
         """
        self.i = 1
        image = self.images[self.i]
        return image
    
    def __add__(self, ss):
        """ allows you to join strips.  """
        self.images.extend(ss.images)
        return self

