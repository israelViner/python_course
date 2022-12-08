from Company import Company 
import random

class Ceo:
	
		
	def __init__(self, Name):
		self.ceo_name = Name
		
	
	def __repr__(self):
		return self.ceo_name
	
		
	def add_project(self, project, company):
		company.update_project({project: f"{self.ceo_name}"})	
		
	
	def update_project(self, project, company, name = 0):
		if name == 0:
			company.update_project({project: f'{name}'})
		elif random.random() > 0.5:
			company.update_project({project: f'{name}'})
		else:
			print("The update request was rejected")
			
			
	def remove_project(self, project, company, name = 'ceo'):
		if name == 'ceo':
			company.remove_project(project)
		elif random.random() > 0.5:
			company.remove_project(project)
		else:
			print("The deletion request was rejected")
			
				
	

