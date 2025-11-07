from dataclasses import dataclass

DELIMITER = ";"  

@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

    def total(self) -> float:
        return self.consumption * self.price

def readTimestamps(filename, timestamps):
    try:
        with open(filename, encoding='utf-8') as file:
            for line in file:
                row = line.strip()
                if not row:
                    continue
                columns = row.split(DELIMITER)
                if columns[0] == "Weekday":
                    continue

                ts = TIMESTAMP(
                    weekday=columns[0],
                    hour=columns[1],
                    consumption=float(columns[2]),
                    price=float(columns[3])
                )
                timestamps.append(ts)
                columns.clear()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


    return timestamps

def displayTimestamps(timestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for ts in timestamps:
        total = ts.total()
        print(f" - {ts.weekday} {ts.hour}:00, price {ts.price:.2f} €, consumption {ts.consumption:.2f} kWh, total {total:.2f} €")

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')

    print("Analysing timestamps.")
    timestamps = readTimestamps(filename)

    displayTimestamps(timestamps)

    print(f"Collected {len(timestamps)} timestamps.")
    print("Program ending.")


if __name__ == "__main__":
    main()
