from matplotlib import pyplot as plt
import numpy as np 
import statistics


#Calculate the gradient vector
def Gradient(X_array, Y_array, teta1, teta2, weight_array):
	der_teta1 = 0
	der_teta2 = 0
	for i in range(len(Y_array)):
		der_teta1 += (teta1 + teta2*X_array[i] - Y_array[i]) * weight_array[i]
		der_teta2 += ((teta1 + teta2*X_array[i] - Y_array[i]) * X_array[i]) * weight_array[i]
	return der_teta1, der_teta2
	

#Find the best equasion line for the array train		
def Linear_regression(X_array, Y_array, weight_array, iteration = 2000):
	teta1, teta2 = 1, 1
	i = 0
	epsilon = 1
	learning_rate = 0.001
	iteration = iteration
	while i < iteration and abs(epsilon) > 0.001:
		der_teta1, der_teta2 = Gradient(X_array, Y_array, teta1, teta2, weight_array) 
		teta1 = teta1 - (der_teta1*learning_rate) 
		teta2 = teta2 - (der_teta2*learning_rate) 
		epsilon = max(abs(der_teta1), abs(der_teta2))
		#print(f"the cost for iteration {i} is: ", f_cost(X_array, Y_array, teta1, teta2, weight_array), "and the gradiant is: ",  der_teta1, der_teta2)
		i += 1
	print(f"The coefficient_of_determination is: {calculate_coefficient_of_determination(X_array, Y_array, teta1, teta2):.3f}")
	return teta1, teta2
	
	
#Displaing the results on a coordinate system
def display(X_array, Y_array, teta1, teta2):
	line_data = line(X_array, teta1, teta2)
	x_axis = np.linspace(0, 10, 100)
	plt.plot(x_axis, line_data , color = 'r', linewidth=2)
	plt.scatter(X_array, Y_array, color = "blue")
	plt.xticks()
	plt.yticks()
	plt.show()

	
#Calculate the precision measure of the model	
def calculate_coefficient_of_determination(X_array, Y_array, teta1, teta2):
	y_minus_f = 0
	y_minus_mean = 0
	for i in range(len(X_array)):
		y_minus_f += (teta1 + teta2*X_array[i] - Y_array[i])**2
		y_minus_mean += (Y_array[i] - sum(Y_array)/len(Y_array))**2
	coefficient_of_determination = 1 - y_minus_f/y_minus_mean
	return coefficient_of_determination


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
def line(X_array, teta1, teta2):
	line_data = np.zeros(len(X_array))
	line_data = teta1 + teta2*X_array 
	return line_data
	
	
def line_polynomial(X_array, teta1, teta2, teta3):
	line_data = np.zeros(len(X_array))
	line_data_array = teta1 + teta2*X_array + teta3*(X_array**2)
	return line_data_array

	
def main():
	data_set = np.load('XYdata.npz') 
	X_array = data_set['array_1']
	Y_array = data_set['array_2']
	weight_array = weight(X_array)
	iteration = int(input("Enter numbur of iterations: "))
	teta1, teta2 = Linear_regression(X_array, Y_array, weight_array, iteration)
	print(f'The equasion line is: y = {teta2:.2f}x + {teta1:.2f}')
	display(X_array, Y_array, teta1, teta2)
	
	
if __name__=="__main__":
	main()
