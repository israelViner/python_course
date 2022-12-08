import pygame, Settings, Tools, random
from Block import Block

class Player(pygame.sprite.Sprite):

     #Initalize Player object
	def __init__(self, player_group, level):
		self.blocks_player = Settings.blocks_player[level]
		self.space_block = 30
		self.midle_player = (self.blocks_player/2) * self.space_block
		x_start = (Settings.SCREEN_WIDTH / 2) - self.midle_player
		blocks = []
		for i in range(self.blocks_player):
			block = Block((x_start, Settings.SCREEN_HEIGHT - 30), level, (102, 204, 0))
			blocks.append(block)
			x_start = x_start + self.space_block
		for block in blocks:
			player_group.add(block)
			
			
      #Move the player (right & left) according to user's presses  	
	def update(self, keys, all_sprites, player_group):
		movement = True
		if keys[pygame.K_LEFT]:
			for block in player_group:
				if block.rect.left < 0:
					movement = False
			if movement:
				for block in player_group:
					block.rect.move_ip(-5, 0)
		if keys[pygame.K_RIGHT]:
			for block in player_group:
				if block.rect.right > Settings.SCREEN_WIDTH:
					movement = False
			if movement:
				for block in player_group:
					block.rect.move_ip(5, 0)
			
			
