import random
random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int):
    """Randomly places mines (value 9) into the PMineField."""
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    placed = 0
    while placed < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1

def calculateNearbys(PMineField: list[list[int]]) -> None:
    """Calculates nearby mines for each non-mine cell."""
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if PMineField[nr][nc] == 9:
                            count += 1
            PMineField[r][c] = count

def generateMinefield(PMineField: list[list[int]], PRows: int, PCols: int, PMines: int) -> None:
    """Initializes minefield, lays mines, and calculates nearby counts."""
    PMineField.clear()
    for i in range(PRows):
        PMineField.append([0] * PCols)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)

def showBoard(PMineField: list[list[int]]) -> None:
    for row in PMineField:
        print(row)

def saveBoard(PMineField: list[list[int]], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for row in PMineField:
            line = ",".join(str(x) for x in row)
            f.write(line + "\n")

def main() -> None:
    print("Program starting.")
    minefield: list[list[int]] = []
    while True:
        print("Options:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            generateMinefield(minefield, rows, cols, mines)
        elif choice == "2":
            if minefield:
                showBoard(minefield)
            else:
                print("No board generated yet.")
        elif choice == "3":
            if minefield:
                fname = input("Insert filename: ")
                saveBoard(minefield, fname)
                print(f"Board saved to {fname}")
            else:
                print("No board generated yet.")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
    print("Program ending.")

if __name__ == "__main__":
    main()


