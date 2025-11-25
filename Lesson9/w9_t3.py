
def readFile():
    filename = input("Insert filename: ")
    try:
        with open(filename, "r", encoding="utf-8" ) as file:
            content = file.read()
            print(f"## {filename} ##")
            
            print(content.strip())
            print(f"## {filename} ##")
    except FileNotFoundError:
        print(f"Couldn't read file \"{filename}\"")

def main():
    print("Program starting")
    readFile()
    print("Program ending. ")
if __name__ == "__main__":
    main()