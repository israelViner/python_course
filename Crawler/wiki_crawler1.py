import requests
from bs4 import BeautifulSoup
import os
import random
from tqdm import tqdm


#Return list of url-addresses that belong to links & images  

def get_urls_link(url_link):
	urls_array = []
	html = requests.get(url_link, timeout=2.50)
	if html.status_code == 200:
		my_html = html.text
		soup = BeautifulSoup(my_html, 'html.parser')
		links = soup.find_all('a')
		for link in links:
			url = link.get('href',None)
			if url is not None and not url.startswith("#"):
				urls_array.append(fix_url(url))
	return urls_array 
	

def get_images_url(url_link):
	images_array = []
	try:
		html = requests.get(url_link, timeout=2.50)
		if html.status_code == 200:
			my_html = html.text
			soup = BeautifulSoup(my_html, 'html.parser')
			links = soup.find_all('img')
			for img in links:
				img_url = img.get('src', None)
				if img_url is not None:
					images_array.append(fix_url(img_url))
	except:
		print('Error')
	return images_array		
	

#Save the images from the url addresses to the dest_folder
def download_pic(dest_folder, images_url):
	os.chdir(dest_folder)
	for i in tqdm(range(len(images_url))):
		try:
			response = requests.get(images_url[i], timeout=2.50)
			if response.status_code == 200:
				image = open(f'{i}.png', 'wb')
				image.write(response.content)
				image.close()
		except:
			print('Unexpected error, unable to download the image')
	os.chdir('..')


#Return the correct url-address by adding the missing prefix (if exsists)
def fix_url(url):
	prefix_wiki = 'https://en.wikipedia.org'
	if url.startswith("https:") or url.startswith("http:"):
		return url
	elif url.startswith("//") or url.startswith("/author/"):
		url_fix = 'https:' + url
	else:
		url_fix = prefix_wiki + url
	return url_fix
		
	
def remove_duplicates(string_array):
	result = []
	for string in string_array:
		if string not in result:
			result.append(string)
	return result


#Return (& clean) the folder name from the last section of the url
def folder_name(page_link):
	split_url = page_link.split('/')
	if split_url[-1] == '':
		split_url[-1] = split_url[-2]
	split_url[-1] = split_url[-1].translate({ord(i): None for i in '!?#@%+*/$&'})
	split_url[-1] = split_url[-1].translate({ord(i): ' ' for i in '_-=)(][:'})
	return split_url[-1]


#The main function; create folder, get & clean the url-address and download the images from the page. repeat the procces in recursion
def crawl(page_link, depth, width):
	foldname = folder_name(page_link)
	if not os.path.isdir(foldname):
		os.mkdir(foldname)
		images_url = get_images_url(page_link)
		clean_urls = remove_duplicates(images_url)
		download_pic(foldname, clean_urls)
		if depth > 1 and width > 0:
			os.chdir(foldname)
			links_url = get_urls_link(page_link)
			width_places = random.sample(links_url, min(width, len(links_url)))
			for place in tqdm(width_places):
				crawl(place, depth - 1, width)
			os.chdir('..')
	

def main():
	page_link = input("Enter page link: ")
	depth =  int(input("Enter depth: "))
	width =  int(input("Enter width: "))
	crawl(page_link, depth, width)

	
if __name__=="__main__":
	main()

