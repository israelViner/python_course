from clip import clip
from ArtClip import ArtClip
import random


class Player:

	def __init__(self, clips):
		self.clips = clips
		self.current = -1
		for clip in clips:
			clip.stop()
		
		
	def __next__(self):
		if not self.clips:
			raise ValueError
		if not self.current == -1:
			self.clips[self.current].stop()
		if self.current == len(self.clips) - 1:
			self.current = 0
		else:
			self.current += 1
		self.clips[self.current].play()
				
				
	def shuffle(self):
		for i in range(len(self.clips)):
			temp = random.randint(0, len(self.clips)-1) 
			self.clips[i], self.clips[temp] = self.clips[temp], self.clips[i]
			
		
		
		
		
