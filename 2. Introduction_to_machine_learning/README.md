# s06.israelwi


# 1. Gradient descent

This program finds and displays the equation of the line closest to all points in a given dataset, using the gradient descent algorithm, which makes it possible to iteratively find at each step a point that minimizes the error of the straight line, until the straight line with the minimum error is obtained, which is the closest straight line to all the points.

Extensions: A. Another program finds the polynomial equation (of  second degree) closest to the points.

B. Another program uses the first program as a machine learning model of training and prediction - first it provides the equation of the line based on a training set randomly selected from the dataset, and then determines the position of the points of the test set according to it - then checks the accuracy of the prediction.
 
Input:
The program uses the data-set from the file 'XYdata.npz', and requests as input from the user: the number of iterations he wishes to run.

Output:
The program starts the calculation from an arbitrary point, and for each point performs the calculation of the gradient (the vector of the partial derivatives) in order to learn in which direction to 'lower' the values of the equation of the line (when, of course, the result of the gradient is multiplied by the learning rate to minimize possible errors). This process is repeated by the program as long as the progress continues, up to the limit of iterations defined by the user. At the end of the run, the program returns the equation of the line (or the polynomial) obtained, indicates the degree of accuracy of the line in relation to the points (coefficient of determination) and displays in a graph the equation of the straight line and the true position of the points (in the training and prediction model, the points of the test array will be displayed in different colors).

In order to increase the accuracy of the model, we defined a 'weight' for each point, so that the points close to the center (on the x-axis) receive a higher score than the points that are far from it, and when calculating the gradient we multiplied the calculation of the partial derivative for each x value by the 'weight' ' corresponding to the same value, and thus we reduced the influence of the points far from the center on the resulting straight line equation.

# 2. k-nearest neighbors algorithm

This program uses the k-NN algorithm to find the number k that will provide the group of neighbors that will allow to predict with the highest degree of accuracy according to the characteristics of each flower (from the given data-set) the species to which it belongs.

Input:
The program uses a dataset from the file 'iris.data', and receives as input the highest k number that will serve as the limit of the range up to which it will check the k values.

Output:
The program performs 100 tests for each k value in the range between one and the selected k value, each time 2/3 of the data is randomly selected for the test, and sums up the average score of all tests - which is calculated from the total number of successes of  identification predictions in relation to the true identity of each flower.

At the end of the tests, the program selects the k-value that provided the highest accuracy, and returns the result of another test utilizing the k value received above, on an array that contains 1/3 of the data.

# 3. Naive Bayes classification

This program implements the Naive Bayes probabilistic model, the purpose of which is to characterize data according to their properties. In this program, we will first classify the data on a training set that will be randomly selected from the given data-set, and then we will choose the accuracy of the model in characterizing the data on the test set.

input:
The program uses a dataset from the file 'agaricus-lepiota.data', which holds data about different features of mushrooms (where for each feature there are several different options), as well as their  classification as 'poisonous' and 'non-poisonous' (Expansion: another program underwent substantial adjustments and changes to perform a classification into different varieties of irises according to a dataset on the sizes of the leaves. In this way, we illustrated that the model can be adapted to characterize different types of information through simple changes).

output:
1. The program splits the data into pairs of data - features alongside classification as poison/not poisonous 

2. Splits the data randomly: 80% into an array to train the model, and 20% for testing the model.

3. Training: the program extracts from the training set all the unique options that exist for each of the twenty-two attributes of the mushrooms, and initializes a nested dictionary for each attribute, within which is a nested dictionary for each option.
In the next step, the program summarizes for each option the number of times it appeared for a poisonous and non-poisonous mushroom, and with this data performs the probability calculation according to Bayes' law for each and every possibility.

Examination : After the model is trained, the program sends the test array for testing, performs a classification for each element in it, and counts and displays how many times the model gave a higher than fifty percent chance that the mushroom is indeed poisonous or less and the mushroom not poisonous as well as the percentage of success.

# 4. k_means_clustering algorithm

This program divides a collection of data points into k clusters (groups) iteratively by calculating the proximity of their numerical data to the centers of mass of the clusters. The program repeats this process for a range of k values and returns the k value that best fits the distribution of the data set.

input:
The program uses a data-set from the file 'iris.data' to classify three varieties of the iris flower according to four coordinates of the length and width of the leaves, and requests a user's input for the maximum number k that he wishes to test.

output:
The program divides the data into k clusters (groups) iteratively according to the calculation of the proximity of their numerical data that are used as location coordinates to the centers of mass of the clusters. In the first step the k 'centers of mass' are chosen randomly, and then in each iteration the center of mass is calculated in relation to all the points associated with that cluster.
The program repeats this process 10 times for each k between 2 and the selected maximum k, with each step keeping (for each k)the k points that provided the result with the minimum total variance.
At the end of the process the program returns the k that provided the minimum total variance, which will usually be the highest k tested, and also displays a graph of the total variance for each k, thus allowing us to find the k value of the 'elbow point' for which a relatively good overall variance was obtained despite the division into a relatively low number of clusters.
After closing the graph, the program will offer the user to enter the k he chose, and will calculate the 'confusion matrix' for the calculation where we can see for each of the k clusters how many of the data points did in truth belong to each of the groups.

23/11/2022


