print("Program starting.")
print("Testing decision structures. ")
integer = int(input("Insert an integer: "))

print("Options: ")
print("1 - In one multi branched decision ")
print("2 - In multiple independent if statements ")
print("0 - Exit ")

Choice = int(input("Your choice: "))
if (Choice == 1):
    if integer > 399:
        Result = integer + 44
        print(f"Using one multi branched decision structure. ")
        print(f"Result is {Result}")
    elif integer > 199:
        Result = integer + 22
        print(f"Using one multi branched decision structure. ")
        print(f"Result is {Result}")
    elif integer > 99:
        Result = integer + 11
        print(f"Using one multi branched decision structure. ")
        print(f"Result is {Result}")
elif (Choice == 2):
    if integer > 399:
        Result = integer + (44 * 1.75)
        print(f"Using multiple independent if statements stucture. ")
        print(f"Result is {Result}")
    elif integer > 199:
        Result = integer + (22 * 1.5)
        print(f"Using multiple independent if statements stucture. ")
        print(f"Result is {Result}")
    elif integer > 99:
        Result = integer + (11 * 1.25)
        print(f"Using multiple independent if statements stucture. ")
        print(f"Result is {Result}")
elif (Choice == 0):
    print("Exiting...")
else:
    print("Unknown option ")

print("\nProgram ending. ")




