import svgwrite
import drawLib2

def main() -> None:
    print("Program starting.")
    Dwg = svgwrite.Drawing()

    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "1":
            drawLib2.drawSquare(Dwg)
        elif choice == "2":
            drawLib2.drawCircle(Dwg)
        elif choice == "3":
            drawLib2.drawHexagon(Dwg)
        elif choice == "4":
            drawLib2.saveSvg(Dwg)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

        print()

    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

if __name__ == "__main__":
    main()
