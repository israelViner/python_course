# s06.israelwi

# 1. Random_walk
This program shows a progression of a random walk in any chosen dimension - for any number of steps we request.

Input: 
The program asks for the requested number of dimensions and steps that the program will be asked to perform and display.

Output: 
The output of the program depends on the number of dimensions selected; If one dimension is selected, the walk will be displayed as a graph relative to the number of steps axis.
If two dimensions are selected, the progress will be shown in the graph in relation to the two dimensions of progress.
If three dimensions are selected, the walk will be displayed in a three-dimensional cube.
If a higher number of dimensions is selected, the steps will be displayed in coordinates.

# 2. Hacker_news
This program extracts the 60 best works on 'thehackernews.com' website, and creates a csv file that contains the details: "ID", "title", "URL", "text" for these works.
Input: the name of the file (the name of the file must end in .csv)
Output: The program finds (via API) the 60 best jobs on 'thehackernews.com' website and extracts the requested details for them, then creates a csv file and writes the requested details into it.

# 3. Wiki_crawler

This program downloads *all* images from multiple Wikipedia pages (starting from a specific page) recursively and randomly. 

Input: 
The program asks the user for a specific link to the Wikipedia website, as well as a depth and a width arguments.

Output: 
The program does the following:
1. Downloads all the images from the selected Wikipedia page to its folder.

2. Then it randomly selects a number of links - according to the number of the *width* argument - and recursively executes them.

3. The process repeats itself a number of times - according to the number of the *depth* argument.

# 4. Github repositories

This program performs a mathematical analysis to check the relation between the number of downloads ('forks') and 'stars' for  projects in github , with the result shown in a graph via a straight line that reflects the coefficient of determination for the number of downloads and the given number of stars, as well as representing the downloads via points for both  the training set (which contains part of the data) and in the prediction set (which contains the rest).

Input:
the program requests as input the number of project pages on which it will run the model (each such page will have 100 projects). 

Output: 
1. The program will extract the requested number of jobs from the API into an array. 

2. The program will initiate an array of pairs for the stars anf downloads data. 

3. The program will then run a 'linear regression' model on these values to check the error of the straight line that provides the coefficient of determination in relation to these points, then display it on a graph.


18/11/2022


