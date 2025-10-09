print("Program starting.\n" )
print("Check multiplicative persistence." )

num = int(input("Insert an integer: " ))
steps = 0
while num > 9:
    i = 1
    for digit in str(num):
        i *= int(digit)
    print(f"{' * '.join(str(num))} = {i}" )
    num = i
    steps += 1

print("No more steps.\n" )

print(f"This program took {steps} step(s)" )

print("\nProgram ending." )


    


    





  
    
       









    




    
