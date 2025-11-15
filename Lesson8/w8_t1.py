import time

def showOptions():
    pause_duration= 0
    while True:
    
        
        print("Options: ")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")
        choice = int(input("Your choice: "))
        if choice == 1:
            try:
                pause_duration = float(input("Insert pause duration (s): "))
                
                
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == 2:
            if pause_duration <= 0:
                print("Pause is not set.")
                print("Set pause first")

            else:
                print(f"Pausing for {pause_duration} seconds ")
                time.sleep(pause_duration)
        elif choice == 0:
            print("Exiting program.")
            break

        else:
            print("Unknown option. ")
        
def main():
    print("Program starting")
    showOptions()
    print("Program ending. ")
    

if __name__ == "__main__":
    main()