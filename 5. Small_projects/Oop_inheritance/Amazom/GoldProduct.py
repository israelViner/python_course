from product import product 


class GoldProduct(product):


	def __init__(self, product_name, amount, bought_with = {}):
		product.__init__(self, product_name, bought_with)
		self.amount = amount
			
		
	def __repr__(self):
		return product.__repr__(self) + ", (" + str(self.amount) + "units left!)" 
		
	
	def update(self, product_names):
		product.update(self, product_names)
		self.amount -= 1
	
		
	def get_recommandations(self, k):
		 return [pro for pro in product.get_recommandations(self, k) if self.bought_with[pro] > 10]
		  
		

