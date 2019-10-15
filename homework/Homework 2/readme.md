# HOMEWORK 2 (SHASHANK KUMBHARE) #  

Problem 1:  
	
click [here](./problem1.py) for problem 1 code.  
	
Problem 2:  

consider, a = 5  
1. Objects are numbers/values. In this case '5' is an object.
(Different objects have different location/address/id).  
2.	Variables are pointers to the id of the objects. In this case 'a' is a pointer and 'a' is pointing towards id of object '5'.  
(Variables points towards the id of object).  
3. id(a) gives the id towards which the pointer 'a' of the object '5' is pointing.    
4. a = 5 : This creates a new pointer/variable with name 'a' which points towards the id of object '5'.  
5. b = a : This creates a new pointer/variable with name 'b' and is a copycat of pointer 'a' and will point towards id of '5'.  
6. print(a) prints the object towards which the pointer 'a' is pointing.  
	
A.  
```python
a = 5  
b = a  
print (id(a), id(b))
```

	Output:  
	140714951152576 140714951152576   
		
Explanation:  
'a' points towards id of '5'. 'b' is a copycat of 'a'. Hence, both id(a) and id(b) are giving the same address, since 'a' and 'b' are pointing towards the same object '5'.  
		  
```python		  
c = b  
b = 3  
print (a,b,c)  
print (id(a),id(b),id(c))  
```	
			  
	Output:  
	5 3 5  
	140714951152576 140714951152512 140714951152576  
		
Explanation:  
'a' is pointing towards id of '5'.  
c = b : 'c' is a copycat of 'b', so 'c' will point towards id of '5'.   
b = 3 : Now, b is pointing towards id of '3'.  
Hence the output.  
		  
```python		  
b = a  
b = 5  
print (id(a), id(b))  
```
				
	Output:  
	140714951152576 140714951152576  
		  
Explanation:  
'a' is pointing towards id of '5'.  
b = a : 'b' is a copycat of 'a', so 'b' is pointing towards '5'.  
b = 5 : 'b' is pointing towards '5'.  
Hence the output.  
		  
		  
B.  
		
Problem 3:  

	asdjhksajd
	asdsad
	sadsad
	asdsa
		
		
		
		
		
		
		
		
		