



2. 
	A. from myModule import myfunc as f  
	B. 
	
3. summ = [a + b for a,b in even,odd ]	
	
4. Infinite time, because we are adding elements to the list in every iteration so the loop is never going to end.
	
	
5. 

	def getSum(n):  
		if n==0:  
			return 0  
 		else:  
			sum=n+getSum(n-1);  
		return sum  