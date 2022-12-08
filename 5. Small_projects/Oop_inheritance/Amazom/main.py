from product import product 
from GoldProduct import GoldProduct 
from RecommandationSystem import RecommandationSystem


def main():
	obgect = RecommandationSystem([('aa', 15),('ba', 13),('ca', 2),('da', -1),('ea', -1),('sa', -1)])
	print(obgect.products)

	obgect.update(["aa", "ba", 'sa'])
	obgect.update(["aa", "ba", "sa"])
	obgect.update(["aa", "ba", "sa"])
	obgect.update(["aa", "ba", "sa"])
	obgect.update(["aa", "ba", "sa"])
	obgect.update(["aa", "ba", "sa"])
	obgect.update(["aa", "ba", "sa"])
	obgect.update(["aa", "ba", "sa"])
	obgect.update(["aa", "ba", "sa"])
	obgect.update(["aa", "ba", "sa"])
	obgect.update(["aa", "ba", "sa"])
	
	print(obgect.products)
	
	s = obgect.get_recommandations('aa',2)
	print(s)
		
	
	
	
if __name__ == "__main__":
	main() 
