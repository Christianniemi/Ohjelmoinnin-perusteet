print("Program starting. ")
print("\nTo get to the page follow the instructionds. ")

name = input("\nInsert your fullname: ")
age = int(input("Insert your age: "))
uname = input("Insert username: ")
admin = input("Are you admin yes/no: ")

if (uname == name and age >= 18 and admin == 'yes'):
    print("\nWelcome to the admin page ")
    print("\nOptinons: ")
    print("1 - Add new user ")
    print("2 - Check device functionality ")
    print("0 - Exit" )
    choice = int(input("Your choice: "))
    if (choice == 1):
        print("\nAdding new user.." )
    elif (choice == 2):
        print("Checking device functionality" )
    elif (choice == 0):
        print("\nExiting..." )
    else:
        print("Unknown option" )
elif (uname == name and age >= 18 and admin == "no"):
    print("\nWelcome to the page")
    print("Options: ")
    print("1 - Check your details" )
    print("0 - Exit " )
    choice = int(input("Your choice"))
    if (choice == 1):
        print(f"\nYour details are: \nName: {name} \nAge: {age} \nUsername: {uname} \nAdmin: {admin}")
    elif (choice == 0):
        print("\nExiting...")
    else:
        print("Unknown option")
elif (age < 18):
    print("Acces denied")
else:
    print("Error")

print("Program ending.")

