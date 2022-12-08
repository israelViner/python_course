import pygame, sys, Settings
from pygame import mixer
from Alien_spaceship import Alien_spaceship
from Block import Block


#initalize the screen of the game
def initalize_screen():
	pygame.display.set_caption("Space invaders")
	img = get_scaled_image(Settings.opening_screen, Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
	size = Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT
	screen = pygame.display.set_mode(size)
	screen.blit(img, (0, 0))
	return screen
		

#Create the groups of the sprite (according to their types)		
def initalize_sprites_groups():
	all_sprites = pygame.sprite.Group()
	aliens_group = pygame.sprite.Group()
	player_shots = pygame.sprite.Group()
	aliens_shots = pygame.sprite.Group()
	alien_spaceship = pygame.sprite.Group()
	block_group = pygame.sprite.Group()
	create_multiple_obstacle(Settings.x_array, Settings.y_array, all_sprites, block_group)
	return all_sprites, aliens_group, player_shots, aliens_shots, alien_spaceship, block_group 
		
		
#Displaing the screen & dynamic information about the status of the game on it
def display(screen, all_sprites, bg, level, score, lives, seconds, clock):
      #Displaing the dynamic information
	level_txt, levelRect = dynamic_information(f'Level: {str(level + 1)}', (50, 25))
	time, timeRect = dynamic_information(f'Game time: {str(seconds)}', (50, 65))
	score_txt, scoreRect = dynamic_information(f'Score: {str(score)}', (50, 105))
	live, livesRect = dynamic_information(f'Lives: {str(lives - 1)}', (50, 145))
			
      #Displaing the screen
	screen.fill([0, 0, 0])
	screen.blit(bg, (0, 0))
	screen.blit(level_txt, levelRect)
	screen.blit(time, timeRect)
	screen.blit(score_txt, scoreRect)
	screen.blit(live, livesRect)
	for sprite in all_sprites:
		screen.blit(sprite.image, sprite.rect)
	pygame.display.flip()
	clock.tick(50)
		

#Update the groups of the aliens during the while-game		
def update_groups(all_sprites,aliens, aliens_shots, player_shots, alien_spaceship, TIMER_ALIEN_SHOT, events, level):
	not_running = aliens.update(all_sprites, aliens_shots, TIMER_ALIEN_SHOT, events, level)
	aliens_shots.update()
	player_shots.update()
	alien_spaceship.update()
	return not_running
		
#Get commands from keyboard and performs them 		
def update_by_keyboard(RUNNING, spaceship, all_sprites, screen):
	key = pygame.key.get_pressed()
	spaceship.update(key, all_sprites)
	if key[pygame.K_ESCAPE]:
		sys.exit()
	
      #Pause the game by TAB key	
	if key[pygame.K_TAB]:
		pop_up(screen, 'Pause', pygame.K_KP_ENTER)
			
      #Back door to skip to the next level
	if key[pygame.K_BACKSPACE]:
		RUNNING = False
	return key, RUNNING
		

#Create new alien-spaceship (that passes at the top of the screen)		
def create_alien_spaceship(all_sprites, alien_spaceship):
	alien_space = Alien_spaceship(all_sprites)
	alien_spaceship.add(alien_space)
	all_sprites.add(alien_spaceship)
		

#Check if the player fails the game		
def is_game_over(RUNNING, spaceship, aliens_group, lives, not_running, screen):
	PLAY = True
	collide = pygame.sprite.spritecollide(spaceship, aliens_group, True)
	if lives == 0 or collide or not_running:
		pop_up(screen, 'Game over!', pygame.K_KP_ENTER)
		RUNNING = False
		PLAY = False
	return RUNNING, PLAY
		
		
#Check if the player finished the stage successfully
def is_level_complete(RUNNING, screen, aliens_group):
	if not aliens_group:
		pop_up(screen, 'Well done!', pygame.K_KP_ENTER)
		RUNNING = False
	return RUNNING
		
		
#Check if the player won the game (after 4 levels)
def is_win(PLAY, screen, level, global_score):
	if level == 4 and PLAY == True:
		pop_up(screen, f'You win the game! your score is: {global_score}', pygame.K_SPACE)
		PLAY = False
	return PLAY
		
		
#Set the timers for the events in the game
def set_timer(milliseconds, i):
	EVENT = pygame.USEREVENT + i
	pygame.time.set_timer(EVENT, milliseconds)
	return EVENT
		

#Play the sounds of the game		
def sound_play(music, repeat = 0):
	background_sound = mixer.Sound(music)
	background_sound.play(repeat)
		

#Scaled an image to the requested size		
def get_scaled_image(image, width, height):
	scaled_image = pygame.image.load(image)
	return pygame.transform.scale(scaled_image, (width, height))
		

#Handling with the scheduled events during the game (for the player shot & the creation of alien spaceship)		
def event_handling(events, spaceship, key, all_sprites, player_shots, alien_spaceship, TIMER_SHOT, TIMER_ALIEN_SPACESHIP):		
	for event in events:
		if event.type == pygame.QUIT: 
			sys.exit()
		if event.type == TIMER_SHOT:
			spaceship.spaceship_shoot(key, all_sprites, player_shots)
		if event.type == TIMER_ALIEN_SPACESHIP:
			create_alien_spaceship(all_sprites, alien_spaceship)
		
		
#Create block for obstacle
def create_obstacle(x_start, y_start, all_sprites, block_group):
	for row_index, row in enumerate(Settings.shape):
		for col_index, col in enumerate(row):
			if col == 'x':
				x = x_start + col_index * Settings.size_box
				y = y_start + row_index * Settings.size_box
				block = Block((x, y))
				block_group.add(block)
				all_sprites.add(block)
	
#Create complete obstacle				
def create_multiple_obstacle(x_array, y_array, all_sprites, block_group):
	for x, y, in zip(Settings.x_array, Settings.y_array):
		create_obstacle(x, y,  all_sprites, block_group)
		

#Display the important messages during the game 
def pop_up(screen, message, press_key, color = (255, 255, 255)):		
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
	text = font.render(massage , True, (102,102,255))
	textRect = text.get_rect(topleft = center)
	return text, textRect
