import pygame, Settings, Tools


class Alien_spaceship(pygame.sprite.Sprite):

      #Initalize the Alien_spaceship object  
	def __init__(self, all_sprites):
		super(Alien_spaceship, self).__init__()
		self.image = Tools.get_scaled_image(Settings.alien_spaceship, Settings.alien_spaceship_x, Settings.alien_spaceship_y)
		self.width = Settings.SCREEN_WIDTH
		self.height = Settings.SCREEN_HEIGHT
		self.x = Settings.random_side
		self.rect = self.image.get_rect(midtop = (self.x, 20))
		self.direction = Settings.speed_aliens_spaceship if self.x == 0 else -Settings.speed_aliens_spaceship
	
		
      #Move the spaceship (to right or left - according its initial location)  	
	def update(self):
		self.rect.move_ip(self.direction, 0)
		if self.rect.left > self.width or self.rect.right < 0:
			self.kill()
