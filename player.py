import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.import_character_assets()
		self.frame_index = 0
		self.animation_speed = 0.15
		self.image = self.animations["idle"][self.frame_index]
		self.rect = self.image.get_rect(topleft = pos)

		# player movement
		self.direction = pygame.math.Vector2(0, 0)
		self.speed = 5
		self.gravity = 1
		self.jump_speed = -16

		# player status
		self.status = "idle"

	def import_character_assets(self):
		character_path = "img/pete/"
		self.animations = {
			"idle": [],
			"walk": [],
			"jump": [],
			"fall": []
		}
		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def animate(self):
		animation = self.animations[self.status]
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0
		self.image = animation[int(self.frame_index)]

	def get_input(self, clicked_key):
		if clicked_key != False:
			if clicked_key == "right":
				self.direction.x = 1
				self.animate()
			elif clicked_key == "left":
				self.direction.x = -1
				self.animate()
		else:
			self.direction.x = 0
			self.animate()

	def get_status(self):
		if self.direction.y < 0:
			self.status = "jump"
		elif self.direction.y > 0:
			self.status = "fall"
		elif self.direction.x != 0:
			self.status = "walk"
		else:
			self.status = "idle"

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def jump(self):
		self.direction.y = self.jump_speed

	def update(self, clicked_key):
		self.get_status()
		if clicked_key == "space":
			self.jump()
		else:
			self.get_input(clicked_key)

