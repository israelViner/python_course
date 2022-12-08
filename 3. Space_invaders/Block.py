import pygame, Tools, Settings


class Block(pygame.sprite.Sprite):

      #Initalize Block object
	def __init__(self, coordinates):
		super(Block, self).__init__()
		self.image = pygame.Surface((Settings.size_box, Settings.size_box))
		self.image.fill(Settings.color_block)
		self.rect = self.image.get_rect(center = (coordinates))
		
