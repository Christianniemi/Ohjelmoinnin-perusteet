def main():
    print("Program starting.")
    print("Collect positive integers.")

    numbers: list[int] = []

    while True:
        try:
            value = int(input("Insert positive integer(negative stops): "))
            if value < 0:
                break
            numbers.append(value)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("Stopped collecting positive integers.")

    if not numbers:
        print("No integers to display.")
    else:
        print(f"Displaying {len(numbers)} integers:")
        for index, number in enumerate(numbers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {number}")

    print("Program ending.")

if __name__ == "__main__":
    main()
