def readFile():
    filename = input("Insert filename to read: ")
    print(f"Reading names from \"{filename}\"")
    file = open(filename, "r")
    lines = []
    while True:
        
        line = file.readline()
        if line == "":
            break
        lines.append(line)
    file.close ()
        
    return lines

def analyseLines(lines1):
    line = 0
    while True:
        if line in lines1 == "":
            len(lines1) = -1
            print len(lines1)
        else:
            print(lines1)

    
    return None



def main():
    print("Program starting. ")
    print("This program analyses a list of names from a file. ")
    lines = readFile()
    analyseLines(lines)
if __name__ == "__main__":
    main()