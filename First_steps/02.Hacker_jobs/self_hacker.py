import csv
from urllib.request import urlopen
import json
from tqdm import tqdm


#Get the list of ids of the 60 best works from Hacker News website 
def get_ids():
	try:
		with urlopen('https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty') as data:
			job_ids = json.loads(data.read())
		return job_ids
	except:
		print("An error occured in in the 'get_ids' function")


#Get specific gob details according to the id number
def get_job(id):
	try:
		with urlopen(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty') as job_s:
			job = json.loads(job_s.read())
			clean_job = [job.pop("id", None), job.pop("title", None), job.pop("url", None)]
		return clean_job
	except:
		print("An error occured in in the 'get_job' function")


#Get a list of specific details of the jobs according to a list of id numbers 
def get_all_jobs(job_ids):
	try:
		all_jobs = []
		for i in tqdm(job_ids):
			all_jobs.append(get_job(i))
		return all_jobs
	except:
		print("An error occured in in the 'get_all_jobs' function")


#Create csv file named <name_file> and write the details into the file		
def write_to_csv(name_file, data):
	try:
		with open(name_file, "w+") as file:
			writer = csv.writer(file) 
			writer.writerow(["id","title","url"])
			for row in data:
				writer.writerow(row)
	except:
		print("An error occured in in the 'write_to_csv' function")

#The main function
def main():
	name_file = input("enter name file: ")
	if not (len(name_file) > 4 and name_file.endswith(".csv")):
		raise Exception("Name file must end in '.csv'")
	try:
		ids = get_ids()
		data = get_all_jobs(ids)
		write_to_csv(name_file, data)
	except:
		print("something went wrong")
	

if __name__ == '__main__':
	main() 
