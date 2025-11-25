def showOptions() -> None:
    print("Options: ")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

    # TODO: Print the menu options
    return None

def askChoice() -> int:
    try:
        num = int(input("Your choice: "))
        return num
    except ValueError:
        return None
        
    # TODO: Ask user for a menu choice and return it as an integer
    # Students should use try-except to handle invalid input
    

def saveLines(PLines: list[str]) -> None:
    try:
        filename = input("Filename to save: ")
        with open(filename, "w", encoding="UTF-8") as f:
            f.writelines(PLines)   # käytä writelines suoraan
        print(f"Saved {len(PLines)} lines to '{filename}'.")
    except OSError as e:
        print(f"File error: {e}")



    # TODO: Ask for filename and save lines to the file
    # Students should use try-except to handle file errors
    return None

def insertLine(PLines: list[str]) -> None:
    try:
        text = input("Insert text: ")
        PLines.append(text + "\n")
        print("Line added.")
    except Exception as e:
        print(f"Error inserting line: {e}")



    # TODO: Ask user to input a line and add it to PLines
    return None
def onInterrupt(PLines: list[str]) -> None:
    if not PLines:
        print("^CClosing suddenly.")
    else:
        print("Keyboard interrupt and unsaved progress!")
        choice = input("Save before quit(y/n)?: ").strip().lower()
        if choice == "y":
            saveLines(PLines)
    

    # TODO: Handle KeyboardInterrupt when there are unsaved lines
    # Students should use try-except to handle input errors
    return None

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    # Wrap the main loop in a try-except block to catch KeyboardInterrupt
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        onInterrupt(Lines)
    
    finally:
        Lines.clear()
        print("Program ending.")

if __name__ == "__main__":
    main()