from Company import Company 
from Ceo import Ceo
import random


class Team_leader:
	
	
	def __init__(self, Name, team_members = []):
		self.team_leader_name = Name
		self.team_members = team_members
		self.team_members.append(self.team_leader_name)
		
	
	def __repr__(self):
		return f'The team_leader is: {self.team_leader_name}, and the members of the team them: {self.team_members}'
		
		
	def add_team_member(self, employee_name):
		self.team_members.append(employee_name)
		
	
	def remove_team_member(self, employee_name):
		self.team_members.remove(employee_name)
	
	
	def add_project(self, project, company):
		company.update_project({project: f"{self.team_leader_name}"})
		
	
	def update_project(self, project, company,  name = 'abc'):
		if name == 'abc':
			company.update_project({project: f"{self.team_leader_name}"})
		if name in self.team_members:
			if random.random() > 0.5:
				company.update_project({project: f"{name}"})
			else:
				print("The update request was rejected")
		else:
			Ceo.update_project(self, project, company, name)
	
	
	def remove_project(self, project, name, company):
		if name in self.team_members:
			if random.random() > 0.5:
				company.remove_project(project)
			else:
				print("The deletion request was rejected")
		else:
			Ceo.remove_project(self, project, company, name)
		
		
	
			

