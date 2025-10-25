def showOptions():
    print("\nOptions:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return -1

def main():
    print("Program starting.")
    count = 0

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")

        elif choice == 2:
            count += 1
            print("Count increased!")

        elif choice == 3:
            count = 0
            print("Cleared count!")

        elif choice == 0:
            print("Exiting program.")
            break

        elif choice == -1:
            continue  

        else:
            print("Unknown option!")

        print("Program ending.")

main()









    
    
    




    
