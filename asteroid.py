import pygame

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x_axis, y_axis, radius):
        super().__init__(x_axis, y_axis, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

