# s06.israelwi


# 1. Fisrt_steps


# Random_walk

This program shows a progression of a random walk in any chosen dimension - for any number of steps we request.

Input: 
The program asks for the requested number of dimensions and steps that the program will be asked to perform and display.

Output: 
The output of the program depends on the number of dimensions selected; If one dimension is selected, the walk will be displayed as a graph relative to the number of steps axis.
If two dimensions are selected, the progress will be shown in the graph in relation to the two dimensions of progress.
If three dimensions are selected, the walk will be displayed in a three-dimensional cube.
If a higher number of dimensions is selected, the steps will be displayed in coordinates.


# Hacker_news

This program extracts the 60 best works on 'thehackernews.com' website, and creates a csv file that contains the details: "ID", "title", "URL", "text" for these works.
Input: the name of the file (the name of the file must end in .csv)
Output: The program finds (via API) the 60 best jobs on 'thehackernews.com' website and extracts the requested details for them, then creates a csv file and writes the requested details into it.


# Wiki_crawler

This program downloads *all* images from multiple Wikipedia pages (starting from a specific page) recursively and randomly. 

Input: 
The program asks the user for a specific link to the Wikipedia website, as well as a depth and a width arguments.

Output: 
The program does the following:
1. Downloads all the images from the selected Wikipedia page to its folder.

2. Then it randomly selects a number of links - according to the number of the *width* argument - and recursively executes them.

3. The process repeats itself a number of times - according to the number of the *depth* argument.


# Github_repositories

This program performs a mathematical analysis to check the relation between the number of downloads ('forks') and 'stars' for  projects in github , with the result shown in a graph via a straight line that reflects the coefficient of determination for the number of downloads and the given number of stars, as well as representing the downloads via points for both  the training set (which contains part of the data) and in the prediction set (which contains the rest).

Input:
the program requests as input the number of project pages on which it will run the model (each such page will have 100 projects). 

Output: 
1. The program will extract the requested number of jobs from the API into an array. 

2. The program will initiate an array of pairs for the stars anf downloads data. 

3. The program will then run a 'linear regression' model on these values to check the error of the straight line that provides the coefficient of determination in relation to these points, then display it on a graph.


# 2. Introduction_to_machine_learning


# Gradient_descent

This program finds and displays the equation of the line closest to all points in a given dataset, using the gradient descent algorithm, which makes it possible to iteratively find at each step a point that minimizes the error of the straight line, until the straight line with the minimum error is obtained, which is the closest straight line to all the points.

Extensions: A. Another program finds the polynomial equation (of  second degree) closest to the points.

B. Another program uses the first program as a machine learning model of training and prediction - first it provides the equation of the line based on a training set randomly selected from the dataset, and then determines the position of the points of the test set according to it - then checks the accuracy of the prediction.
 
Input:
The program uses the data-set from the file 'XYdata.npz', and requests as input from the user: the number of iterations he wishes to run.

Output:
The program starts the calculation from an arbitrary point, and for each point performs the calculation of the gradient (the vector of the partial derivatives) in order to learn in which direction to 'lower' the values of the equation of the line (when, of course, the result of the gradient is multiplied by the learning rate to minimize possible errors). This process is repeated by the program as long as the progress continues, up to the limit of iterations defined by the user. At the end of the run, the program returns the equation of the line (or the polynomial) obtained, indicates the degree of accuracy of the line in relation to the points (coefficient of determination) and displays in a graph the equation of the straight line and the true position of the points (in the training and prediction model, the points of the test array will be displayed in different colors).

In order to increase the accuracy of the model, we defined a 'weight' for each point, so that the points close to the center (on the x-axis) receive a higher score than the points that are far from it, and when calculating the gradient we multiplied the calculation of the partial derivative for each x value by the 'weight' ' corresponding to the same value, and thus we reduced the influence of the points far from the center on the resulting straight line equation.


# k_nearest_neighbors_algorithm

This program uses the k-NN algorithm to find the number k that will provide the group of neighbors that will allow to predict with the highest degree of accuracy according to the characteristics of each flower (from the given data-set) the species to which it belongs.

Input:
The program uses a dataset from the file 'iris.data', and receives as input the highest k number that will serve as the limit of the range up to which it will check the k values.

Output:
The program performs 100 tests for each k value in the range between one and the selected k value, each time 2/3 of the data is randomly selected for the test, and sums up the average score of all tests - which is calculated from the total number of successes of  identification predictions in relation to the true identity of each flower.

At the end of the tests, the program selects the k-value that provided the highest accuracy, and returns the result of another test utilizing the k value received above, on an array that contains 1/3 of the data.


# Naive_bayes_classification

This program implements the Naive Bayes probabilistic model, the purpose of which is to characterize data according to their properties. In this program, we will first classify the data on a training set that will be randomly selected from the given data-set, and then we will choose the accuracy of the model in characterizing the data on the test set.

input:
The program uses a dataset from the file 'agaricus-lepiota.data', which holds data about different features of mushrooms (where for each feature there are several different options), as well as their  classification as 'poisonous' and 'non-poisonous' (Expansion: another program underwent substantial adjustments and changes to perform a classification into different varieties of irises according to a dataset on the sizes of the leaves. In this way, we illustrated that the model can be adapted to characterize different types of information through simple changes).

output:
1. The program splits the data into pairs of data - features alongside classification as poison/not poisonous 

2. Splits the data randomly: 80% into an array to train the model, and 20% for testing the model.

3. Training: the program extracts from the training set all the unique options that exist for each of the twenty-two attributes of the mushrooms, and initializes a nested dictionary for each attribute, within which is a nested dictionary for each option.
In the next step, the program summarizes for each option the number of times it appeared for a poisonous and non-poisonous mushroom, and with this data performs the probability calculation according to Bayes' law for each and every possibility.

Examination : After the model is trained, the program sends the test array for testing, performs a classification for each element in it, and counts and displays how many times the model gave a higher than fifty percent chance that the mushroom is indeed poisonous or less and the mushroom not poisonous as well as the percentage of success.


# k_means_clustering_algorithm

This program divides a collection of data points into k clusters (groups) iteratively by calculating the proximity of their numerical data to the centers of mass of the clusters. The program repeats this process for a range of k values and returns the k value that best fits the distribution of the data set.

input:
The program uses a data-set from the file 'iris.data' to classify three varieties of the iris flower according to four coordinates of the length and width of the leaves, and requests a user's input for the maximum number k that he wishes to test.

output:
The program divides the data into k clusters (groups) iteratively according to the calculation of the proximity of their numerical data that are used as location coordinates to the centers of mass of the clusters. In the first step the k 'centers of mass' are chosen randomly, and then in each iteration the center of mass is calculated in relation to all the points associated with that cluster.
The program repeats this process 10 times for each k between 2 and the selected maximum k, with each step keeping (for each k)the k points that provided the result with the minimum total variance.
At the end of the process the program returns the k that provided the minimum total variance, which will usually be the highest k tested, and also displays a graph of the total variance for each k, thus allowing us to find the k value of the 'elbow point' for which a relatively good overall variance was obtained despite the division into a relatively low number of clusters.
After closing the graph, the program will offer the user to enter the k he chose, and will calculate the 'confusion matrix' for the calculation where we can see for each of the k clusters how many of the data points did in truth belong to each of the groups.


# 3. Space_invaders


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


# 4. Brick_breaker


In this project I implemented the well-known game "Brick breaker"; In this game, the player uses the keyboard to control the surface located at the bottom of the screen, and tries to prevent the block that bounces on the screen at high speed (and at an angle that changes randomly when hitting the surface) from reaching the bottom. At the top of the screen colored blocks are positioned and when the block hits them, they are destroyed, and the player gets a score.

The game includes three stages, the transition between which is done when the player succeeds in destroying all the colored blocks. At each stage, the following changes:
1. The length of the player's surface (which shortens in the third stage). 
2. The number and size of the colored blocks. 
3. The block's movement speed.
4. the background image.

The player receives a limited number of 'lives' (which accumulated from stage to stage) that decrease every time he fails to prevent the block from reaching the ground, and when they are finished the game ends.

This project is a personal task that I took on, in addition to the usual assignments of the Python course.

Note: The game is built using the Pygame module of Python. If the library is not installed on your computer, it must be installed before running the program.


# 5. Small_projects


# Oop - object oriented

This project includes several small tasks conducted as part of learning the 'object-oriented' features of the Python programming language. Each folder contains several programs that simulate a music site/sales site, etc. and communicate with each other through 'inheritance' and 'composition'.


# Star Wars API
This program allows you to analyze information about the 'Star Wars' movies from the website 'swapi.dev'. The program allows you to perform two actions:
1. Search for information for a specific term from one of the resources in the API (for user input: search <resource> <term>).
2. Display the planets data sorted according to each selected term - in ascending or descending order (for user input: sort <order_field> <True/False>).

