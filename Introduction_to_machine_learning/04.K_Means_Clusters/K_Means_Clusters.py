from matplotlib import pyplot as plt
import csv
import random
import math


ITERATIONS = 10
DIMENSIONS = 4


#Test the prediction of each k in the range between 2 and the chosen large k, in order to find the best k
def find_the_best_k(d_array, max_k):
	best_k = 0
	sum_error1 = [2**63-1]*max_k
	best_k_means = []
	best_clusters = []
	
	for k in range(2, max_k):
		k_means, sum_error, clusters = clustering_loop(d_array, k)	
		if sum_error < min(sum_error1):
			best_k = k
			best_k_means = k_means
			best_clusters = clusters
		sum_error1[k] = sum_error
      
      #Round the numbers of the coordinate points 
	for i in range(len(best_k_means)):
		for j in range(len(best_k_means[0])):
			best_k_means[i][j] = round(best_k_means[i][j], 2)
	
	return best_k, best_k_means, min(sum_error1), best_clusters, sum_error1


#Test the precision of each k ITERATIONS times
def clustering_loop(d_array, k=3):
	min_sum_error = 2**63-1
	best_k_means = []
	best_clusters = []

	for i in range(ITERATIONS):
		init_k_array = random.sample(d_array, k)
		k_array, sum_error, clusters = clustering(d_array, init_k_array)
		if sum_error < min_sum_error:
			min_sum_error = sum_error
			best_k_means = k_array
			best_clusters = clusters

	return best_k_means, min_sum_error, best_clusters


#The process of clustring in each iteration, until the converge of the errors
def clustering(d_array, k_array):
	previous_k_array = []
	clusters = clustring_association(d_array, k_array)
	sum_error = squared_distance_error(clusters)
	while previous_k_array != k_array:
		previous_k_array = k_array
		k_array = find_central_mass(clusters)
		clusters = clustring_association(d_array, k_array)
		sum_error = squared_distance_error(clusters)
	return k_array, sum_error, clusters
		

#Associates the points to the nearest cluster		
def clustring_association(d_array, k_array):
	clusters = [[] for i in range(len(k_array))]
	for point in d_array:	
		index, distance = array_distance(point, k_array)
		clusters[index].append([point, distance])
	return clusters
	

#Calculate the squared distance error of the clusters in relation to the central-mass points
def squared_distance_error(clusters):
	sum_error = 0
	for i in range(len(clusters)):
		for j in range(len(clusters[i])):
			sum_error += clusters[i][j][1]
	return sum_error  
	

#Finding the central of the mass of each cluster
def find_central_mass(clusters):
	k_array = [[] for i in range(len(clusters))]
	for i in range(len(clusters)):
		for j in range(DIMENSIONS):
			central = 0
			for a in range(len(clusters[i])):
				central += clusters[i][a][0][j]/len(clusters[i])
			k_array[i].append(central)
	return k_array  
	
	
#Send the point to check distance in relation to k clusters
def array_distance(point, k_array):
	shortest = shortest_index = 2**63-1
	for i in range(len(k_array)):
		distance = check_distance(point, k_array[i])
		if distance < shortest:
			shortest = distance
			shortest_index = i
	return shortest_index, shortest


#Check the distance between 2 points by L2 model
def check_distance(point, test):
	distance = 0
	for i in range(len(point)):
		distance += (point[i] - test[i])**2 
	#distance = np.sqrt(distance)
	return distance


#Collect the coordinates of the points of the data-set into a list of lists 
def data_array(data):
	points = [0]*len(data)
	for i in range(len(data)):
		points[i] = []
		for j in range(len(data[0])-1):
			points[i].append(float(data[i][j]))
	return points


def get_the_data():
	with open("iris.data", "r") as data:
		data_read = csv.reader(data)
		data_array = list(data_read)
	return data_array


#The two functions that made to check the accuracy of the model

def pairs_array(data):
	status = [data[i][-1] for i in range(len(data))] 
	attributes = [0]*len(data)
	attributes = [[float(iris[j]) for j in range(len(data[0])-1)] for iris in data]
	data_pairs = [[attribute, stat] for attribute, stat in zip(attributes, status)]
	return data_pairs

		
def confusion_matrix(clusters, data_pairs):
	c_matrix = [[] for cluster in clusters]
	for i in range(len(clusters)):
		c_matrix[i] = [0]*3
		for pair in data_pairs:
			for point in clusters[i]:
				if pair[0] == point[0]:
					if pair[1] == 'Iris-setosa':
						c_matrix[i][0] += 1
					elif pair[1] == 'Iris-versicolor':
						c_matrix[i][1] += 1
					else:
						c_matrix[i][2] += 1		
	print("The confusion matrix is:")
	for j in range(len(c_matrix[0])):
		for row in c_matrix:
			print(row[j], end = '	')
		print()


'''def check_the_model(clusters, data_pairs):
	for i in range(len(clusters)):
		print("The group of the cluster ", i+1, " is:")
		for j in range(len(clusters[i])):
			for a in range(len(data_pairs)):
				if clusters[i][j][0] == data_pairs[a][0]:
					print(data_pairs[a][-1], end = ", ")
		print()'''

	
#Displaing the squared distance error for each k on a coordinate system
def display(sum_error, largest_k):
	sum_error1 = sum_error[2:]
	xpos = [i for i in range(len(sum_error1))]
	plt.style.use('seaborn')
	plt.plot(xpos, sum_error1 , color = 'b', linewidth=2)
	plt.xticks(xpos, xpos)
	#plt.yscale('log')
	plt.title("The best k")
	plt.legend(["k"])
	plt.xlabel("k")
	plt.ylabel("squared distance error")
	plt.show()	

	
def main():

      #Get and arranges the data-set
	data = get_the_data()
	d_array = data_array(data)
	largest_k = int(input("Enter the largest k that you want to check: ")) + 1
	
      #Run the algorithm and find the best k for the clustering, the best k central-mass points, and the clusters that belongs to them	
	best_k, best_k_means, min_sum_error, best_clusters, sum_error = find_the_best_k(d_array, largest_k)
	print(f"The best k is: {best_k}, which provides the squared distance error: {round(min_sum_error, 2)}\n")
	display(sum_error, largest_k)
	
      #Now choose from the graph the specific k that you want to check, and display the confusion matrix for this k 	
	chosen_k = int(input("Enter the k that you chose to check: ")) 
	best_k_means, min_sum_error, best_clusters = clustering_loop(d_array, chosen_k)
     
      #Check the accuracy of the clustering
	pairs = pairs_array(data)
	c_matrix = confusion_matrix(best_clusters, pairs)
			
	
if __name__=="__main__":
	main()
	
