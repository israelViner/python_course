import pygame, Settings, Tools, random
from Block import Block

class Obstacles(pygame.sprite.Sprite):

     #Initalize Player object
	def __init__(self, obstacles_group, level):
		blocks = []
		for i in range(30, Settings.SCREEN_WIDTH + 20, Settings.x_obstacle[level] + 10):
			for j in range(20, Settings.SCREEN_HEIGHT - 700, Settings.y_obstacle[level] + 10):
				block = Block((i, j), level, random.choice(Settings.color_array), True)
				blocks.append(block)
		for block in blocks:
			obstacles_group.add(block)
	
