import pygame
import random

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x_axis, y_axis, radius):
        super().__init__(x_axis, y_axis, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS).velocity += self.position.rotate(angle) * 1.2
        Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS).velocity += self.position.rotate(-angle) * 1.2


