class clip:


	def __init__(self, Name, year):
		self.name = Name
		self.year = year
		self.is_played = False
		
		
	def __repr__(self):
		return f'{self.name}:{str(self.year)}'
		
		
	def play(self):
		self.is_played = True
		
		
	def stop(self):
		self.is_played = False
