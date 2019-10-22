



2. 
	A. from myModule import myfunc as f  
	B. 
	
3. 
	even = [0,2,4,6,8]   
	odd = [1,3,5,7,9]   
	summ = [even[i] + odd[i] for i in range(len(even))]   
		
4. Infinite time, because we are adding elements to the list in every iteration so the loop is never going to end.
		
5. 
	def getSum(n):  
		if n==0:  
			return 0  
 		else:  
			sum=n+getSum(n-1);  
		return sum  