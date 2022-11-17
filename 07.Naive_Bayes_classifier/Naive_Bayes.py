import random
import csv
import math


#Test the accuracy of the model on a testing-data
def test_the_model(testing_array, count_probabilities):
	count_poisoned = count_not_poisoned = 0
	for i in range(len(testing_array)):
		mushroom_probability = poisoned_probability(count_probabilities, testing_array[i][0])
		if mushroom_probability > 0.5 and testing_array[i][1] == 'p':
			count_poisoned += 1
		if mushroom_probability < 0.5 and testing_array[i][1] == 'e':
			count_not_poisoned += 1
	return count_poisoned, count_not_poisoned
		

#Check the probability of a mushroom - if it poisoned or not
def poisoned_probability(count_probabilities, mushroom):
	log_prob_if_poisoned = log_prob_if_not_poisoned = 0.0
	for i in range(len(mushroom)): 
		for attribute, prob_if_poisoned, prob_if_not_poisoned in count_probabilities[i]:
			if attribute in mushroom[i]:
				log_prob_if_poisoned += math.log(prob_if_poisoned)
				log_prob_if_not_poisoned += math.log(prob_if_not_poisoned)
			else:
				log_prob_if_poisoned += math.log(1.0 - prob_if_poisoned)
				log_prob_if_not_poisoned += math.log(1.0 - prob_if_not_poisoned)
	prob_if_poisoned = math.exp(log_prob_if_poisoned)
	prob_if_not_poisoned = math.exp(log_prob_if_not_poisoned)
	poisoned_prob = prob_if_poisoned / (prob_if_poisoned + prob_if_not_poisoned)
	return poisoned_prob


#Calculate the probability for each attribute in each subject
def attributes_probabilities(count_appearances, sum_poisoned, sum_not_poisoned, k=0.5):
	count_probabilities = [0]*len(count_appearances)
	for i in count_appearances:
		count_probabilities[i] = []
		for j, (poisoned, not_poisoned) in count_appearances[i].items():
			count_probabilities[i].append((j, (poisoned + k)/(sum_poisoned + 2*k), (not_poisoned + k)/(sum_not_poisoned + 2*k)))
	return count_probabilities


#Count the total sum of the poisoned/not poisoned mushrooms
def count_poisoned(training_array):
	sum_poisoned = sum_not_poisoned = 0
	for i in range(len(training_array)):
		if training_array[i][1] == 'p':
			sum_poisoned += 1
		else:
			sum_not_poisoned += 1
	return sum_poisoned, sum_not_poisoned


#Count the appearances of each attribute in poisoned/not poisoned mushrooms
def count_attributes(training_array, dict_attributes):
	for i in range(len(training_array)):
		for j in range(len(training_array[0][0])):
			dict_attributes[j][training_array[i][0][j]][0 if training_array[i][1] == 'p' else 1]+=1
	return dict_attributes


#Create dictionary in order to count the poisoned/not poisoned for each attribute
def create_dict_attributes(unique_attributes):
	dict_attributes = {}
	for i in range(len(unique_attributes)):
		dict_attributes[i] = {}
		for item in unique_attributes[i]:
			dict_attributes[i][item] = [0, 0]
	return dict_attributes
	

#Get the unique attributes from each column of the data-set 
def get_the_attributes(data_pairs):
	unique_attributes = []
	for j in range(len(data_pairs[0][0])):
		unique_attributes.append([])
		for i in range(len(data_pairs)):
			unique_attributes[j].append(data_pairs[i][0][j])
		unique_attributes[j] = set(unique_attributes[j])
	return unique_attributes
	

#Split the data to attributes and status and collect the data into an array of pairs in order to shuffle the data	
def pairs_array(data_array):
	status = [data_array[i][0] for i in range(len(data_array))] 
	attributes = [data_array[i][1:] for i in range(len(data_array))]
	data_pairs = [[attributes[i], status[i]] for i in range(len(data_array))]
	random.shuffle(data_pairs)
	return data_pairs


def get_the_data():
	with open("agaricus-lepiota.data", "r") as data:
		data_read = csv.reader(data)
		data_array = [row for row in data_read]
	return data_array
	

def main():
      #Get and arranges the data-set
	data_array = get_the_data()
	data_pairs = pairs_array(data_array)
	unique_attributes = get_the_attributes(data_pairs)
	dict_attributes = create_dict_attributes(unique_attributes)
	
      #Split the data to training and testing
	training_array = data_pairs[:int(len(data_pairs)*4/5)]
	testing_array = data_pairs[int(len(data_pairs)*4/5):]
	
      #Train the model
	sum_poisoned, sum_not_poisoned = count_poisoned(training_array)
	count_appearances = count_attributes(training_array, dict_attributes)
	calculate_probabilities = attributes_probabilities(count_appearances, sum_poisoned, sum_not_poisoned)
	
      #Test the model
	sum_test_poisoned, sum_test_not_poisoned = count_poisoned(testing_array)
	count_poisoned1, count_not_poisoned = test_the_model(testing_array, calculate_probabilities)
	print("The model is accurate in", count_poisoned1, "cases from", sum_test_poisoned, "poisonous mushrooms (",round(100 *count_poisoned1/sum_test_poisoned, 2),"%), and in", count_not_poisoned, "from", sum_test_not_poisoned, "not poisonous (", round(100 *count_not_poisoned/sum_test_not_poisoned, 2),"%)")
	print("The final grade of the model is: ", round(100 *(count_poisoned1 + count_not_poisoned)/(sum_test_poisoned + sum_test_not_poisoned), 2),"%")
	
	
if __name__=="__main__":
	main()
