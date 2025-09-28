print("Program startin")
print("Insert two integers")
int1 = int(input("Insert first interger: "))
int2 = int(input("Insert second integer: "))
print("Comparing inserted integers. ")
if (int1 > int2):
    print("First interger is greater")
elif(int2 > int1):
    print("Second interger is greater")
else:
    print("Integers are the same")
print("")
Sum = int1 + int2
print(f"{int1} + {int2} = {Sum}")
Remainder = Sum % 2
if (Remainder == 0):
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending")
