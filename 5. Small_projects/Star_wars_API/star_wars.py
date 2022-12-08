import json, csv, os, sys, random
from urllib.request import urlopen


#Get the wanted terms from the specific resource in the API page
def search_terms(resource, term):
	res = []
	if os.path.isfile(resource):
		with open(resource) as json_file:
			data_dict = json.load(json_file)
	else:	
		with urlopen(f'https://swapi.dev/api/{resource}') as repo:
			data_repo = json.load(repo)
		data_dict = data_repo["results"]
		write_to_file(resource, data_dict)
		print
	for data in data_dict:
		if any(term in d for d in data):
			res.append({data['name' if 'name' in data else 'title']: data[term]})
	return res, data_dict


#Sort the the planets data according to specific term
def sort_by_terms(order_field, reverse = False):
	res = []
	if os.path.isfile("planets"):
		with open('planets') as json_file:
			data_dict = json.load(json_file)
	else:
		with urlopen(f'https://swapi.dev/api/planets') as repo:
			data_repo = json.load(repo)
		data_dict = data_repo["results"]
		write_to_file("planets", data_dict)
	for data in sorted(data_dict, key = lambda x: int(x[order_field]) if x[order_field].isdigit() else (2**63-1 if x[order_field] == "unknown" else x[order_field]) ,reverse = reverse):
		print(data[order_field])
		res.append(data)
	return res

			
#Create file named <name_file> and write the details into the file		
def write_to_file(name_file, data):
	with open(name_file, "w") as outfile:
		json.dump(data, outfile)


def main():
	choose = sys.argv[1]
	arg1 = sys.argv[2]
	arg2 = sys.argv[3]
	if choose == "search":
		resource = arg1
		term = arg2
		data, data_dict = search_terms(resource, term)
		print(data)
	if choose == "sort":
		order_field = arg1
		reverse = arg2
		if reverse == "True":
			res = sort_nested_dict(order_field, True)
		else:
			res = sort_nested_dict(order_field)
		print(res)
		

if __name__=="__main__":
	main()
	

