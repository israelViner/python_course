import pygame, sys, Settings, Tools
from Spaceship import Spaceship
from Aliens import Aliens


def main():
	pygame.init()
	PLAY = True
	level = global_score = 0
	lives = Settings.lives
		
     #Initialize the screen
	screen = Tools.initalize_screen()
			
     #Pop up a massage before the starting of the game 
	Tools.pop_up(screen, 'press ENTER', pygame.K_KP_ENTER, (0,0,0))
	
     #Set the clock for the FPS of the display
	clock = pygame.time.Clock()
				
	while PLAY:
	
	     #Set the timers for the events of shooting & thealien spaceship appearance
		TIMER_SHOT = Tools.set_timer(Settings.timer_shot[level], 1)
		TIMER_ALIEN_SPACESHIP = Tools.set_timer(Settings.timer_alien_spaceship, 2)
		TIMER_ALIEN_SHOT = Tools.set_timer(Settings.timer_alien_shot, 1)
	
	     #Set the background image & display the headline before the starting of the level
		bg = Tools.get_scaled_image(Settings.background_image[level], Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
		screen.blit(bg, (0, 0))
		Tools.pop_up(screen, f'Level {level + 1}', pygame.K_SPACE)
				
	     #Add bacground music
		pygame.mixer.stop()
		Tools.sound_play(Settings.background_music[level], -1)
				
	     #Initialize the groups of the sprites for the objects of the game  
		all_sprites, aliens_group, player_shots, aliens_shots, alien_spaceship, block_group = Tools.initalize_sprites_groups()
					
	     #Create the spaceship and the aliens & add the spaceship to the sprite's group
		spaceship = Spaceship(all_sprites, Settings.spaceship_image[level], level, lives)
		aliens = Aliens(all_sprites, aliens_group, level, global_score)
				
	     #Start the run of the time clock
		start_clock = pygame.time.get_ticks()
				
		RUNNING = True     
		
		while RUNNING:
		
		     #Folowing the events in the game (mainly for player shooting & for alien's spaceship appearance)				
			key, RUNNING = Tools.update_by_keyboard(RUNNING, spaceship, all_sprites, screen)
			events = pygame.event.get()
			Tools.event_handling(events, spaceship, key, all_sprites, player_shots, alien_spaceship, TIMER_SHOT, TIMER_ALIEN_SPACESHIP)
		               
		     #Update the procesess of the game (and collect information for checking & diaplaing)
			lives = spaceship.check_collision(aliens_shots, aliens_group, screen, block_group)
			score = aliens.check_collision(player_shots, alien_spaceship, aliens_group, block_group)
			seconds = (pygame.time.get_ticks() - start_clock)//1000
			not_running = Tools.update_groups(all_sprites, aliens, aliens_shots, player_shots, alien_spaceship, TIMER_ALIEN_SHOT, events, level)
												
		     #Checking the conditions for 'game over'
			RUNNING, PLAY = Tools.is_game_over(RUNNING, spaceship, aliens_group, lives, not_running, screen)
						
		     #Checking the condition for winning the game
			RUNNING = Tools.is_level_complete(RUNNING, screen, aliens_group)
															
		     #Displaing the screen & dynamic information about the status of the game
			Tools.display(screen, all_sprites, bg, level, score, lives, seconds, clock)
		
	      #level up		
		lives += Settings.lives				
		global_score = score + 300*(level+1)
		level += 1
		PLAY = Tools.is_win(PLAY, screen, level, global_score)


if __name__=="__main__":
	main()
