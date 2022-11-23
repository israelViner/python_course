import random
import matplotlib.pyplot as plt
import numpy as np


class RW:
	def __init__(self,n,N):
	     #The number of steps
		self.N = N+1
	     #The number of dimensions
		self.n = n
	     #the coordinate system
		self.rw = self.init_coordinates()

	
     #Initialize the coordinate system
	def init_coordinates(self): 
		rw = [0]*self.n
		for i in range(self.n):
			rw[i] = [0]*self.N
		return rw

	
     #The main function that performs the Random-walk
	def fill_coordinates(self):
		for i in range(self.N-1):
			dim = random.randint(0,self.n-1)
			for j in range(self.n):
				if j != dim:
					self.dont_move(j, i)
				else:
					self.choose_direction(j, i)
		return self.rw
	
	
     #The two functions of the steps	
	
	def dont_move(self,j,i):
		self.rw[j][i+1] = self.rw[j][i]
		return
	
	
	def choose_direction(self,j, i):
		dice = random.random()
		if dice > 0.5:
			self.rw[j][i+1] = self.rw[j][i]+1
		else:
			self.rw[j][i+1] = self.rw[j][i]-1
				

     #Displaying the steps according to the number of dimensions selected
	def display(self):
		if self.n == 1:
			plt.plot(list(range(self.N)),self.rw[0])
			plt.show()
		elif self.n == 2:
			plt.plot(self.rw[0],self.rw[1])
			plt.show()
		elif self.n == 3:
			m = plt.subplot(1,1,1,projection = "3d")
			m.plot(self.rw[0],self.rw[1],self.rw[2])
			plt.show()
		else:
			for i in range(self.N):
				print("step", str(i+1).zfill(3) ,"is:", end = " ")
				res = []
				for j in range(self.n):
					res.append(str(self.rw[j][i]).zfill(2))
				new_res = '[' + ', '.join(res) + ']'
				print(new_res)
		 

#The main call to perform the random-walk
def main():
	dim = int(input("Enter the number of the dimensions: "))
	id dim < 1:
		return
	steps =  int(input("Enter the number of the steps: "))
	random_walk = RW(dim, steps)
	random_walk.fill_coordinates()
	random_walk.display()
		
	

if __name__=="__main__":
	main()



	 
	 	 

	  
