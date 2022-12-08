from Company import Company 
from Ceo import Ceo
from Team_leader import Team_leader
from employee import employee


def main():
	obgect = Company()
	print(obgect)
	
	big_boss = Ceo('itsik')
	small_boss = Team_leader('oron')
	tiny_boss = Team_leader('aviv')
	employee_1 = employee("israel", small_boss)
	employee_2 = employee("moyshi", small_boss)
	employee_3 = employee("baruch", small_boss)
	employee_4 = employee("yair", tiny_boss)
	
	
	big_boss.add_project("endroid" ,obgect)
	small_boss.add_project("linux" ,obgect)
	print(obgect)
	
	employee_1.add_project("ios" ,obgect)
	employee_1.add_project("windows" ,obgect)
	employee_2.update_project("windows" ,obgect)
	print(obgect)
	
	employee_3.update_project("windows" ,obgect)
	print(obgect)
	
	employee_1.remove_project("ios" ,obgect)
	print(obgect)
	
	employee_4.add_project("iphone" ,obgect)
	print(obgect)
	
	employee_2.update_project("iphone" ,obgect)
	print(obgect)
	
	big_boss.remove_project("windows" ,obgect)
	print(obgect)
	
	
	
	
		
	
	
	
if __name__ == "__main__":
	main() 
