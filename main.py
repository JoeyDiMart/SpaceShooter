'''
Joseph DiMartino
Pygame! combining asteroids with space invaders
'''
import pygame

pygame.init() # initialize modules

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h # fullscreen

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE) # can change size

pygame.display.set_caption('Space Shooter')
