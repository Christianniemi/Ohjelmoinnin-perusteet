SEPARATOR = ";"
def readValues(filename): 
    print("#### Number analysis - START ####")
    print(f"File \"{filename}\" results: ")
    values = []
    file = open(filename, "r")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        values.append(line)
    file.close()
    return values

def analyseValues(result):
    numbers = [int(line.strip()) for line in result]
    Total = len(numbers)
    Count = sum(numbers)
    Greatest = max(numbers)
    Average = Count / Total
    Result = f"Count{SEPARATOR}Sum{SEPARATOR}Greatest{SEPARATOR}Average\n"
    Result += f"{Total}{SEPARATOR}{Count}{SEPARATOR}{Greatest}{SEPARATOR}{Average:.2f}\n"
    return Result
    


def main():
    print("Program starting. ")
    filename = input("Insert filename: ")
    values = readValues(filename)
    Result= analyseValues(values)
    print(f"{Result}")
    print("#### Number analysis - END ####")
    print("Program ending. ")

if __name__ == "__main__":
    main()
