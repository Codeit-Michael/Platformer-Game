import pygame, sys
from settings import *
from level import Level

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()
level = Level(level_map, screen)
clicked_key = False

bg_img = pygame.image.load('img/bg/bg-img.jpg')
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

while True:
	screen.blit(bg_img, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				clicked_key = "left"
			if event.key == pygame.K_RIGHT:
				clicked_key = "right"
			if event.key == pygame.K_SPACE:
				clicked_key = "space"
		elif event.type == pygame.KEYUP:
			clicked_key = False

	level.draw(clicked_key)
	pygame.display.update()
	clock.tick(60)
