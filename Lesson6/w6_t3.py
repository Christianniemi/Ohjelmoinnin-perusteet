def copyFile():
    filename1 = input("Insert source filename: ")
    filename2 = input("Insert destination filename: ")
    print(f"Reading file \'{filename1}\'")
    file = open(filename1, "r")
    
    lines = []
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        lines.append(line)  
    file.close()
    file = open(filename2, "w")
    file.write(str(lines))
    file.close()



def main():
    print("Program starting. ")
    print("This program can copy a file. ")
    copyFile()
    print("Program ending. ")

if __name__ == "__main__":
    main()