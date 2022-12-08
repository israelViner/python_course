from clip import clip


class ArtClip(clip):

	def __init__(self, name, year, time):
		clip.__init__(self, name, year)
		self.time = time
		
		
	def __repr__(self):
		return f'{clip.__repr__(self)} ({self.time})' 
		
		
	def is_valid_for_euro(self):
		return self.time > 3
	
	
