from timeLib import readTimestamps, calculateYears, calculateMonths, calculateWeekdays

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = []
    readTimestamps(filename, timestamps)

    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "1":
            year = int(input("Insert year: "))
            count = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {count}")

        elif choice == "2":
            month = input("Insert month: ")
            count = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {count}")

        elif choice == "3":
            weekday = input("Insert weekday: ")
            count = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")

        print()

    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

if __name__ == "__main__":
    main()
