print("Program starting.\n")

start = int(input("Insert starting point: " ))
stop =int(input("Insert stopping point: " ))
inspection = int(input("Insert inspection point: " ))

if start >= stop:
    if inspection < start or inspection >= stop:
        print("\nStarting point value must be less than the stopping point value.\nInspection value must be within the range of start and stop.")
    else:
        print("Starting point value must be less than the stopping point value.")
    
elif inspection < start or inspection > stop:
    print("\n\nInspection value must be within the range of start and stop.")

else:
    i = 0
    print("\nFirst loop - inspection with break: ")
    for i in range (start, stop):
        if (i == inspection):
            break
        print(i, end=" ")
    print("\nSecont loop - inspection with continue: ")
    for i in range (start, stop):
        if (i == inspection):
            continue        
        print(i, end=" ")

print("\n\nProgram ending. ")
    
        
    
