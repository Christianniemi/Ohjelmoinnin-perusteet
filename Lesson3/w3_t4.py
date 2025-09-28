print("Program starting")
print("This is a program with simple menu, where you can choose which operation the program performs.")
Name = input("Before the menu, please insert your name: ")
print("\nOptions:")
print("1 - Print welcome message")
print("2 - Print the name backwards ")
print("3 - Print the first character ")
print("4 - Show the amount of characters in the name ")
print("0 - Exit ")

Choice = int(input("Your choice: "))
if (Choice == 1):
    print(f"Welcome {Name} !")
elif (Choice == 2):
    print(f"Your name backwards is \"{Name[::-1]}\"")
elif (Choice == 3):
    print(f"The first character in the name \"{Name}\" is \"{Name[-4]}\"")
elif (Choice == 4):
    print(f"There are {len(Name)} characters in the name \"{Name}\"")
elif(Choice == 0):
    print("Exiting...")
else:
    print("Unknown option ")

print("\nProgram ending. ")

