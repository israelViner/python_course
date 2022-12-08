from clip import clip
from ArtClip import ArtClip
from Player import Player


def main():
	avraham_fried = clip("yomim", 1983)
	madona = ArtClip("like_a", 1999, 4)
	rihana = ArtClip("stay", 2011, 2)
	tailor = ArtClip("midnights", 2022, 5)
	bily = clip("tv", 2021)
	
	print(avraham_fried)
	print(avraham_fried.is_played)
	avraham_fried.play()
	print(avraham_fried.is_played)
	
	print(rihana)
	print(madona)
	print(tailor)
	print(bily)
	
	print(madona.is_valid_for_euro())
	print(rihana.is_valid_for_euro())
	
	clips = [avraham_fried, madona, rihana, bily, tailor]
	new_list = Player(clips)
	
	print(new_list.clips)
	
	print("The shuffle clips is: ")
	new_list.shuffle()
	print(new_list.clips)
	
	
	print("The process of the next method is shown below: ")
	
	for cl in  new_list.clips:
		print("The ststus of the clip is: " ,cl.is_played)
		
	new_list.__next__()
	
	print()
	
	for cl in  new_list.clips:
		print("The ststus of the clip is: " ,cl.is_played)
	
	new_list.__next__()
	print()
	for cl in  new_list.clips:
		print("The ststus of the clip is: " ,cl.is_played)
	
	
	new_list.__next__()
	print()
	for cl in  new_list.clips:
		print("The ststus of the clip is: " ,cl.is_played)
	
	
	new_list.__next__()
	print()
	for cl in  new_list.clips:
		print("The ststus of the clip is: " ,cl.is_played)
		
	new_list.__next__()
	print()
	for cl in  new_list.clips:
		print("The ststus of the clip is: " ,cl.is_played)
	
	
	new_list.__next__()
	print()
	for cl in  new_list.clips:
		print("The ststus of the clip is: " ,cl.is_played)
	
	
	
	

if __name__ == "__main__":
	main() 
