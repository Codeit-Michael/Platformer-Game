import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.image = pygame.Surface((size, size))
		self.image.fill(pygame.Color("darkorange"))
		self.rect = self.image.get_rect(topleft = pos)

	def update(self, x_shift):
		self.rect.x += x_shift