import pygame
import random


#The size of the screen
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1500

#The number of lives of the player
lives = 3

#The speed & direction of the shot movment
speed_shot = 10

#The speed & direction of the aliens movment
speed_movement = [4, 7, 9, 11]

#The number of parallel shots of the aliens
parallel_shots = [1, 1, 1, 2]

#The fall height of the aliens (when they reach the wall)
fall = [10, 11, 12, 13]

#Choose the side of alien's spaceship appearance
random_side = random.choice([0, SCREEN_WIDTH]) 

#The speed of the alien's spaceship
speed_aliens_spaceship = 8

#Determine the score for killing alien spaceship
random_score = random.choice([50,100,150,200]) 
 
#The timer for each shot of the player (milliseconds)
timer_shot = [400, 300, 200, 20]

#The timer for the alien's spaceship appearance (milliseconds)
timer_alien_spaceship = 10000
 
#The timer for aliens shooting (milliseconds)
timer_alien_shot = 400

#Alien's size
alien_x = 50
alien_y = 45

#Spaceship size
spaceship_x = 80
spaceship_y = 80

#Alien spaceship size
alien_spaceship_x = 150
alien_spaceship_y = 60
  
#Images
opening_screen = 'images/DRf8fR8XUAEi9rp.jpg_large'
background_image = ["images/background1.jpg", "images/background2.jpg", "images/background3.jpg", "images/background4.jpg"]
spaceship_image = ['images/spaceship1.png','images/spaceship2.png', 'images/spaceship3.png', 'images/spaceship4.png']
shot_image = "images/1454337-glenos-g-160-bulletpng-bullet-png-1280_1280.png"
aliens_images = ['images/alien4.png','images/alien2.png','images/alien3.png','images/alien1.png']
alien_spaceship = 'images/alien_spaceship.png'

#Sounds
background_music = ['sounds/background1.mp3', 'sounds/background2.mp3', 'sounds/background3.mp3', 'sounds/background4.mp3']
shots_music = 'sounds/laser.wav'
explosion_music = 'sounds/explosion.wav'
#game_over = 'sounds/game_over.wav'

#Dynamic information font & size
dynamic_information_font = 'fonts/game_over.ttf'
dynamic_information_size_font = 80

#Important mesagges font & size
important_mesagges_font = 'fonts/game_over.ttf'
important_mesagges_size_font = 170

#obstacle's locations
x_array = [170, 520, 870, 1220]
y_array = [600, 600, 600, 600]

#The size of each block
size_box = 5

#The color of the obstacles
color_block = [153,204,255]

#The shape of the obstacles
shape  = [
'     xxxxxxxxxxxxxxxx     ',
'    xxxxxxxxxxxxxxxxxx    ',
'   xxxxxxxxxxxxxxxxxxxx   ',
'  xxxxxxxxxxxxxxxxxxxxxx  ',
' xxxxxxxxxxxxxxxxxxxxxxxx ',
'xxxxxxxxxxxxxxxxxxxxxxxxxx',
'xxxxxxxxxxxxxxxxxxxxxxxxxx',
'xxxxxxxxx        xxxxxxxxx',
'xxxxxxxxx        xxxxxxxxx',
'xxxxxxxx          xxxxxxxx',
'xxxxxxxx          xxxxxxxx',
'xxxxxxxx          xxxxxxxx',
'xxxxxxx            xxxxxxx',
'xxxxxxx            xxxxxxx',
]
