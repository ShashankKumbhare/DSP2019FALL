# HOMEWORK 2 (SHASHANK KUMBHARE) #  

Problem 1:  
click [here](./problem1.py) for problem 1 code.  

Problem 2:  

	A.  a = 5  
		b = a  
		print (id(a), id(b))  
		
		Output: 140714951152576 140714951152576  
		
		Explanation: 
		1. Objects are numbers/values (and different objects have different location/address).   
		2. Variables are pointers to the location/address of objects. (Variables points to the location/address).  
		3. id() gives the address/location of the object.  
		4. a = 5 : This creates a new variable/pointer which points towards the address/location of object 5.  
		5. b = a : This creates a new pointer/variable and is a copycat of pointer a.  
		6. Hence, both id(a) and id(b) are giving the same address, since both a and b points towards the same object.  
		
	B. 
		
		