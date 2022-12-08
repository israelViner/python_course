

class Company:

	def __init__(self, company_data = {}):
		self.company_data = company_data
		
			
	def remove_project(self, project):
		self.company_data.pop(project)	
	
		
	def update_project(self, project):
		key = list(project.keys())[0]
		self.company_data[key] = project[key]
		
	
	def __repr__(self):
		return f'{self.company_data}'
	
