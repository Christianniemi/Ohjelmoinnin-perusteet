import csv
from dataclasses import dataclass

# Viikonpäivät oikeassa muodossa
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday"]

@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

    def total(self) -> float:
        return self.consumption * self.price

def readTimestamps(filename: str) -> list[TIMESTAMP]:
    timestamps: list[TIMESTAMP] = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)  # ✅ Ohitetaan otsikkorivi
            for row in reader:
                try:
                    weekday = row[0].strip()
                    hour = row[1].strip()
                    consumption = float(row[2])
                    price = float(row[3])
                    ts = TIMESTAMP(weekday, hour, consumption, price)
                    timestamps.append(ts)
                except Exception as e:
                    print(f"Skipping row due to error: {e}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return timestamps

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')

    print("Analysing timestamps.")  # ✅ Testi vaatii tämän rivin
    timestamps = readTimestamps(filename)

    analysis_helper = [{"day": day, "usage": 0.0, "cost": 0.0} for day in WEEKDAYS]

    print("Analysing weekdays.")
    for ts in timestamps:
        for entry in analysis_helper:
            if entry["day"] == ts.weekday:
                entry["usage"] += ts.consumption
                entry["cost"] += ts.total()
                break

    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for entry in analysis_helper:
        usage = f"{entry['usage']:.2f}"
        cost = f"{entry['cost']:.2f}"
        print(f" - {entry['day']} usage {usage} kWh, cost {cost} €")
    print("### Electricity consumption summary ###")
    print(f"Collected {len(timestamps)} timestamps.")
    print("Program ending.")

if __name__ == "__main__":
    main()