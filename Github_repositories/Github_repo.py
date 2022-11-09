import json
import numpy as np
from matplotlib import pyplot as plt
from urllib.request import urlopen
from tqdm import tqdm
from sklearn.linear_model import LinearRegression


#The two functions that get the repositories from the API page

def get_repositories(sufix_link):
	with urlopen('https://api.github.com/search/repositories' + sufix_link) as repo:
		data_repo = json.load(repo)
	return data_repo['items']


def search_repositories(num):
	sufix_link = '?q=language:python&per_page=100&page='+ str(num)
	return sufix_link


#Collect the repositories from the chosen number of pages to an array of repositories 
def collect_repositories_pages(num_page):
	repositories_list = []
	for i in tqdm(range(1, num_page + 1)):
		page = get_repositories(search_repositories(i))
		for repo in tqdm(page):
			repositories_list.append(repo)
	print(len(repositories_list))
	return repositories_list


#Get the specific wanted data from an array of repositories
def split_repsitories(repositories_list):
	stars = []
	forks = []
	for repo in repositories_list:
		stars.append(repo.pop('stargazers_count')) 
		forks.append(repo.pop('forks_count'))
	return 	np.array(stars).reshape((-1, 1)), np.array(forks)


#The model of Linear Regression - fit the model with 2/3 of the array and then predict the result for the rest of it
def linear_regresion(x, y):
	stars_test = x[2::3]
	forks_test = y[2::3]
	stars_train = np.delete(x ,np.s_[2::3]).reshape((-1, 1))    #np.delete(x, np.arange(len(x), 3)).reshape((-1, 1))
	forks_train = np.delete(y ,np.s_[2::3])                     #np.delete(y, np.arange(len(y), 3)) 
	#print(stars_test[:25], stars_train[:25], print(len(stars_test)), print(len(stars_train))
	model = LinearRegression().fit(stars_train, forks_train)
	line_train = model.predict(stars_train)
	#predict_test = model.predict(stars_test)
	score = model.score(stars_test, forks_test)
	print(f"coefficient of determination: {score}")
	return line_train, stars_train, forks_train, stars_test, forks_test
	

#Displaing the results on a coordinate system
def display(line_train, stars_train, forks_train, stars_test, forks_test):
	plt.scatter(stars_train, forks_train, color = "black")
	plt.scatter(stars_test, forks_test, color="red")	
	plt.plot(stars_train, line_train, color="blue", linewidth=2)
	plt.xticks(stars_train)
	plt.yticks(forks_train)
	plt.show()


def main():
	data_repository = collect_repositories_pages(int(input("Enter number of repository pages: ")))
	stars , forks = split_repsitories(data_repository)
	line_train, stars_train, forks_train, stars_test, forks_test = linear_regresion(stars, forks)
	display(line_train, stars_train, forks_train, stars_test, forks_test)
	

if __name__=="__main__":
	main()
	

