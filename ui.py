from circleshape import CircleShape
from constants import *
import pygame
import os.path as path

class ScoreUI(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__(self.containers)
		self.font = pygame.font.Font(path.join('assets','font','Moonlit Horta.ttf'),size = 30)
		self.score_text = 0
		self.surface = self.font.render(str(self.score_text),True,"white")

	def draw(self, screen):
		screen.blit(self.surface,(SCREEN_WIDTH//2,10))

	def update(self,delta_time):
		self.surface = self.font.render(str(self.score_text),True,"white")
		self.surface.blit(self.surface,(SCREEN_WIDTH//2,10))


