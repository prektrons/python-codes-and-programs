def triangle(n): 
      
    # number of spaces 
    k = 2*n + 2
  
  
    for i in range(0, n): 
      
        for j in range(0, k): 
            print(end=" ") 
      
        
        k = k + 1
      
       
        for j in range(0, i+1): 
          
            # printing stars 
            print("1 ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
triangle(n) 
