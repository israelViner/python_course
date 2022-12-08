import pygame, Tools, Settings, random


class Block(pygame.sprite.Sprite):

      #Initalize Block object
	def __init__(self, coordinates, level, color = random.choice(Settings.color_array),rectangle = False):
		super(Block, self).__init__()
		self.color = color
		x_size = Settings.size_box if not rectangle else Settings.x_obstacle[level]
		y_size = Settings.size_box if not rectangle else Settings.y_obstacle[level]
		self.image = pygame.Surface((x_size, y_size))
		self.image.fill(self.color)
		self.rect = self.image.get_rect(center = (coordinates))
		self.speed = [Settings.speed_block[int(level)], -Settings.speed_block[int(level)]]
		
	
	def update_(self, all_sprites, lives, screen, player_group, level):
		if self.rect.left < 0 or self.rect.right > Settings.SCREEN_WIDTH:
			Tools.sound_play(Settings.shots_music)
			self.speed[0] = -self.speed[0]
		if self.rect.top < 0:
			Tools.sound_play(Settings.shots_music)
			self.speed[1] = -self.speed[1]
		if self.rect.bottom > Settings.SCREEN_HEIGHT:
			lives -= 1
			if lives != 0:
				Tools.pop_up(screen, "Its okay, Let's try again", pygame.K_KP_ENTER)
				place = 4
				for i, block in zip(range(place), player_group):
					new_place = block
				self.rect = self.image.get_rect(midbottom = new_place.rect.midtop)
				self.speed = [Settings.speed_block[int(level)], -Settings.speed_block[int(level)]]
		self.rect.move_ip(self.speed)
		return lives
		
		
	def check_colission(self, all_sprites, player_group, obstacles_group, score, level):
		collide = pygame.sprite.spritecollide(self, player_group, False)
		if collide:
			Tools.sound_play(Settings.shots_music)
			self.speed[0] = self.speed[0] + random.choice([0, 1/4, 1/2, 3/4, 1])
			self.speed[1] = -self.speed[1]
		collision = pygame.sprite.spritecollide(self, obstacles_group, True)
		if collision:
			Tools.sound_play(Settings.shots_music)
			self.speed[1] = -self.speed[1]
			score += 5*(level+1)
		return score

		
