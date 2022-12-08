import pygame, sys, Settings
from pygame import mixer
from Block import Block


#initalize the screen of the game
def initalize_screen():
	pygame.display.set_caption("Brick Breaker")
	img = get_scaled_image(Settings.messages_background, Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
	size = Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT
	screen = pygame.display.set_mode(size)
	screen.blit(img, (0, 0))
	#screen.fill((96,96,96))
	return screen
		
		
#Get commands from keyboard and performs them 		
def update_by_keyboard(RUNNING, screen):
	key = pygame.key.get_pressed()
	if key[pygame.K_ESCAPE]:
		sys.exit()
	
      #Pause the game by TAB key	
	if key[pygame.K_TAB]:
		pop_up(screen, 'Pause', pygame.K_KP_ENTER)
			
      #Back door to skip to the next level
	if key[pygame.K_BACKSPACE]:
		RUNNING = False
	return RUNNING
		

#Check if the player won the game (after 3 levels)
def is_win(PLAY, screen, level, score):
	if level == 3 and PLAY == True:
		pop_up(screen, f'you win! your score is: {score}', pygame.K_SPACE)
		PLAY = False
	return PLAY
		

#Play the sounds of the game		
def sound_play(music, repeat = 0):
	background_sound = mixer.Sound(music)
	background_sound.play(repeat)
		

#Scaled an image to the requested size		
def get_scaled_image(image, width, height):
	scaled_image = pygame.image.load(image)
	return pygame.transform.scale(scaled_image, (width, height))
		

#Display the important messages during the game 
def pop_up(screen, message, press_key, color = (102, 204, 0)):		
	white = (255, 255, 255)
	black = (0,0,0)
	font = pygame.font.Font(Settings.important_mesagges_font, Settings.important_mesagges_size_font)
	text = font.render(message , True, color)
	textRect = text.get_rect()
	textRect.center = (Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT// 2)
	key = pygame.key.get_pressed()
	while not key[press_key]:
		key = pygame.key.get_pressed()
		screen.blit(text, textRect)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			pygame.display.flip()
				
		
#Display the dynamic information during the game 	
def dynamic_information(massage, center):
	font = pygame.font.Font(Settings.dynamic_information_font, Settings.dynamic_information_size_font)
	text = font.render(massage , True, (102, 204, 0))
	textRect = text.get_rect(topleft = center)
	return text, textRect
