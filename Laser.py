'''
Class creating laser objects
'''
import math


class Laser:
    def __init__(self, x, y, angle, laser, laser_rect):
        self.x = laser_rect.x
        self.y = laser_rect.y
        self.angle = angle
        self.speed = 10
        self.dx = self.speed * math.cos(math.radians(self.angle))
        self.dy = self.speed * math.sin(math.radians(self.angle))
        self.laser = laser
        self.laser_rect = laser_rect

    def move(self):
        self.laser_rect.x += self.dx
        self.laser_rect.y -= self.dy

    def delete(self):
        self.x = self.y = self.angle = self.speed = self.dx = self.dy = self.laser = self.laser_rect = None




