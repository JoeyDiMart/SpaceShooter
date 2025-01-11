'''
Joseph DiMartino
Pygame! combining asteroids with space invaders
'''
import pygame
import math
import random
from Laser import Laser
from Eye import Eye

pygame.init()  # initialize modules
clock = pygame.time.Clock()  # create clock object
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h  # fullscreen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)  # can change size
pygame.display.set_caption('Space Game')  # title
BG_COLOR = pygame.Color(10, 10, 10)  # bg color
#frame_counter = 0

# Cursor
custom_cursor = pygame.image.load("cursor.png").convert_alpha()
cursor_rect = custom_cursor.get_rect()
cursor_offset = (-cursor_rect.width // 2, -cursor_rect.height // 2)
pygame.mouse.set_visible(False)

jet = "yellow_jet.png"  # Replace with the path to your JPG
jet = pygame.image.load(jet).convert_alpha()
jet_width, jet_height = jet.get_size()
jet_clone = jet.copy()
jet_rect = jet.get_rect()
center_w, center_h = jet_width // 2, jet_height // 2  # how many pixels to center of jet image

lasers = []
laser = "lasers.png"
laser = pygame.image.load(laser).convert_alpha()


# jet initial position
x_position, y_position = screen_width // 2 - center_w, screen_height // 2 - center_h
jet_rect.topleft = x_position, y_position

screen.blit(jet, (x_position, y_position))  # initial jet on screen

# HUD
lives = 3
score = 0
heart_icon = pygame.image.load("heart.png")
score_font = pygame.font.Font("ARCADECLASSIC.TTF", 20)

# Enemy spawning
eye_list = []
#eye_frames = [pygame.image.load("eyes/eye0.png").convert_alpha(), pygame.image.load("eyes/eye1.png").convert_alpha(),
#              pygame.image.load("eyes/eye3.png").convert_alpha()]
eye = pygame.image.load("eyes/eye0.png").convert_alpha()
spawn_time = 80  # time in ms for each spawn


def HUD(lives, score):
    heart_pos = 20
    for i in range(lives):
        screen.blit(heart_icon, (heart_pos, screen_height-60))
        heart_pos += 70
    score_render = score_font.render(str(score), True, (255, 255, 255))
    screen.blit(score_render, (20, 10))
    return


# Subroutines for game logic
def rotateJet(x_center, y_center, x_mouse, y_mouse):
    dx, dy = x_center - x_mouse, y_center - y_mouse
    angle = math.degrees(math.atan2(-dy, dx)) + 90
    rotated_jet = pygame.transform.rotate(jet, angle)
    rotated_rect = rotated_jet.get_rect(center=jet_rect.center)
    return screen.blit(rotated_jet, rotated_rect.topleft)


def makeLaser():
    x_mouse, y_mouse = pygame.mouse.get_pos()
    x_center, y_center = jet_rect.x + center_w, jet_rect.y + center_h
    dx, dy = x_mouse - x_center, y_mouse - y_center
    angle = math.degrees(math.atan2(-dy, dx))
    rotated_laser = pygame.transform.rotate(laser, angle + 90)
    rotated_laser_rect = rotated_laser.get_rect(center=jet_rect.center)
    lasers.append(Laser(x_center, y_center, angle, rotated_laser, rotated_laser_rect))
    return


def spawnEye(jet_x, jet_y):
    eye_x, eye_y = -20, -20
    wall = random.randint(1, 4)
    if wall % 2 == 0:
        eye_x = random.randint(0, screen_width)
        if wall == 4:
            eye_y = screen_height + 20
    else:
        eye_y = random.randint(0, screen_height)
        if wall == 3:
            eye_x = screen_width + 20

    eye_rect = eye.get_rect()
    eye_rect.x, eye_rect.y = eye_x, eye_y
    dx, dy = jet_x - eye_x, jet_y - eye_y
    angle = math.degrees(math.atan2(-dy, dx))
    rotated_eye = pygame.transform.rotate(eye, angle)
    eye_rect = rotated_eye.get_rect(center=eye_rect.center)
    eye_list.append(Eye(angle, rotated_eye, eye_rect, 2))
    return


def jetMovement(x_speed, y_speed):
    jet_rect.y += y_speed
    jet_rect.x += x_speed
    if jet_rect.top <= 0:
        jet_rect.bottom = screen_height
    elif jet_rect.bottom >= screen_height:
        jet_rect.top = 0
    if jet_rect.left <= 0:
        jet_rect.right = screen_width
    elif jet_rect.right >= screen_width:
        jet_rect.left = 0
    return


def game(frame_counter=0):
    x_speed, y_speed = 0, 0
    run = True
    while run:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        frame_counter += 1
        screen.fill(BG_COLOR)
        screen.blit(custom_cursor, (mouse_x + cursor_offset[0], mouse_y + cursor_offset[1]))

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
                makeLaser()

        if frame_counter % spawn_time == 0:
            spawnEye(jet_rect.x, jet_rect.y)

        jetMovement(x_speed, y_speed)
        rotateJet(jet_rect.x + center_w, jet_rect.y + center_h, mouse_x, mouse_y)

        for l in lasers:
            l.move()
            screen.blit(l.laser, l.laser_rect)
        for e in eye_list:
            e.move()
            screen.blit(e.eye, e.eye_rect)
            if ((e.eye_rect.x > screen_width + 30) or (e.eye_rect.x < -200) or
                (e.eye_rect.y > screen_height + 30) or (e.eye_rect.y < -200)):
                e.delete()
                eye_list.remove(e)


        HUD(lives, score)
        pygame.display.flip()  # update window
        clock.tick(60)  # 60 fps


if __name__ == "__main__":
    game()



