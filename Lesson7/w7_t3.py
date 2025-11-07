WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')
    PRows.clear()
    try:
        with open(PFilename, encoding="utf-8") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    continue  
                row = line.strip()
                if row:
                    PRows.append(row)
    except FileNotFoundError:
        print(f'File "{PFilename}" not found.')

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    WeekdayTimestampAmount = [0] * len(WEEKDAYS)
    for row in PRows:
        for i, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                WeekdayTimestampAmount[i] += 1
                break
    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {WeekdayTimestampAmount[i]} stamps")
    WeekdayTimestampAmount.clear()

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for line in PResults:
        print(line)
    print("### Timestamp analysis ###")

def main() -> None:
    print("Program starting.")
    rows: list[str] = []
    results: list[str] = []
    filename = input("Insert filename: ")
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    rows.clear()
    results.clear()
    print("Program ending.")
if __name__ == "__main__":
    main()
