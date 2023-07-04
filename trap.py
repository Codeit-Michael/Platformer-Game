import pygame

class Trap(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		img_path = 'assets/trap/saw/off.png'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (size, size))
		self.rect = self.image.get_rect(topleft = pos)

	def update(self, x_shift):
		self.rect.x += x_shift

