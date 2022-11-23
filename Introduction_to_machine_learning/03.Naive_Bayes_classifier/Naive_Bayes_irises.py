import random
import csv
import math


#Test the accuracy of the model on a testing-data
def test_the_model(testing_array, count_probabilities):
	count_setosa = count_versicolor = count_virginica = 0
	for i in range(len(testing_array)):
		setosa_prob, versicolor_prob, virginica_prob = irises_probability(count_probabilities, testing_array[i][0])
		if versicolor_prob > setosa_prob and versicolor_prob > virginica_prob and testing_array[i][1] == 'Iris-versicolor':
			count_versicolor += 1
		elif virginica_prob > setosa_prob and virginica_prob > versicolor_prob and testing_array[i][1] == 'Iris-virginica':
			count_virginica += 1
		elif setosa_prob > versicolor_prob and setosa_prob > virginica_prob and testing_array[i][1] == 'Iris-setosa':
			count_setosa += 1
	return count_setosa, count_versicolor, count_virginica
		

#Check the probability of a iris - which of varieties it belongs
def irises_probability(count_probabilities, iris):
	log_prob_setosa = log_prob_versicolor = log_prob_virginica = 0.0
	for i in range(len(iris)): 
		for attribute, prob_setosa, prob_versicolor, prob_virginica in count_probabilities[i]:
			if attribute == int(iris[i]):
				log_prob_setosa += math.log(prob_setosa)
				log_prob_versicolor += math.log(prob_versicolor)
				log_prob_virginica += math.log(prob_virginica)
			else:
				log_prob_setosa += math.log(1.0 - prob_setosa)
				log_prob_versicolor += math.log(1.0 - prob_versicolor)
				log_prob_virginica += math.log(1.0 - prob_virginica)
	prob_setosa = math.exp(log_prob_setosa)
	prob_versicolor = math.exp(log_prob_versicolor)
	prob_virginica = math.exp(log_prob_virginica)
	
	setosa_prob = prob_setosa / (prob_setosa + prob_versicolor + prob_virginica)
	versicolor_prob = prob_versicolor / (prob_setosa + prob_versicolor + prob_virginica)
	virginica_prob = prob_virginica / (prob_setosa + prob_versicolor + prob_virginica)
	
	return setosa_prob, versicolor_prob, virginica_prob


#Calculate the probability for each attribute in each subject
def attributes_probabilities(count_appearances, sum_setosa, sum_versicolor, sum_virginica, k=0.5):
	count_probabilities = [0]*len(count_appearances)
	for i in count_appearances:
		count_probabilities[i] = []
		for j, (setosa, versicolor, virginica) in count_appearances[i].items():
			count_probabilities[i].append((j, (setosa + k)/(sum_setosa + 2*k), (versicolor + k)/(sum_versicolor + 2*k), (virginica + k)/(sum_virginica + 2*k)))
	return count_probabilities


#Count the total sum of the setosa/versicolor/virginica irises
def count_irises(training_array):
	sum_setosa = sum_versicolor = sum_virginica = 0
	for i in range(len(training_array)):
		if training_array[i][1] == 'Iris-setosa':
			sum_setosa += 1
		elif training_array[i][1] == 'Iris-versicolor':
			sum_versicolor += 1
		else:
			sum_virginica += 1
	return sum_setosa, sum_versicolor, sum_virginica


#Count the appearances of each leaf-size in setosa/versicolor/virginica irises
def count_attributes(training_array, dict_attributes):
	for i in range(len(training_array)):
		for j in range(len(training_array[0][0])):
			dict_attributes[j][int(training_array[i][0][j])][0 if training_array[i][1] == 'Iris-setosa' else 1 if training_array[i][1] =='Iris-versicolor' else 2]+=1
	return dict_attributes


#Create dictionary in order to count the setosa/versicolor/virginica irises for each leaf-size
def create_dict_attributes(unique_attributes):
	dict_attributes = {}
	for i in range(len(unique_attributes)):
		dict_attributes[i] = {}
		for item in unique_attributes[i]:
			dict_attributes[i][item] = [0, 0, 0]
	return dict_attributes
	

#Get the unique attributes from each column of the data-set 
def get_the_attributes(data_pairs):
	unique_attributes = []
	for j in range(len(data_pairs[0][0])):
		unique_attributes.append([])
		for i in range(len(data_pairs)):
			unique_attributes[j].append(int(data_pairs[i][0][j]))
		unique_attributes[j] = set(unique_attributes[j])
	return unique_attributes
	

#Split the data to attributes and status and collect the data into an array of pairs in order to shuffle the data	
def pairs_array(data_array):
	status = [data_array[i][-1] for i in range(len(data_array))] 
	attributes = [0]*len(data_array)
	for i in range(len(data_array)):
		attributes[i] = []
		for j in range(len(data_array[0])-1):
			attributes[i].append(float(data_array[i][j]))
	data_pairs = [[attributes[i], status[i]] for i in range(len(data_array))]
	random.shuffle(data_pairs)
	return data_pairs


def get_the_data():
	with open("iris.data", "r") as data:
		data_read = csv.reader(data)
		data_array = list(data_read)
	return data_array
	

def main():
      #Get and arranges the data-set
	data_array = get_the_data()
	data_pairs = pairs_array(data_array)
	unique_attributes = get_the_attributes(data_pairs)
	dict_attributes = create_dict_attributes(unique_attributes)
	
      #Split the data to training and testing
	training_array = data_pairs[:int(len(data_pairs)*1/2)]
	testing_array = data_pairs[int(len(data_pairs)*1/2):]
	
      #Train the model
	sum_setosa, sum_versicolor, sum_virginica = count_irises(training_array)
	count_appearances = count_attributes(training_array, dict_attributes)
	calculate_probabilities = attributes_probabilities(count_appearances, sum_setosa, sum_versicolor, sum_virginica, 0.5)
	
      #Test the model
	sum_setosa, sum_versicolor, sum_virginica = count_irises(testing_array)
	count_setosa, count_versicolor, count_virginica = test_the_model(testing_array, calculate_probabilities)
	print("The model is accurate in", count_setosa, "cases from", sum_setosa, "setosa irises (",round(100 *count_setosa/sum_setosa, 2),"%), and in", count_versicolor, "from", sum_versicolor, "versicolor irises (", round(100 *count_versicolor/sum_versicolor, 2),"%), and in", count_virginica, "from", sum_virginica, "virginica irises (", round(100 *count_virginica/sum_virginica, 2),"%)")
	print("The final grade of the model is: ", round(100 *(count_setosa + count_versicolor + count_virginica)/(sum_setosa + sum_versicolor + sum_virginica), 2),"%")
	
	
if __name__=="__main__":
	main()
