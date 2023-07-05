import pygame
from tile import Tile
from trap import Trap
from settings import tile_size, WIDTH
from player import Player
from game import Game
from goal import Goal

class World:
	def __init__(self, world_data, surface):
		self.display_surface = surface
		self.world_data = world_data
		self.setup_world(world_data)
		self.world_shift = 0
		self.current_x = 0
		self.gravity = 0.7
		self.game = Game()

	def setup_world(self, layout):
		self.tiles = pygame.sprite.Group()
		self.traps = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self.goal = pygame.sprite.GroupSingle()

		for row_index, row in enumerate(layout):
			for col_index, cell in enumerate(row):
				x, y = col_index * tile_size, row_index * tile_size
				if cell == "X":
					tile = Tile((x, y), tile_size)
					self.tiles.add(tile)
				elif cell == "s":
					tile = Trap((x, y), tile_size)
					self.traps.add(tile)
				elif cell == "P":
					player_sprite = Player((x, y))
					self.player.add(player_sprite)
				elif cell == "G":
					goal_sprite = Goal((x, y), tile_size)
					self.goal.add(goal_sprite)

	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x

		if player_x < WIDTH // 4 and direction_x < 0:
			self.world_shift = 8
			player.speed = 0
		elif player_x > WIDTH - (WIDTH // 4) and direction_x > 0:
			self.world_shift = -8
			player.speed = 0
		else:
			self.world_shift = 0
			player.speed = 3

	def apply_gravity(self, player):
		player.direction.y += self.gravity
		player.rect.y += player.direction.y

	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				# checks if moving towards left
				if player.direction.x < 0:
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				# checks if moving towards right
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right
		if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
			player.on_right = False

	def vertical_movement_collision(self):
		player = self.player.sprite
		self.apply_gravity(player)

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				# checks if moving towards bottom
				if player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				# checks if moving towards up
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True
		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False
		if player.on_ceiling and player.direction.y > 0:
			player.on_ceiling = False

	def handle_traps(self):
		player = self.player.sprite

		for sprite in self.traps.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.x < 0 or player.direction.y > 0:
					player.rect.x += tile_size
				elif player.direction.x > 0 or player.direction.y > 0:
					player.rect.x -= tile_size
				# Note: add delay to life subtracter
				player.life -= 1
		# game_over() if player.life <= 0 else None

	def update(self, player_event):
		# for tile
		self.tiles.update(self.world_shift)
		self.tiles.draw(self.display_surface)

		# for trap
		self.traps.update(self.world_shift)
		self.traps.draw(self.display_surface)

		# for goal
		self.goal.update(self.world_shift)
		self.goal.draw(self.display_surface)


		self.scroll_x()

		# for player
		self.player.update(player_event)
		self.horizontal_movement_collision()
		self.vertical_movement_collision()
		self.handle_traps()
		self.player.draw(self.display_surface)

		self.game.game_state(self.player.sprite, self.goal.sprite)
