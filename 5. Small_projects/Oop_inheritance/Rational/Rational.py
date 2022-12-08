import math

class Rational:

	def __init__(self, numerator, denominator = 1):
		if denominator == 0:
			raise ValueError
		self.numerator = numerator
		self.denominator = denominator
		
	def __repr__(self):
		return f'{self.numerator}/{self.denominator}'
	
	
	def add(self, fraction):
		new_Rational =  Rational((fraction.numerator * self.denominator + self.numerator * fraction.denominator),  (fraction.denominator*self.denominator))
		return new_Rational
		
		
	def is_equal(self, fraction):
		return fraction == self.numerator/self.denominator
		
		
	def shrink(self):
		gcd = f'{int(self.numerator/math.gcd(self.numerator, self.denominator))}/{int(self.denominator/math.gcd(self.numerator, self.denominator))}'
		return gcd
