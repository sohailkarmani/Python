# Python program example to show the use of while loop   
  
num = 15  
  
# initializing summation and a counter for iteration  
summation = 0  
c = 1  
  
while c <= num: # specifying the condition of the loop  
    # begining the code block  
    summation = c**2 + summation  
    c = c + 1    # incrementing the counter  
  
# print the final sum  
print("The sum of squares is", summation)  