def writeFile():
    name1= input("Insert firstname: ")
    name2= input("Insert lastname: ")
    filename = input("Insert filename: ")
    file = open(filename, "w")
    file.write(name1 + "\n")
    file.write(name2)
    file.close()

def main():
    print("Program starting.")
    writeFile()

if __name__ == "__main__":
    main()