DELIMETER = ","
LOGO1 = "# --- Vertically --- #"
LOGO2 = "# --- Horizontally --- #"

def askFilename():
    
    filename = input("Inser filename: ")
    with open (filename, "r") as file:
        content = file.readlines()
        
    return content

def workLines(Plines):
    print(LOGO1)
    for line in Plines:
        numbers = line.strip()
        
        print(numbers)
    print(LOGO1)
    print(LOGO2)
    cleanednumbers = []
    for line in Plines:
        line = line.strip()
        if line.isdigit():
            cleanednumbers.append(line)
    result = DELIMETER.join(cleanednumbers)
    print(result)

    print(LOGO2)

    return 

def main():
    print("Program starting. ")
    content = askFilename()
    workLines(content)
    print("Program ending. ")
if __name__ == "__main__":
    main()