## HOMEWORK 2 (SHASHANK KUMBHARE) #  

## <p align="center">```Problem 1: ```</p>  
	
click [here](./problem1.py) for problem 1 code.  
	
## <p align="center">```Problem 2: ```</p>  


consider, a = 5  
1.	Objects are numbers/values. In this case '5' is an object.  
	Different objects have different location/address/id)
2.	Variables are pointers to the id of the objects. In this case 'a' is a pointer and 'a' is pointing towards id of object '5'.  
	Variables points towards the id of object.  
3.	id(a) gives the id towards which the pointer 'a' is pointing. In this case, id(a) will give id of object '5', because 'a' is pointing towards id of '5'.     
4.	a = 5 : This creates a new pointer/variable with name 'a' which points towards the id of object '5'.   
5. 	b = a : This creates a new pointer/variable with name 'b' and is a copycat of pointer 'a' and will point towards id of '5'.  
6. 	print(a): prints the object towards which the pointer 'a' is pointing.  
	
### ```A.```  

```python
a = 5  		
b = a  
print (id(a), id(b))
```
```  
140714951152576 140714951152576   
```		
Explanation:  
a = 5 : This creates a new pointer 'a' which points towards id of '5'.    
b = a : This creates a new pointer 'b' which is a copycat of 'a' and points towards id of '5'.  
Hence, both id(a) and id(b) are giving the same address, since 'a' and 'b' are pointing towards the same object '5'.  	  
   
```python		  
c = b  
b = 3  
print (a,b,c)  
print (id(a),id(b),id(c))  
```	
```			   
5 3 5  
140714951152576 140714951152512 140714951152576  
```	
Explanation:  
Both 'a' and 'b' are pointing towards id of '5'.  
c = b : This creates a new pointer 'c' which is a copycat of 'b', so 'c' will also point towards id of '5'.   
b = 3 : This creates a new pointer 'b' which points towards id of '3' and now this will have no effect on 'a' or 'c'.  
Hence the output.  
  
```python		  
b = a  
b = 5  
print (id(a), id(b))  
```
```				  
140714951152576 140714951152576  
```		  
Explanation:  

'a' is pointing towards id of '5'.  
b = a : This creates a new pointer 'b' which is a copycat of 'a', so 'b' is pointing towards id of '5'.  
b = 5 : This creates a new pointer 'b' which points towards id of '5'.  
Hence the output.  
  
### ```B.```    

```python		  
a = [5]
b = a
print (id(a), id(b))  
```
```				
2437144781192 2437144781192 
```  
Explanation:  
a = [5] : This creates a new pointer 'a' which points towards id of list-object '[ ]'.    
And the list-object '[ ]' contains an int-object '5'.   
b = a : This creates a new pointer 'b' which is a copycat of 'a', so 'b' is pointing towards id of '[ ]'.    
Hence the output.  

```python		  
b.append(1)
print (a,b)
print (id(a),id(b)) 
```
```				
[5, 1] [5, 1]
2437144182088 2437144182088  
```  
Explanation:  
'a' and 'b' are pointing towards id of object '[ ]' containing an element '5'.  
b.append(1) : This adds an element '1' in the list-object '[ ]' containing an element '5' towards which 'b' is pointing at the end. This does not change the list-object '[ ]' rather change the no. of elements it posses.  
Note: List and its elements have different ids.   
Hence the output.  

### ```C.```    

```python		  
a = [5]
b = list(a)
print (a,b)
print (id(a), id(b))  
```
```				
[5] [5]
2437145015176 2437145035272
```  
Explanation:  
a = [5] : This creates a new pointer 'a' which points towards id of list-object '[ ]' containing an element '5'.  
list(a) : This creates a new list-object '[ ]' containg the elements of iterable-object towards which 'a' is pointing.  
b = list(a) : This creates a new pointer 'b' which points towards a list-object '[ ]' contaning the elements of iterable-object towards which 'a' is pointing.    
Notice that 'a' and list(a) are not the same object, since list(a) creates a new list-object.    
Hence the output.  
  
```python		  
b = a[:]
print (a,b)
print (id(a), id(b))  
```
```				
[5] [5]
2437145015176 2437144226824
```  
Explanation:  
b = a[:] : This also creates a new pointer 'b' which points towards a list-object '[ ]' contaning all the elements of a list '[ ]' towards which 'a' is pointing.    

### ```D.```    

```python		  
a = (5,)
b = tuple(a)
print (id(a), id(b)) 
```
```				
2437144241376 2437144241376
```  
Explanation:  
a = [5] : This creates a new pointer 'a' which points towards id of list-object '[ ]' containing an element '5'.  
list(a) : This creates a new list-object '[ ]' containg the elements of iterable-object towards which 'a' is pointing.  
b = list(a) : This creates a new pointer 'b' which points towards a list-object '[ ]' contaning the elements of iterable-object towards which 'a' is pointing.    
Notice that 'a' and list(a) are not the same object, since list(a) creates a new list-object.    
Hence the output.  

```python		  
b = a[:]
print (id(a), id(b))
```
```				
2437144241376 2437144241376
```  
Explanation:  
a = [5] : This creates a new pointer 'a' which points towards id of list-object '[ ]' containing an element '5'.  
list(a) : This creates a new list-object '[ ]' containg the elements of iterable-object towards which 'a' is pointing.  
b = list(a) : This creates a new pointer 'b' which points towards a list-object '[ ]' contaning the elements of iterable-object towards which 'a' is pointing.    
Notice that 'a' and list(a) are not the same object, since list(a) creates a new list-object.    
Hence the output. 

## <p align="center">```Problem 3: ```</p>  








