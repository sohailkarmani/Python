import random  
numbers = [ ]  
for val in range(0, 11):  
    numbers.append( random.randint( 0, 11 ) )  
for num in range( 0, 11 ):  
    for i in numbers:  
        if num == i:  
            print( num, end = " " )  