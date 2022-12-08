# Brick breaker


In this project I implemented the well-known game "Brick braker"; In this game, the player uses the keyboard to control the surface located at the bottom of the screen, and tries to prevent the block that bounces on the screen at high speed (and at an angle that changes randomly when hitting the surface) from reaching the bottom. At the top of the screen colored blocks are positioned and when the block hits them, they are destroyed, and the player gets a score.

The game includes three stages, the transition between which is done when the player succeeds in destroying all the colored blocks. At each stage, the following changes:
1. The length of the player's surface (which shortens in the third stage). 
2. The number and size of the colored blocks. 
3. The block's movement speed.
4. the background image.

The player receives a limited number of 'lives' (which accumulated from stage to stage) that decrease every time he fails to prevent the block from reaching the ground, and when they are finished the game ends.

This project is a personal task that I took on, in addition to the usual assignments of the Python course.

Note: The game is built using the Pygame module of Python. If the library is not installed on your computer, it must be installed before running the program.

1/12/22
