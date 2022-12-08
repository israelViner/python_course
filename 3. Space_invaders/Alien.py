import pygame, Tools, Settings


class Alien(pygame.sprite.Sprite):

      #Initalize alien object
	def __init__(self, width, height, img_file):
		super(Alien, self).__init__()
		self.image = Tools.get_scaled_image(img_file, Settings.alien_x, Settings.alien_y)
		self.rect = self.image.get_rect(center = (width, height))
		
