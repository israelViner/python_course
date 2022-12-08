import pygame, Settings, Tools
import random
from pygame import mixer
from Alien import Alien
from Shots import Shots


class Aliens(pygame.sprite.Sprite):
	
     #Initalize aliens group object  
	def __init__(self, all_sprites, aliens_group, level, global_score):
		super(Aliens, self).__init__()
		self.aliens = []
		self.width = Settings.SCREEN_WIDTH
		self.height = Settings.SCREEN_HEIGHT
		self.parallel_shots = Settings.parallel_shots[level]
		self.direction = Settings.speed_movement[level]
		self.fall= 0
		self.score = global_score
		aliens_images = Settings.aliens_images
		
	      #Create the aliens with different characters for each row
		for i in range(150, self.width - 100, 100):
			for j, image in zip(range(50, self.height - 400, 50), aliens_images):
				new_alien = Alien(i, j, image)
				self.aliens.append(new_alien)
	       
	      #Add the aliens to the group of the aliens & add the groop to the sprite's group		
		for alien in self.aliens:
			aliens_group.add(alien)
		all_sprites.add(aliens_group)
			
	
      #The update process of the aliens - the movement and the call to the shooting function (& return the checking if the aliens touching in the ground)		
	def update(self, all_sprites, aliens_shots, TIMER_ALIEN_SHOT, events, level):
		not_running = False
		
	      #Call to shooting
		for event in events:
			if event.type == TIMER_ALIEN_SHOT:
				if len(aliens_shots) < self.parallel_shots and len(self.aliens) > 0: 
					Aliens.alien_shot(self, all_sprites, aliens_shots)
		
	      #The movement
		for Alien in self.aliens:
			if Alien.rect.right >= self.width or Alien.rect.left <= 0:
				self.direction = -self.direction
				self.fall = Settings.fall[level]
				break
		for Alien in self.aliens:
			Alien.rect.move_ip(self.direction, self.fall)
		self.fall= 0
		
	      #Check if an alien touch in the ground
		for alien in self.aliens:
			if alien.rect.bottom >= self.height:
				not_running = True
		return not_running
		
		
      #Create the shot from random alien 
	def alien_shot(self, all_sprites, aliens_shots):
		place = random.randint(0, len(self.aliens) -1)
		place_shot = self.aliens[place].rect.midbottom
		Tools.sound_play(Settings.shots_music)
		new_shot = Shots(place_shot, Settings.speed_shot, all_sprites)
		aliens_shots.add(new_shot)
		all_sprites.add(new_shot)
	
		
      #Checking if one of the aliens was hit from shot & return the updated score
	def check_collision(self, player_shots, alien_spaceship, aliens_group, block_group):
		
	      #Handling collisions between  aliens and obstacles 
		for alien in aliens_group:
			if pygame.sprite.spritecollide(alien, block_group, True):
				for block in block_group:
					block.kill()
	     
	      #Handling collisions between shot (from the player) and obstacles
		for bullet in player_shots:
			collision = pygame.sprite.spritecollide(bullet, block_group, True)
			if collision:
				bullet.kill()
				
	      #Handling collisions between shot (from the player) and aliens / alien spaceship
		for shot in player_shots:
			collide_space = pygame.sprite.spritecollide(shot, alien_spaceship, True)
			collide = pygame.sprite.spritecollide(shot, aliens_group, True)
			if collide_space:
				Tools.sound_play(Settings.explosion_music)
				self.score += Settings.random_score
				shot.kill()
			for alien in collide:
				Tools.sound_play(Settings.explosion_music)
				self.aliens.remove(alien)
				alien.kill()
			if collide:
				self.score += 10
				shot.kill()
		return self.score
			
				
		
