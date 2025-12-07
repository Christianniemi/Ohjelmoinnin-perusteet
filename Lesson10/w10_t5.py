def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")
    try:
        n = int(input("Insert factorial: "))
    except ValueError:
        print("Invalid input, must be integer.")
        return

    print(f"Factorial {n}!")
    
    factors = [str(i) for i in range(1, n + 1)]
    expression = "*".join(factors)
    result = recursiveFactorial(n)
    print(f"{expression} = {result}")
    print("Program ending.")

if __name__ == "__main__":
    main()
