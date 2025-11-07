def main():
    print("Program starting.")
    user_input = input("Insert comma separated integers: ")

    values = user_input.split(",")
    valid_integers: list[int] = []

    for value in values:
        value = value.strip()
        try:
            number = int(value)
            valid_integers.append(number)
        except ValueError:
            print(f"Invalid value '{value}' detected.")

    if not valid_integers:
        print("No valid integers to analyze.")
    else:
        total = sum(valid_integers)
        parity = "even" if total % 2 == 0 else "odd"
        print(f"There are {len(valid_integers)} integers in the list.")
        print(f"Sum of the integers is {total} and it's {parity}")

    print("Program ending.")

if __name__ == "__main__":
    main()
