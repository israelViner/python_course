import pygame, random

#The colors of the blocks
color_array = [(255,0,0),(51,153,255),(255,255,0),(255,0,127)]

#The length of the player's surfase
blocks_player = [10, 10, 8]

#Size obstacles
x_obstacle = [125, 100, 75]
y_obstacle = [50, 50, 25]

#The size of the screen
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 900

#Determine the score for passing stages
score = [100, 250, 400]

#The speed & direction of the block movment
speed_block = [2, 4, 5]

#The number of lives of the player
lives = 5

#images
background = ["images/background2.png", "images/background3.jpg", "images/background3.jpeg"]
messages_background ="images/unnamed.png"

#Sounds
background_music = 'sounds/background2.mp3'
shots_music = 'sounds/laser.wav'
explosion_music = 'sounds/explosion.wav'
#game_over = 'sounds/game_over.wav'

#Dynamic information font & size
dynamic_information_font = 'fonts/game_over.ttf'
dynamic_information_size_font = 100

#Important mesagges font & size
important_mesagges_font = 'fonts/game_over.ttf'
important_mesagges_size_font = 170

#The size of each block
size_box = 25

#The color of the obstacles
color_block = [102,255,102]

