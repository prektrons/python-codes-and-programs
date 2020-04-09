def triangle(n): 
      
    
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        
        for j in range(0, k): 
            print(end=" ") 
      
        
        k = k - 1
      
        
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
triangle(n) 
