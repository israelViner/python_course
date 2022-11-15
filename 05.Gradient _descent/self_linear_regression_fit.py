from matplotlib import pyplot as plt
import numpy as np 
import random
import math


#Calculate the gradient vector
def Gradient_calculate(X_train, Y_train, teta1, teta2, weight_array):
	der_teta1 = 0
	der_teta2 = 0
	for i in range(len(Y_train)):
		der_teta1 += (teta1 + teta2*X_train[i] - Y_train[i]) * weight_array[i]
		der_teta2 += (teta1 + teta2*X_train[i] - Y_train[i]) * X_train[i] * weight_array[i]
	return der_teta1, der_teta2

	
#Find the best equasion line for the array train	
def gradient_descent(X_train, Y_train, weight_array, iteration = 2000):
	teta1, teta2 = 1, 1
	i = 0
	iteration = iteration
	epsilon = 1
	learning_rate = 10**-3
	while i < iteration and epsilon > 0.001:
		der_teta1, der_teta2 = Gradient_calculate(X_train, Y_train, teta1, teta2, weight_array) 
		teta1 = teta1 - der_teta1*learning_rate
		teta2 = teta2 - der_teta2*learning_rate
		epsilon = max(abs(der_teta1), abs(der_teta2))
		#print(f"the cost for iteration {iteration} is: ", f_cost(X_train, Y_train, teta1, teta2, weight_array), "and the gradiant is: ",  der_teta1, der_teta2)
		i += 1
	return teta1, teta2

	
#The model of Linear Regression - fit the model with 4/5 of the array and then predict the result for the rest of it
def linear_regression_fit_and_test(X_array, Y_array, weight_array, iteration): 
	data_pairs = pairs_array(X_array, Y_array)
	len_d = len(data_pairs)
	print(len_d)
	middle = int(len(data_pairs)*1/5)
	X_train = data_pairs[middle:,0] 
	Y_train = data_pairs[middle:,1]
	X_test = data_pairs[:middle,0] 
	Y_test = data_pairs[:middle,1]
	teta1, teta2 = gradient_descent(X_train, Y_train, weight_array, iteration)
	line_data = line(X_train, teta1, teta2)
	print(f'The equasion of the line is: y = {teta2:.2f}x + {teta1:.2f}')
	print(f"The coefficient_of_determination is: {calculate_coefficient_of_determination(X_test, Y_test, teta1, teta2):.3f}")
	return line_data, X_train, Y_train, X_test, Y_test 


#Collect the data into array of pairs in order to shuffle the split the data 
def pairs_array(X_array, Y_array):
	data_pairs = []
	array = np.arange(100)
	np.random.shuffle(array)
	for ar in array:
		data_pairs.append([X_array[ar], Y_array[ar]])
	return np.array(data_pairs)
	

#Calculate the precision measure of the model	
def calculate_coefficient_of_determination(X_test, Y_test, teta1, teta2):
	y_minus_f = 0
	y_minus_mean = 0
	for i in range(len(X_test)):
		y_minus_f += (teta1 + teta2*X_test[i] - Y_test[i])**2
		y_minus_mean += (Y_test[i] - sum(Y_test)/len(Y_test))**2
	coefficient_of_determination = 1 - y_minus_f/y_minus_mean
	return coefficient_of_determination


#Displaing the results on a coordinate system
def display(line_data, X_train, Y_train, X_test, Y_test):
	plt.scatter(X_train, Y_train, color = "blue")
	plt.scatter(X_test, Y_test, color="red")	
	plt.plot(X_train, line_data , color = 'black', linewidth=2)
	plt.xticks()
	plt.yticks()
	plt.show()


#The cost of the difference between the prediction and the correct location of the points		
def f_cost(X_array, Y_array, teta1, teta2, weight_array):
	cost = 0
	for i in range(len(X_array)):
		cost += ((teta1 + teta2*X_array[i] - Y_array[i])**2) * weight_array[i]
	return cost


#Calculate and determine the weight of each term of the data 		
def weight(X_array):
	median = np.median(X_array)
	weight_array = -((X_array - median) ** 2) + max(abs(max(X_array) - median), abs(min(X_array) - median))**2 + 0.01
	sum_weights = sum(weight_array)
	weight_array = weight_array/sum_weights
	return weight_array
	

#Calculate the line to display it		
def line(X_train, teta1, teta2):
	line_data = np.zeros(len(X_train))
	line_data = teta1 + teta2*X_train 
	return line_data	

	
def main():
	data_set = np.load('XYdata.npz') 
	X_array =  data_set['array_1'] #np.random.randint(1,1000,200)  #np.random.uniform(0, 200, 100)          
	Y_array =  data_set['array_2']
	iteration = int(input("Enter numbur of iterations: ")) 
	weight_array = weight(X_array) 
	line_data, X_train, Y_train, X_test, Y_test = linear_regression_fit_and_test(X_array, Y_array, weight_array, iteration)
	display(line_data, X_train, Y_train, X_test, Y_test)
	
	
if __name__=="__main__":
	main()#Calculate the line to display it	
