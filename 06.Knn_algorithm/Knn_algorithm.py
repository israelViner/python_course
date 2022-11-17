from matplotlib import pyplot as plt
import numpy as np 
import random
import math

#For throwing a certain warning 
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

ITER_TRAIN = 100


#Check the distance between 2 points by L2 model
def check_distance(point, test):
	distance = 0
	for i in range(len(point)):
		distance += (point[i] - test[i])**2 
	distance = np.sqrt(distance)
	return distance


#Send all of the points in the array to check distance, and return the k closest ones 
def array_distance(data_train, data_test, index, k):
	distance = [0]*len(data_train)
	i = 0
	for j in range(len(data_train)):
		distance[i] = [check_distance(data_test[index], data_train[j]), i]
		i += 1
	return sorted(distance)


#Determine the group acoording to the groups of its neigbhors
def determine_group(names_data_train, k_neigbhor, k):
	k_neigbhor = k_neigbhor[1:k + 1]
	groop = []
	for neigbhor in k_neigbhor:
		groop.append(names_data_train[neigbhor[1]])
	return max(set(groop), key = groop.count)
		

#Send to check distance to determine the group	
def knn(data_train, names_data_train, data_test, index, k):
	k = k
	k_neigbhor = array_distance(data_train, data_test, index, k)
	groop = determine_group(names_data_train, k_neigbhor, k)
	return groop
	

#Calculate the prediction successes for all the data
def knn_on_array(data_train, names_data_train, data_test, names_data_test, k):
	counter = 0
	for index in range(len(data_test)):
		group = knn(data_train, names_data_train, data_test, index, k)
		if group == names_data_test[index]:
			counter += 1
	return counter
	
	
#Test the prediction of each k 100 times, in order to find the best k
def find_the_best_k(data_pairs, largest_k):
	precision = [0] * largest_k
	for i in range(ITER_TRAIN):
		k = 1
		d_train, names_train, d_test, names_test = split_array(data_pairs)
		while k < largest_k:
			precision[k] += knn_on_array(d_train, names_train, d_test, names_test, k)
			k += 1
	for i in range(len(precision)):
		precision[i] = round(precision[i]/(len(d_test)), 2)
	print(precision)
	max_presicion = max(precision)
	best_k = precision.index(max_presicion)
	return best_k, max_presicion, precision
	

#Split the pairs array randomly to two sets: train arrays and test arrays  
def split_array(data_pairs):
	np.random.shuffle(data_pairs)
	middle = int(len(data_pairs)*2/3)
	d_train = data_pairs[:middle,0] 
	names_train = data_pairs[:middle,1]
	d_test = data_pairs[middle:,0] 
	names_test = data_pairs[middle:,1]
	return d_train, names_train, d_test, names_test


#Split the pairs array to data array and names array  	
def split_all_array(data_pairs):
	data = data_pairs[:,0] 
	names = data_pairs[:,1]
	print("the len of data is: ", len(data))
	return data, names


#Collect the data into an array of pairs in order to shuffle the data 
def pairs_array(data_array, data_names):
	data_pairs = []
	array = np.arange(len(data_array))
	np.random.shuffle(array)
	for ar in array:
		data_pairs.append([data_array[ar], data_names[ar]])
	return data_pairs
	
	
#Displaing the results on a coordinate system
def display(precision):
	precision1 = precision[1:]
	xpos = np.arange(len(precision1))
	plt.style.use('seaborn')
	plt.bar(xpos, precision1)
	#plt.plot(xpos, precision1 , color = 'r', linewidth=2)
	plt.xticks(xpos, xpos)
	plt.ylim([94,97])
	plt.style.use('seaborn')
	plt.title("The best k")
	plt.legend(["k"])
	plt.ylabel("k")
	plt.show()

	
def main():
	max_k = input("Enter the largest k that do you want to check: ")
	
     #Get the data
	data_array = np.loadtxt('iris.data',usecols = [0,1,2,3] ,skiprows = 1 ,dtype = 'float', delimiter = ',')
	data_names = np.loadtxt('iris.data', usecols = [4], skiprows = 1 ,dtype = 'str', delimiter = ',')
	
     #Create array of pairs - data & names, and replace the names to numbers
	data_pairs = np.array(pairs_array(data_array, data_names), dtype=object)
	data_pairs[data_pairs == 'Iris-setosa'] = 1
	data_pairs[data_pairs == 'Iris-virginica'] = 2
	data_pairs[data_pairs == 'Iris-versicolor'] = 3
	
     #Find the best k in the range between 1 and the chosen k
	best_k, max_precision, precision = find_the_best_k(data_pairs, int(max_k))
	print("The best number k is: ", best_k, " and it succeeded to predict in ", max_precision, "% of the cases")
	display(precision)
		
	
if __name__=="__main__":
	main()
