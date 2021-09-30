import pygame
pygame.init()
from Maps import Level_One
from Maps import Power_Up
from Player import Player


def main():
    """ Sets screen and window, sets map grid, runs Main Loop """
    # Color
    BACKGROUND_BLUE = (107, 187, 233)
    
    # Set screen and window 
    size = (800, 544)
    screen = pygame.display.set_mode(size)
    windowSurface = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption("Ninja!")
    
    my_player = Player() # create player
    
    create = Level_One(my_player) # generate map
    
    my_player.level = create # give player current level lists
    my_player.rect.y = 416 # starting position
    
    sprite_list = pygame.sprite.Group()
       
    sprite_list.add(my_player)  # Add to group 
        
    run_program = True
    clock = pygame.time.Clock()        
    
    # Main Loop
    while run_program:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_program = False
                    
            pygame.key.set_repeat(0, 6000) # player controls
            key = pygame.key.get_pressed()
            
            if key[pygame.K_LEFT]:
                my_player.left()
            elif key[pygame.K_RIGHT]:
                my_player.right()
            elif key[pygame.K_UP]:
                my_player.jump()
            else:
                my_player.stop() 
                
        screen.fill(BACKGROUND_BLUE)  # background color 
        create.create_level(screen) # update level
                               
        power_up = Power_Up() # create power up
                
        power_up.draw(screen) # draw power up
        
        sprite_list.update() # update 
        
        sprite_list.draw(screen) # draw   
                    
        pygame.display.update() # update display                      
                    
        clock.tick(60)  
     
    pygame.quit()    
    
main()  