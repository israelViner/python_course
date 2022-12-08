from product import product 
from GoldProduct import GoldProduct 


class RecommandationSystem:

	def __init__(self, product_tuples):
		products = {}
		for pro in product_tuples:
			if pro[1] == -1:
				products[pro[0]] = product(pro[0])
			else:
				products[pro[0]] = GoldProduct(pro[0], pro[1])
		self.products = products		


	def update(self, purchased_product_names):
		for pro in purchased_product_names:
			self.products[pro].update([prod for prod in purchased_product_names if not prod == pro])
			
	
	def get_recommandations(self, product_name, k):
		return self.products[product_name].get_recommandations(k)

