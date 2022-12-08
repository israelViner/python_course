import pygame, Settings


class Shots(pygame.sprite.Sprite):
	
      #Initalize shot object  
	def __init__(self, location, speed_shot, all_sprites):
		super(Shots, self).__init__()
		self.Shots = []
		self.width = Settings.SCREEN_WIDTH
		self.height = Settings.SCREEN_HEIGHT
		self.speed = speed_shot
		self.image = pygame.image.load(Settings.shot_image)
		self.image = pygame.transform.scale(self.image, (20, 40))
		self.rect = self.image.get_rect(center = location)
		

      #Move the shot			
	def update(self):
		self.rect.move_ip(0, self.speed)
		if self.rect.top <= 0 or self.rect.bottom >= self.height:
			self.kill()
