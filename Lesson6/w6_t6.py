LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def collectRows():
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        
        rows.append(row)
    return rows

def shiftCharacter(char, alphabet):
    if char in alphabet:
        index = alphabet.index(char)
        return alphabet[(index + 13) % 26]
    return char

def rot13(text):
    result = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            result += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:
            result += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            result += char
    return result

def writeFile(filename, content):
    if filename == "":
        print("Filename not defined.")
        print("Aborting save operation. ")
    else:
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(content)
        print("Ciphered text saved! ")
    return None
         



def main():
    print("Program starting.")
    print("\nCollecting plain text rows for ciphering.")
    rows = collectRows()
    ciphered_rows = [rot13(row) for row in rows]
    result = "\n".join(ciphered_rows)
    print("\n#### Ciphered text ####")
    print(result)
    print("\n#### Ciphered text ####")
    filename = input("Enter filename to save: ")
    writeFile(filename, result)
    print("Program ending.")

if __name__ == "__main__":
    main()
