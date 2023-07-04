import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		img_path = 'assets/bg/stone.jpg'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (size, size))
		self.rect = self.image.get_rect(topleft = pos)

	def update(self, x_shift):
		self.rect.x += x_shift