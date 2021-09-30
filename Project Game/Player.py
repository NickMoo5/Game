import pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    """ Class for player and its methods """
    
    def __init__(self):
        """ Sets base variables and loads sprite images """
        super().__init__()
        
        self.rect_x = 52
        self.rect_y = 64
        
        self.rect = pygame.Rect(0, 0, self.rect_x, self.rect_y) # player rectangle
        
        self.walking_l = [] # list for walk cycle
        self.walking_r = [] # list for walk cycle
        
        self.change_x = 0
        self.change_y = 0
        
        self.direction = "R" # Direction player is facing
        
        # right facing walk pictures
        image = pygame.image.load("images/sprite_images/sprite_1.png")
        self.walking_r.append(image)
        image = pygame.image.load("images/sprite_images/sprite_2.png")
        self.walking_r.append(image)
        image = pygame.image.load("images/sprite_images/sprite_3.png")
        self.walking_r.append(image)
        image = pygame.image.load("images/sprite_images/sprite_4.png")
        self.walking_r.append(image)   
        
        # standing left and right picture
        self.standing_r = pygame.image.load("images/sprite_images/sprite_5.png")
        self.standing_l = pygame.image.load("images/sprite_images/sprite_5.png")
        self.standing_l = pygame.transform.flip(self.standing_l, True, False)
        
        # left facing walk pictures
        image = pygame.image.load("images/sprite_images/sprite_1.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_l.append(image)
        image = pygame.image.load("images/sprite_images/sprite_2.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_l.append(image)
        image = pygame.image.load("images/sprite_images/sprite_3.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_l.append(image)
        image = pygame.image.load("images/sprite_images/sprite_4.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_l.append(image)    
        
        # jumping pictures
        self.jumping_r = pygame.image.load("images/sprite_images/sprite_6.png")
        self.jumping_l = pygame.image.load("images/sprite_images/sprite_6.png")
        self.jumping_l = pygame.transform.flip(self.jumping_l, True, False)
        
        self.frame = 0 # frame of cycle
        
        self.image = self.walking_r[self.frame] # sets current image
        
        self.standing = 0 # counter for standing timing animation
        
        self.level = None 
        
        
    def update(self):
        """ Updates position, current image, collison detection of player """
        self.gravity()
        
        self.rect.x += self.change_x # Move along_x
        
        if self.direction == "R":
            self.frame += 1 # increases frame in right cycle
            if self.frame == 4:
                self.frame = 0
            self.image = self.walking_r[self.frame]
        else:
            self.frame += 1 # increases frame in left cycle
            if self.frame == 4:
                self.frame = 0
            self.image = self.walking_l[self.frame]  
        
        if self.change_x == 0: # if standing still bob head 
            if self.direction == "R": # right
                if self.standing <= 3: # counter
                    self.image = self.standing_r # up position
                else:
                    self.image = self.walking_r[0] # down position
            else: # Left
                if self.standing <= 3:
                    self.image = self.standing_l
                else:
                    self.image = self.walking_l[0]
                    
            if self.standing == 6: # resets counter
                self.standing = 0
            else: 
                self.standing += 1
                
        block_hit_list = pygame.sprite.spritecollide(self, self.level.block_list, False) # collison detection with map
        for block in block_hit_list:
            
            if self.change_x > 0: # x axis blocks
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
                                                      
        self.rect.y += self.change_y # move up/down
        
        block_hit_list = pygame.sprite.spritecollide(self, self.level.block_list, False) # collison detection with map
        for block in block_hit_list:
            
            if self.change_y > 0: # y axis blocks
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            
            self.change_y = 0 # stop up/down movement 
            
        if self.rect.x <= 0:
            self.change_x = 0
            self.rect.x = 0

                
    def gravity(self):
        """ Applies affect of gravity and when to stop """
        if self.change_y == 0: # if not moving up/down start falling
            self.change_y = 20
        else:
            self.change_y += .85 # affect of gravity
            
        block_hit_list = pygame.sprite.spritecollide(self, self.level.block_list, False) # collision detection
        for block in block_hit_list:
            
            if self.change_y > 0: # y axis blocks
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                        
            self.change_y = 0 # stop falling
            
            
    def jump(self):    
        """ Checks to see if on solid ground and jumps """
        self.rect.y += 2
        block_hit_list = pygame.sprite.spritecollide(self, self.level.block_list, False) # detects if on ground
        self.rect.y -= 2
        
        if len(block_hit_list):
            self.change_y += -15
            if self.direction == "R":
                self.image = self.jumping_r
            else:
                self.image = self.jumping_l
                
                                         
    def draw(self, screen):
        """ Blits image at rectangle location """
        screen.blit(self.image, self.rect)
    
    
    def left(self):
        """ Move left """
        self.change_x = -8
        self.direction = "L"
        self.frame = 0
        
        
    def right(self):
        """ Move Right """
        self.change_x = 8
        self.direction = "R"
        self.frame = 0
        
        
    def stop(self):
        """ stop moving """
        self.change_x = 0
        
