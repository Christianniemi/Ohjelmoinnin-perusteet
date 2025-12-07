import sys 

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.isdigit():              
                    PValues.append(int(line))
    except Exception:
        print("File not found")
        sys.exit        
    return None

def sumOfValues(PValues: list[int]) -> int:
    return sum(PValues)

    

def productOfValues(PValues: list[int]) -> int:
    for line in PValues:
        Product = line * line
    return Product

def main() -> None:
    SUM1 = "# --- Sum of numbers --- #"
    PRODUCT1 = "# --- Product of numbers --- #"
    # 1. Initialize
    Values: list[int] = []
    # 2. Operate
    print("Program starting.")
    # 2.1 Ask filname
    filename = input("Insert filename: ")
    # 2.2 read values
    readValues(filename, Values)
    Sum = sumOfValues(Values)
    print(SUM1)
    print(Sum)
    print(SUM1)
    Product = productOfValues(Values)
    print(PRODUCT1)
    print(Product)
    print(PRODUCT1)
    # 2.3 calculate sum of values
    # 2.4 calculate product of values
    # 2.5 display results
    # 3. Cleanup
    Values.clear()
    print("Program ending.")
    return None
if __name__ == "__main__":
    main()