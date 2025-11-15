from datetime import datetime

# Kuukaudet ja viikonpäivät vakioina
MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    with open(PFilename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    ts = datetime.strptime(line, "%Y-%m-%dT%H:%M")
                except ValueError:
                    # Jos joskus rivissä on välilyönti T:n sijaan
                    ts = datetime.strptime(line, "%Y-%m-%d %H:%M")
                PTimestamps.append(ts)


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    """Laske kuinka monta timestampia annetulle vuodelle."""
    return sum(1 for ts in PTimestamps if ts.year == PYear)

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    """Laske kuinka monta timestampia annetulle kuukaudelle (nimenä)."""
    if PMonth not in MONTHS:
        return 0
    month_index = MONTHS.index(PMonth) + 1
    return sum(1 for ts in PTimestamps if ts.month == month_index)

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    """Laske kuinka monta timestampia annetulle viikonpäivälle (nimenä)."""
    if PWeekday not in WEEKDAYS:
        return 0
    weekday_index = WEEKDAYS.index(PWeekday)
    return sum(1 for ts in PTimestamps if ts.weekday() == weekday_index)
