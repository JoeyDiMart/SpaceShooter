'''
figure out how to make the ship follow the cursor
'''

import pygame
import math

pygame.init()  # initialize modules
clock = pygame.time.Clock()  # create clock object
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h  # fullscreen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)  # can change size
pygame.display.set_caption('Rotation Testing')  # title
BG_COLOR = pygame.Color(10, 10, 10)  # bg color

jet = "yellow_jet.png"  # Replace with the path to your JPG
jet = pygame.image.load(jet).convert_alpha()
jet_width, jet_height = jet.get_size()
jet_rect = jet.get_rect()
center_w, center_h = jet_width // 2, jet_height // 2  # how many pixels to center of jet image


# jet initial position
x_position, y_position = screen_width // 2 - center_w, screen_height // 2 - center_h

screen.blit(jet, (x_position, y_position))  # initial jet on screen


# method to rotate jet from its center
def rotateJet(x_center, y_center):
    x_mouse, y_mouse = pygame.mouse.get_pos()
    dx, dy = x_center - x_mouse, y_center - y_mouse
    angle = math.degrees(math.atan2(-dy, dx)) + 90
    rotated_jet = pygame.transform.rotate(jet, angle)
    rotated_rect = rotated_jet.get_rect(center=jet_rect.center)
    return screen.blit(rotated_jet, rotated_rect.topleft)


def game():
    run = True
    while run:
        screen.fill(BG_COLOR)

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check for X out of game
                run = False

        jet_rect.topleft = (x_position, y_position)
        rotateJet(jet_rect.x + center_w, jet_rect.y + center_h)

        pygame.display.flip()  # update window
        clock.tick(60)  # 60 fps


if __name__ == "__main__":
    game()




