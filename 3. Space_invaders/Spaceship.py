import pygame, sys, Settings, Tools
from pygame import mixer
from Shots import Shots


class Spaceship(pygame.sprite.Sprite):

      #Initalize the spaceship object  
	def __init__(self, all_sprites, image, level, lives):
		super(Spaceship, self).__init__()
		self.image = Tools.get_scaled_image(image, Settings.spaceship_x, Settings.spaceship_y)
		self.width = Settings.SCREEN_WIDTH
		self.height = Settings.SCREEN_HEIGHT
		self.rect = self.image.get_rect(midbottom = (self.width/2, self.height - 10))
		self.lives = lives
		all_sprites.add(self)
		
		
      #Move the spaceship (right & left) according to user's presses  	
	def update(self, keys, all_sprites):
		if keys[pygame.K_LEFT] and self.rect.left > 0:
			self.rect.move_ip(-5, 0)
		if keys[pygame.K_RIGHT] and self.rect.right < self.width:
			self.rect.move_ip(5, 0)
	
		        	   		
      #Create the user's shots from the spaceship   	   		
	def spaceship_shoot(self, keys, all_sprites, player_shots):
		plece = self.rect.center
		if keys[pygame.K_SPACE]:
			Tools.sound_play(Settings.shots_music)
			new_shot = Shots(self.rect.midtop, -Settings.speed_shot, all_sprites)
			player_shots.add(new_shot)
			all_sprites.add(new_shot)
           
           		
      #Checking if the alien's shots hits the spaceship (and return the updated number of the lives)   		
	def check_collision(self, aliens_shots, aliens_group, screen, block_group):
		
	     #Handling collisions between the spaceship and the shots (from the aliens)
		collide = pygame.sprite.spritecollide(self, aliens_shots, True)
		if collide:
			Tools.sound_play(Settings.explosion_music)
			self.lives -= 1
			if self.lives != 0:
				Tools.pop_up(screen, "Its okay, Let's try again", pygame.K_KP_ENTER)
			self.rect = self.image.get_rect(midbottom = (self.width/2, self.height - 10))
		
	      #Handling collisions between shot (from the aliens) and obstacles
		for shot in aliens_shots:
			collision = pygame.sprite.spritecollide(shot, block_group, True)
			if collision:
				shot.kill()
		return self.lives
		
		

