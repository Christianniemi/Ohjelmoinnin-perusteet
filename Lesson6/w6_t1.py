def readFile():
    Filename = input("Insert filename: ")
    print(f"#### START \"{Filename}\" ####")
    file = open(Filename, "r")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        print(line, end="")
    file.close()
    return Filename


def main():
    print("Program starting")
    print("This program can read a file.")
    Filename = readFile()
    print(f"\n#### END \"{Filename}\" ####")
    print("Program ending. ") 
    



if __name__ == "__main__":
    main()