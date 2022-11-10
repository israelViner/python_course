import json
import random
import numpy as np
from matplotlib import pyplot as plt
from urllib.request import urlopen
from tqdm import tqdm
from sklearn.linear_model import LinearRegression


#Get the repositories from the API page
def get_repositories(page_num):
	with urlopen(f'https://api.github.com/search/repositories?q=language:python&per_page=100&page={page_num}') as repo:
		data_repo = json.load(repo)
	return data_repo['items']


#Collect the repositories from the chosen number of pages to an array of repositories 
def collect_repositories_pages(num_pages):
	repositories_list = []
	for i in tqdm(range(num_pages)):
		num_page = i + 1
		page = get_repositories(num_page)
		for repo in tqdm(page):
			repositories_list.append(repo)
	print(len(repositories_list))
	return repositories_list


#Get the specific wanted data from an array of repositories
def split_repsitories(repositories_list):
	specific_data = []
	for repo in repositories_list:
		specific_data.append([repo['stargazers_count'], repo['forks_count']]) 
	return np.array(specific_data)


#The model of Linear Regression - fit the model with 2/3 of the array and then predict the result for the rest of it
def linear_regresion(specific_data): 
	random.shuffle(specific_data)
	middle = int(len(specific_data)*2/3)
	stars_test = specific_data[middle:,0].reshape((-1, 1)) 
	forks_test = specific_data[middle:,1]
	stars_train = specific_data[:middle,0].reshape((-1, 1)) 
	forks_train = specific_data[:middle,1]
	#print(len(stars_test), len(stars_train))
	model = LinearRegression().fit(stars_train, forks_train)
	line_train = model.predict(stars_train)
	score = model.score(stars_test, forks_test)
	print(f"The score is: {score}")
	return line_train, stars_train, forks_train, stars_test, forks_test
	

#Displaing the results on a coordinate system
def display(line_train, stars_train, forks_train, stars_test, forks_test):
	plt.scatter(stars_train, forks_train, color = "blue")
	plt.scatter(stars_test, forks_test, color="red")	
	plt.plot(stars_train, line_train, color="black", linewidth=2)
	plt.xticks()
	plt.yticks()
	plt.show()


def main():
	data_repository = collect_repositories_pages(int(input("Enter number of repository pages: ")))
	specific_data = split_repsitories(data_repository)
	#stars , forks = split_repsitories(data_repository)
	line_train, stars_train, forks_train, stars_test, forks_test = linear_regresion(specific_data)
	display(line_train, stars_train, forks_train, stars_test, forks_test)
	

if __name__=="__main__":
	main()
	

