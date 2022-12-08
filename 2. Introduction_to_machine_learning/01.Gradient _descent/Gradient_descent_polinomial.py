from matplotlib import pyplot as plt
import numpy as np 


#Calculate the gradient vector
def Gradient(X_array, Y_array, teta1, teta2, teta3):
	der_teta1 = 0
	der_teta2 = 0
	der_teta3 = 0
	for i in range(len(Y_array)):
		der_teta1 += teta1 + teta2*X_array[i] + + teta3*(X_array[i]**2) - Y_array[i]
		der_teta2 += (teta1 + teta2*X_array[i] + teta3*(X_array[i]**2) - Y_array[i]) * X_array[i]
		der_teta3 += (teta1 + teta2*X_array[i] + teta3*(X_array[i]**2) - Y_array[i]) * (X_array[i]**2)
	return der_teta1, der_teta2, der_teta3
	

#Find the best polynomial line for the array train		
def Linear_regression(X_array, Y_array, iteration = 2000):
	teta1, teta2, teta3 = 1, 1, 1
	epsilon = 1
	gama = 0.000001
	iteration = iteration
	i = 0
	while i < iteration and abs(epsilon) > 0.001:
		der_teta1, der_teta2, der_teta3 = Gradient(X_array, Y_array, teta1, teta2, teta3) 
		teta1 = teta1 - (der_teta1*gama)#*2/len(X_array)
		teta2 = teta2 - (der_teta2*gama)#*2/len(Y_array)
		teta3 = teta3 - (der_teta3*gama)#*2/len(Y_array)
		epsilon = max(der_teta1, der_teta2, der_teta3)
		#print(f"the cost for iteration {i} is: ", f_cost(X_array, Y_array, teta1, teta2, teta3), "and the gradiant is: ",  der_teta1, der_teta2, der_teta3)
		i += 1
	print(f"The coefficient_of_determination is: {calculate_coefficient_of_determination(X_array, Y_array, teta1, teta2, teta3):.3f}")
	return teta1, teta2, teta3
	

#The cost of the difference between the prediction and the correct location of the points			
def f_cost(X_array, Y_array, teta1, teta2, teta3):
	cost = 0
	for i in range(len(X_array)):
		cost += (teta1 + teta2*X_array[i] + teta3*(X_array[i]**2) - Y_array[i])**2
	return cost


#Calculate the line to display it			
def line(X_array, teta1, teta2, teta3):
	line_data = np.zeros(len(X_array))
	line_data = teta1 + teta2*X_array + teta3*(X_array**2)
	return line_data

	
#Calculate the precision measure of the model	
def calculate_coefficient_of_determination(X_array, Y_array, teta1, teta2, teta3):
	y_minus_f = 0
	y_minus_mean = 0
	for i in range(len(X_array)):
		y_minus_f += (teta1 + teta2*X_array[i] + teta3*(X_array[i]**2) - Y_array[i])**2
		y_minus_mean += (Y_array[i] - sum(Y_array)/len(Y_array))**2
	coefficient_of_determination = 1 - y_minus_f/y_minus_mean
	return coefficient_of_determination

	
#Displaing the results on a coordinate system
def display(X_array, Y_array, teta1, teta2, teta3):
	line_data = line(X_array, teta1, teta2, teta3)
	x_axis = np.linspace(0, 10, 100)
	plt.plot(x_axis, line_data, color = "red")
	plt.scatter(X_array, Y_array, color = "blue")
	plt.xticks()
	plt.yticks()
	plt.show()
	
	
def main():
	data_set = np.load('XYdata.npz') 
	X_array = data_set['array_1']
	Y_array = data_set['array_2']
	iteration = int(input("Enter the number of iterations: "))
	teta1, teta2, teta3 = Linear_regression(X_array, Y_array, iteration)
	print(f'The polynomial equasion is: y = {teta3:.2f}x^2 + {teta2:.2f}x + {teta1:.2f}')
	display(X_array, Y_array, teta1, teta2, teta3)
	
	
if __name__=="__main__":
	main()
