'''
eye.png animations
'''
import math
import pygame

class Eye:
    #num = 0
    def __init__(self, angle, eye, eye_rect, health):
        self.angle = angle
        self.speed = 6.5
        self.dx = self.speed * math.cos(math.radians(self.angle))
        self.dy = self.speed * math.sin(math.radians(self.angle))
        self.eye = eye
        self.eye_rect = eye_rect
        self.health = health

    def move(self):
        self.eye_rect.x += self.dx
        self.eye_rect.y -= self.dy


    def killAnimation(self):
        pass

    def rotatePhoto(self):
        pass

    def delete(self):
        self.angle = self.speed = self.dx = self.dy = self.eye = self.eye_rect = self.health = None

    def loseHealth(self):
        self.health -= 1

