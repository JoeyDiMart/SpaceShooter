'''
Joseph DiMartino
Pygame! combining asteroids with space invaders
'''
import pygame

pygame.init() # initialize modules
clock = pygame.time.Clock() # create clock object

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h # fullscreen

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE) # can change size

pygame.display.set_caption('Space Shooter') # title

BG_COLOR = pygame.Color(10, 10, 10) # bg color

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check for X out of game
            run = False
    screen.fill(BG_COLOR)
    pygame.display.flip()  # update window
    clock.tick(60)  # 60 fps




