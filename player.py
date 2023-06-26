import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.Surface((25, 50))
		self.image.fill(pygame.Color("indigo"))
		self.rect = self.image.get_rect(topleft = pos)

		# player movement
		self.direction = pygame.math.Vector2(0, 0)
		self.speed = 5
		self.gravity = 1
		self.jump_speed = -16

	def get_input(self, clicked_key):
		if clicked_key != False:
			if clicked_key == "right":
				self.direction.x = 1
			elif clicked_key == "left":
				self.direction.x = -1
		else:
			self.direction.x = 0

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def jump(self):
		self.direction.y = self.jump_speed

	def update(self, clicked_key):
		if clicked_key == "space":
			self.jump()
		else:
			self.get_input(clicked_key)

		self.rect.x += self.direction.x * self.speed
		self.apply_gravity()