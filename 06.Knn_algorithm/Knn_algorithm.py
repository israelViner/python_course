from matplotlib import pyplot as plt
import numpy as np 
import random
import math

#For throwing a certain warning 
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
#print('x' in np.arange(5)) 


#Check the distance between 2 points by L2 model
def check_distance(point, test):
	distance = 0
	for i in range(len(point)):
		distance += (point[i] - test[i])**2 
	distance = np.sqrt(distance)
	return distance


#Send all of the points in the array to check distance, and return the k closest ones 
def array_distance(data, index, k):
	distance = [0]*len(data)
	i = 0
	for point in data:
		distance[i] = [check_distance(data[index], point), i]
		i += 1
	return sorted(distance)


#Determine the group acoording to the groups of its neigbhors
def determine_group(names_data, k_neigbhor, k):
	k_neigbhor = k_neigbhor[1:k + 1]
	groop = []
	for neigbhor in k_neigbhor:
		groop.append(names_data[neigbhor[1]])
	return max(set(groop), key = groop.count)
		

#Send to check distance to determine the group	
def knn(data_array, data_names, index, k):
	k = k
	k_neigbhor = array_distance(data_array, index, k)
	groop = determine_group(data_names, k_neigbhor, k)
	return groop
	

#Calculate the prediction successes for all the data
def loop_knn(data_array, data_names, k):
	counter = 0
	for index in range(len(data_array)):
		group = knn(data_array, data_names, index, k)
		if group == data_names[index]:
			counter += 1
	return counter
	
	
#Test the prediction of each k 100 times, in order to find the best k
def find_the_best_k(data_pairs, largest_k):
	k = 1
	precision = [0] * largest_k
	while k < largest_k:
		for i in range(100):
			d_train, names_train, d_test, names_test = split_array(data_pairs)
			precision[k] += loop_knn(d_train, names_train, k)
		precision[k] = round(precision[k]/(len(d_train)), 2)
		print("The k now is: ", k)
		k += 1
	print(precision)
	max_presicion = max(precision)
	best_k = precision.index(max_presicion)
	return best_k, max_presicion
	

#Collect the data into an array of pairs in order to shuffle the data 
def pairs_array(data_array, data_names):
	data_pairs = []
	array = np.arange(len(data_array))
	np.random.shuffle(array)
	for ar in array:
		data_pairs.append([data_array[ar], data_names[ar]])
	return data_pairs


#Split the pairs array randomly to two sets: train arrays and test arrays  
def split_array(data_pairs):
	middle = int(len(data_pairs)*2/3)
	d_train = data_pairs[:middle,0] 
	names_train = data_pairs[:middle,1]
	d_test = data_pairs[middle:,0] 
	names_test = data_pairs[middle:,1]
	#print("The len of the test array is: ", len(d_test))
	return d_train, names_train, d_test, names_test

	
#Calculate the prediction successes for all the data
#def loop_knn_pred(d_test, names_test, d_train, names_train, k):
#	counter = 0
#	for index in range(len(d_test)):
#		group = knn(data_array, data_names, index, k)
#		if group == data_names[index]:
#			counter += 1
#	return counter


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
	best_k, precision = find_the_best_k(data_pairs, int(max_k))
	print("The best number k is: ", best_k, " and it succeeded to predict in ", precision, "% of the cases")
	
     #Check the precision of the model on a test train
	d_train, names_train, d_test, names_test = split_array(data_pairs)
	predict_grade = loop_knn(d_test, names_test, best_k)
	print("The model is accurate in ", predict_grade, " from ", len(d_test), " cases, and the grade is: ", round(predict_grade/len(d_test)*100,2),"%")
	
	
	
if __name__=="__main__":
	main()
