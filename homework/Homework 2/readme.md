## HOMEWORK 2 (SHASHANK KUMBHARE) #  

### <p align="center">```Problem 1: Python script call from the Bash command line```</p>  
```python		  
#!/usr/bin/env python
print("""This is Python version 3.5.2\n 
Python is the best language for String manipulation!\n
!noitalupinam gnirtS rof egaugnal tseb eht si nohtyP\n
!otlpnmgit o gunlte h inhy\n
pYTHON IS THE BEST LANGUAGE FOR sTRING MANIPULATION!\n\n
The sentence 'Python is the best language for String manipulation!' contains
4 'a' letters, and
0 'A' letters!\n
Python
is
the
best
language
for
String
manipulation!\n
PYTHON
IS
THE
BEST
LANGUAGE
FOR
STRING
MANIPULATION!""")  
```	
click [here](./problem1.py) for the above problem1.py file.  
	
	
### <p align="center">```Problem 2: Python aliasing vs. copying variables```</p>  


consider, a = 5  
1.	Objects are numbers/values. In this case, '5' is an object.  
	Different objects have different location/address/id)
2.	Variables are pointers to the id of the objects. In this case, 'a' is a pointer and 'a' is pointing towards id of object '5'.  
	Variables points towards the id of object.  
3.	id(a) gives the id towards which the pointer 'a' is pointing. In this case, id(a) will give id of object '5', because 'a' is pointing towards id of '5'.     
4.	a = 5 : This creates a new pointer/variable with name 'a' which points towards the id of object '5'.   
5. 	b = a : This creates a new pointer/variable with name 'b' and is a copycat of pointer 'a' and will point towards id of '5'.  
6. 	print(a): prints the object towards which the pointer 'a' is pointing.  
	
### <p align="center">```2.A```</p>  

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
  
### <p align="center">```2.B```</p>    

```python		  
a = [5]
b = a
print (id(a), id(b))  
```
```				
2437144181896 2437144181896  
```  
Explanation:  
a = [5] : This creates a new pointer 'a' which points towards id of list-object '[ ]'. And the list-object '[ ]' contains an int-object '5'.   
b = a : This creates a new pointer 'b' which is a copycat of 'a', so 'b' is pointing towards id of '[ ]'.    
Hence the output.  

```python		  
b.append(1)
print (a,b)
print (id(a),id(b)) 
```
```				
[5, 1] [5, 1]
2437144181896 2437144181896  
```  
Explanation:  
'a' and 'b' are pointing towards id of object '[ ]' containing an element '5'.  
b.append(1) : This adds an element '1' in the list-object '[ ]' containing an element '5' towards which 'b' is pointing at the end. This does not change the list-object '[ ]' rather change the no. of elements it posses.  
Note: List and its elements have different ids.   
Hence the output.  

### <p align="center">```2.C```</p>    

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
b = list(a) : This creates a new pointer 'b' which points towards a list-object '[ ]' contaning the elements of list-object '[ ]' towards which 'a' is pointing.    
Notice that 'a' and list(a) are not the same object, since list(a) creates a new list-object.    
Hence the output.  
  
```python		  
b = a[:]
print (a,b)
print (id(a), id(b))  
```
```				
[5] [5]
2437144973768 2437145017416
```  
Explanation:  
a[:] : This creates an iterable-object of the type towards which 'a' is pointing. In this case, the new iterable-object created would be a list-object since 'a' is pointing towards a list-object [ ].    
b = a[:] : This also creates a new pointer 'b' which points towards a list-object '[ ]' contaning all the elements of a list '[ ]' towards which 'a' is pointing.    
Notice that 'a' and a[:] are not the same object, since list(a) creates a new list-object.    
Hence the output.  

### <p align="center">```2.D```</p>    

```python		  
a = (5,)
b = tuple(a)
print (id(a), id(b)) 
```
```				
2437143136632 2437143136632
```  
Explanation:  
a = (5,) : This creates a new pointer 'a' which points towards id of tuple-object '( )' containing an element '5'.  
tuple(a) : This creates a new tuple-object '( )' containg the elements of iterable-object towards which 'a' is pointing.  
b = tuple(a) : This creates a new pointer 'b' which points towards a tuple-object '( )' contaning the elements of tuple-object towards which 'a' is pointing.    
Notice that 'a' and tuple(a) are the same object, since tuple(a) does not creates a new tuple-object.    
Hence the output.  

```python		  
b = a[:]
print (id(a), id(b))
```
```				
2437143136632 2437143136632
```  
Explanation:  
a[:] : This creates an iterable-object of the type towards which 'a' is pointing. In this case, the new iterable-object created would be a tuple-object since 'a' is pointing towards a tuple-object ( ).    
b = a[:] : This also creates a new pointer 'b' which points towards a tuple-object '[ ]' contaning all the elements of a tuple '[ ]' towards which 'a' is pointing.    
Notice that 'a' and a[:] are the same object, since tuple(a) creates a new tuple-object.  
Hence the output.  


### <p align="center">```Problem 3: Implementing the Bell-shaped (Gaussian) function```</p>  
```python
#!/usr/bin/env python

from math import pi, exp, sqrt

mu=0
sigma=2
x=1

y=1/sqrt(2*pi)/sigma*exp(-1/2*((x-mu)/sigma)**2)
print(y)
```
click [here](./problem3.py) for the above problem3.py file.  


### <p align="center">```Problem 4: Branching, the Pythonic way```</p>  

### <p align="center">```4.A```</p>
```python
#!/usr/bin/env python

abbr = input ("What is the three-letter abbreviation of this course? ")

answer_status = 'correct' if abbr == 'DSP' else 'wrong'

if answer_status=='correct':
    print('You answer is correct!')
else:
    print("wrong buddy...try again") 
```
click [here](./problem4A.py) for the above problem4A.py file.  

### <p align="center">```4.B```</p>
```python
 
```

### <p align="center">```4.C```</p>  
```python
#!/usr/bin/env python

abbr = input ("What is the three-letter abbreviation of this course? ")

answer_status = 'wrong'

if abbr == 'DSP':
	answer_status = 'correct'

print('You answer is correct!' if answer_status=='correct' else "wrong buddy...try again")
```
click [here](./problem4A.py) for the above problem4C.py file.  


### <p align="center">```Problem 5: Branching, the Pythonic way```</p>  
```python
#!/usr/bin/env python

def fib():
        
    def getFib(n_int):
        if n_int==0 or n_int==1:
            F=n_int
        else:
            F=getFib(n_int-1)+getFib(n_int-2)
        return F
    
    n=input("Please enter a non-negative integer or type stop: ")
 
    if n=='stop':
        return
    elif n.isdigit():
        n_int=int(n)
        print('fib(',n_int,') =',getFib(n_int))
        fib()
    else:
        print("The input argument is not a non-negative integer!")
        fib()
        
    return None
```
click [here](./problem5.py) for the above problem5.py file.  


### <p align="center">```Problem 6: Computing the Fibonacci sequence via for-loop```</p>  

### <p align="center">```6.A```</p>
```python
#!/usr/bin/env python

import time

def fib():
        
    def getFib(n_int):
        if n_int==0 or n_int==1:
            F=n_int
        else:
            F=getFib(n_int-1)+getFib(n_int-2)
        return F
    
    n=input("Please enter a non-negative integer or type stop: ")
 
    if n=='stop':
        return
    elif n.isdigit():
        n_int=int(n)
        print("fib(",n_int,") =",getFib(n_int),"\naverage runtime: ",time.process_time(),"seconds")
        fib()
    else:
        print("The input argument is not a non-negative integer!")
        fib()
        
    return None
```
click [here](./problem6A.py) for the above problem6A.py file.  

### <p align="center">```6.B```</p>
```python
#!/usr/bin/env python

import time

def fibLoop():
        
    def getFib(n_int):
        if n_int==0 or n_int==1:
            F=n_int
        else:
            F_old=0
            F_curr=1
            for i in range(1,n_int):
                F=F_old+F_curr
                F_old=F_curr
                F_curr=F       
        
        return F
    
    n=input("Please enter a non-negative integer or type stop: ")
 
    if n=='stop':
        return
    elif n.isdigit():
        n_int=int(n)
        print("fib(",n_int,") =",getFib(n_int),"\naverage runtime: ",time.process_time(),"seconds")
        fibLoop()
    else:
        print("The input argument is not a non-negative integer!")
        fibLoop()
        
    return None
```
click [here](./problem6B.py) for the above problem6B.py file.  

### <p align="center">```6.C```</p>
  
When we time fib( ) and fibLoop( ) for the same input integers 10, 15, 20, 25, 30 and 35, we found that fibLoop( ) is more efficient than fib( ). The reason is that fib() is calling getFib( ) multiple times so it takes more computation time.


### <p align="center">```Problem 7: Checking if an input is a prime number (via recursive function calls)```</p>  

```python
#!/usr/bin/env python

def isPrime(n):
    
    def modulus(n,x):
        if (n%x)==0:
            return False       
        else:
            if x<(n/2):
                return modulus(n,x+1)
            else:
                return True
    
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        return modulus(n,2)
```
click [here](./problem7.py) for the above problem7.py file.


### <p align="center">```Problem 9: Computing the area of a triangle```</p>  

```python
#!/usr/bin/env python

def  getTriangleArea(a):

    area=1/2*abs(a[1][0]*a[2][1]-a[2][0]*a[1][1]-a[0][0]*a[2][1]+a[2][0]*a[0][1]+a[0][0]*a[1][1]-a[1][0]*a[0][1])
        
    return area
```
click [here](./problem9.py) for the above problem9.py file.

### <p align="center">```Problem 10: The while-loop implementation of for-loop```</p>  

```python
#!/usr/bin/env python

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
print ('    C     F')
i=0
while i<len(Cdegrees):
    F = (9.0/5)*Cdegrees[i] + 32
    print("%5d %5.1f"  % (Cdegrees[i],F))
    i+=1
```
click [here](./problem10.py) for the above problem10.py file.

### <p align="center">```Problem 11: Command line input arguments summation via sum( )```</p>  

```python
#!/usr/bin/env python

import sys

print("The sum of {} is {}".format( " ".join(sys.argv[1:]), sum(float(e) for e in sys.argv[1:])))
```
click [here](./problem11.py) for the above problem11.py file.

### <p align="center">```Problem 12: Command line input arguments summation via eval( )```</p>  

```python
#!/usr/bin/env python

import sys

print("The sum of {} is {}".format( " ".join(sys.argv[1:]) , eval("+".join(sys.argv[1:]) ) ) )
```
click [here](./problem12.py) for the above problem12.py file.

### <p align="center">```Problem 13: Impact of machine precision on numerical computation```</p>  

```python
eps = 1.0
while 1.0 != 1.0 + eps:
    print ('...............', eps)
    eps /= 5.0
print ('final eps:', eps)
```
```
............... 1.0
............... 0.2
............... 0.04
............... 0.008
............... 0.0016
............... 0.00032
............... 6.400000000000001e-05
............... 1.2800000000000003e-05
............... 2.5600000000000005e-06
............... 5.120000000000001e-07
............... 1.0240000000000003e-07
............... 2.0480000000000005e-08
............... 4.096000000000001e-09
............... 8.192000000000001e-10
............... 1.6384000000000003e-10
............... 3.2768e-11
............... 6.553600000000001e-12
............... 1.31072e-12
............... 2.62144e-13
............... 5.2428800000000005e-14
............... 1.0485760000000001e-14
............... 2.0971520000000002e-15
............... 4.194304e-16
final eps: 8.388608000000001e-17
```
"1.0 != 1.0 + eps" will be False when "eps" becomes less than "Machine epsilon".  
Machine epsilon is the maximum relative error of the floating point arithmetic. Mathematically, for each floating point type, it is equivalent to the difference between 1.0 and the smallest representable value that is greater than 1.0.
```python
import numpy as np
print(np.finfo(float).eps)
```
```
2.220446049250313e-16
```
You can see the final eps: 8.388608000000001e-17 is less than 2.220446049250313e-16 (Machine epsilon). 

### <p align="center">```Problem 14: Integer overflow```</p>  

```python
import numpy as np
np.iinfo(np.int16)
```
```
iinfo(min=-32768, max=32767, dtype=int16)
```

```python
import numpy as np
np.iinfo(np.int32)
```
```
iinfo(min=-2147483648, max=2147483647, dtype=int32)
```

If we type cast a integer larger than the max int8 no. (127), then the higher integers will start from the smallest int8 no. (-128).    
```python
import numpy as np
#The max limit for int8 is 127
L=[127,128,129,130,200]
print(np.int8(L))
```
```
[ 127 -128 -127 -126  -56]
```

If we type cast a integer smaller than the min int8 no. (-128), then the smaller integers will start from the largest int8 no. (127).    
```python
import numpy as np
#The min limit for int8 is -128
L=[-128,-129,-130,-131,-201]
print(np.int8(L))
```
```
[-128  127  126  125   55]
```

### <p align="center">```Problem 15: ```</p>  

```python
numbers = list(range(10))
print(numbers)
```
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
for n in numbers:
    i = len(numbers)//2
    del numbers[i]
    print ('n={}, del {}'.format(n,i), numbers)
```
```
n=0, del 5 [0, 1, 2, 3, 4, 6, 7, 8, 9]
n=1, del 4 [0, 1, 2, 3, 6, 7, 8, 9]
n=2, del 4 [0, 1, 2, 3, 7, 8, 9]
n=3, del 3 [0, 1, 2, 7, 8, 9]
n=8, del 3 [0, 1, 2, 8, 9]
```
We see the strange behaviour because everytime ```del number[i]``` is executed, the i<sup>th</sup> element of list "numbers" is removed and length of the list and the index no.s of list elemests are changing correspondingly.  





