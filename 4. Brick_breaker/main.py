import pygame, sys, Settings, Tools, random
from Block import Block
from Player import Player
from Obstacles import Obstacles


def main():
	pygame.init()
	
      #Initialize the screen
	screen = Tools.initalize_screen()
	
      #Pop up a massage before the starting of the game 
	Tools.pop_up(screen, 'press ENTER', pygame.K_KP_ENTER)
		
      #Start the run of the time clock
	start_clock = pygame.time.get_ticks()
	
	PLAY = True
	lives = Settings.lives
	level = score = 0
	
	while PLAY:
	
		screen.blit(Tools.get_scaled_image(Settings.messages_background, Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT), (0,0))
		Tools.pop_up(screen, f'Level {level + 1}', pygame.K_SPACE)
	      
	      #Update the background image
		img = Tools.get_scaled_image(Settings.background[level], Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
			
              #Initialize the groups of the sprites for the objects of the game  
		ball_group = pygame.sprite.Group()
		player_group = pygame.sprite.Group()
		all_sprites = pygame.sprite.Group()
		obstacles_group = pygame.sprite.Group()
	
	      #Create the ball and the obstacles & add the sprite's to the sprite's group
		ball = Block((Settings.SCREEN_WIDTH / 2, Settings.SCREEN_HEIGHT - 55), level, random.choice(Settings.color_array))
		obstacles = Obstacles(obstacles_group, level)
		player = Player(player_group, level)
		ball_group.add(ball)
		all_sprites.add(ball_group)
		all_sprites.add(player_group)
		all_sprites.add(obstacles_group)
	
	      #Add bacground music
		pygame.mixer.stop()
		Tools.sound_play(Settings.background_music, -1)
			
		RUNNING = True

		while RUNNING:
			seconds = (pygame.time.get_ticks() - start_clock)//1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
		     #Update the procesess of the game (and collect information for checking & diaplaing)
			lives = ball.update_(ball_group, lives, screen, player_group, level)
			key = pygame.key.get_pressed()
			player.update(key, all_sprites, player_group)
			score = ball.check_colission(all_sprites, player_group, obstacles_group, score, level)
			RUNNING = Tools.update_by_keyboard(RUNNING, screen)
			
		     #Checking the conditions for 'game over'
			if lives == 0:
				Tools.pop_up(screen, 'Game over!', pygame.K_KP_ENTER)
				RUNNING = False
				PLAY = False
			
		      #Checking the condition for completion of the stage	
			if not obstacles_group:
				Tools.pop_up(screen, 'Well done!', pygame.K_KP_ENTER)
				RUNNING = False
							
		      #Display the dynamic information during the game 	
			level_txt, levelRect = Tools.dynamic_information(f'Level: {str(level + 1)}', (50, 25))
			time, timeRect = Tools.dynamic_information(f'Game time: {str(seconds)}', (50, 65))
			live, livesRect = Tools.dynamic_information(f'Lives: {str(lives - 1)}', (50, 105))
			score_txt, scoreRect = Tools.dynamic_information(f'Score: {str(score)}', (50, 145))
			

		      #Displaing the screen
			screen.blit(img, (0, 0))
			for block in all_sprites:
				screen.blit(block.image, block.rect)
			screen.blit(level_txt, levelRect)
			screen.blit(time, timeRect)
			screen.blit(score_txt, scoreRect)
			screen.blit(live, livesRect)
			pygame.display.flip()
		
	      #level-up
		level += 1
		lives = Settings.lives + lives
		score += 300*(level+1)
		
	      #Checking the condition for winning the game
		PLAY = Tools.is_win(PLAY, screen, level, score)
	

if __name__=="__main__":
	main()
	


