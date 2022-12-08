# s06.israelwi


# Space Invaders

In short:
This program contains an extended implementation of the "Space Invaders" game - including several stages of increasing difficulty and a changing background sound that accompanies the game.

In length :
The program contains the well known game "Space Invaders"; The player controls a spaceship that can move left or right by pressing the arrow keys, and must shoot and destroy the aliens invading from space before they reach the bottom.
As they move, the aliens randomly fire timed shots towards the spaceship, with the player having a limited number of 'lives' to lose (accumulated throughout the stages) until the player is finally eliminated and the game ends.
Bonus: once every ten seconds the aliens' mothership passes by at the top of the screen. Destroying it earns the player an additional high score.
Throughout the game, the following data is displayed in the upper left part of the screen:
1. the current stage.
2. The time passed since the player started the current phase.
3. The score the player has earned.
4. The number of 'lives' he has left.
 
Stages:
The game includes four stages of increasing difficulty, with each stage the following is being updated and changed:
1. The speed of movement of the invading aliens.
2. their rate of descent.
3. The rate of shots that the player is allowed.
4. the background image.
5. background music.
6. The spaceship.
At the end of each stage, a praise message will appear for the player (which can be skipped by pressing the 'enter' key), and then an announcement of the next stage (which can be skipped by pressing the 'space' key).

Score:
For each alien destroyed the player earns 10 points, and for the destruction of the mothership that passes on the screen, the player will earn a random number ranging from 50 to 200 points. The score is accumulated  from stage to stage.

Remarks:
Pressing the 'tab' key will pause the game. The game can be resumed by pressing 'Enter'.
Also, there is a 'back door' in the game to move between stages with the 'backspace' key.

Note: The game is built using the Pygame module of Python. If the library is not installed on your computer, it must be installed before running the program.


29/11/2022


