'''
eye.png animations
'''


class Eye:
    def __init__(self, x, y, angle, eye, eye_rect, health):
        self.x = eye_rect.x
        self.y = eye_rect.y
        #self.angle = angle
        self.speed = 7
        #self.dx = self.speed * math.cos(math.radians(self.angle))
        #self.dy = self.speed * math.sin(math.radians(self.angle))
        self.eye = eye
        self.eye_rect = eye_rect
        self.health = health

    #def move(self):
    #    self.eye_rect.x += self.dx
    #    self.eyer_rect.y -= self.dy

    def killAnimation(self):
        pass

    def rotatePhoto(self):
        pass
