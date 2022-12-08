from Rational import Rational


def main():
	fraction = Rational(2, 3)
	fraction2 = Rational(3,4)
	
	fraction3 = Rational(7, 11)
	
	fraction5 = Rational(264, 450)
	
	print(fraction.is_equal(fraction2))
	
	
	
	print(fraction3.add(fraction5).shrink())
	
	print(fraction3.numerator, fraction3.denominator)
	
	print("The shrink is: ", fraction5.shrink())
	
	


	
	
if __name__ == "__main__":
	main() 
