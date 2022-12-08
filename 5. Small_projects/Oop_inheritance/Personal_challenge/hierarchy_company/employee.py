from Company import Company 
from Team_leader import Team_leader 


class employee:
	
	
	def __init__(self, Name, team_leader):
		self.employee_name = Name
		self.team_leader = team_leader
		self.team_leader.add_team_member(self.employee_name)
		
	
	def __repr__(self):
		return f'The employee name is: {self.employee_name}'
		
		
	def remove_project(self, project, company):
		if self.employee_name == company.company_data[project]:
			company.remove_project(project)
		else:
			self.team_leader.remove_project(project, self.employee_name, company)
		
		
	def add_project(self, project, company):
		company.update_project({project: f"{self.employee_name}"})
	
	
	def update_project(self, project, company):
		if self.employee_name == company.company_data[project]:
			company.update_project({project: f"{self.employee_name}"})
		else:
			self.team_leader.update_project(project, company, self.employee_name)
