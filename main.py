'''
Joseph DiMartino
Pygame! combining asteroids with space invaders
'''
import pygame
import math
from Laser import Laser

pygame.init()  # initialize modules
clock = pygame.time.Clock()  # create clock object
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h  # fullscreen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)  # can change size
pygame.display.set_caption('Space Game')  # title
BG_COLOR = pygame.Color(10, 10, 10)  # bg color

jet = "yellow_jet.png"  # Replace with the path to your JPG
jet = pygame.image.load(jet).convert_alpha()
jet_width, jet_height = jet.get_size()
jet_rect = jet.get_rect()
center_w, center_h = jet_width // 2, jet_height // 2  # how many pixels to center of jet image

lasers = []
laser = "lasers.png"
laser = pygame.image.load(laser).convert_alpha()


# jet initial position
x_position, y_position = screen_width // 2 - center_w, screen_height // 2 - center_h
jet_rect.topleft = x_position, y_position

screen.blit(jet, (x_position, y_position))  # initial jet on screen


# Subroutines for game logic
def rotateJet(x_center, y_center):
    x_mouse, y_mouse = pygame.mouse.get_pos()
    dx, dy = x_center - x_mouse, y_center - y_mouse
    angle = math.degrees(math.atan2(-dy, dx)) + 90
    rotated_jet = pygame.transform.rotate(jet, angle)
    rotated_rect = rotated_jet.get_rect(center=jet_rect.center)
    return screen.blit(rotated_jet, rotated_rect.topleft)

def jetMovement(x_speed, y_speed):
    jet_rect.y += y_speed
    jet_rect.x += x_speed
    if jet_rect.top <= 0:
        jet_rect.top = 0
    elif jet_rect.bottom >= screen_height:
        jet_rect.bottom = screen_height
    if jet_rect.left <= 0:
        jet_rect.left = 0
    elif jet_rect.right >= screen_width:
        jet_rect.right = screen_width

def game():
    x_speed, y_speed = 0, 0
    run = True
    while run:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check for X out of game
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_speed -= 5
                if event.key == pygame.K_s:
                    y_speed += 5
                if event.key == pygame.K_a:
                    x_speed -= 5
                if event.key == pygame.K_d:
                    x_speed += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    y_speed += 5
                if event.key == pygame.K_s:
                    y_speed -= 5
                if event.key == pygame.K_a:
                    x_speed += 5
                if event.key == pygame.K_d:
                    x_speed -= 5
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left-click
                x_mouse, y_mouse = pygame.mouse.get_pos()
                x_center, y_center = jet_rect.x + center_w, jet_rect.y + center_h
                dx, dy = x_mouse - x_center, y_mouse - y_center
                angle = math.degrees(math.atan2(-dy, dx))
                rotated_laser = pygame.transform.rotate(laser, angle+90)
                rotated_laser_rect = rotated_laser.get_rect(center=jet_rect.center)
                lasers.append(Laser(x_center, y_center, angle, rotated_laser, rotated_laser_rect))

        jetMovement(x_speed, y_speed)
        rotateJet(jet_rect.x + center_w, jet_rect.y + center_h)
        for l in lasers:
            l.move()
            screen.blit(l.laser, l.laser_rect)

        pygame.display.flip()  # update window
        clock.tick(60)  # 60 fps


if __name__ == "__main__":
    game()



