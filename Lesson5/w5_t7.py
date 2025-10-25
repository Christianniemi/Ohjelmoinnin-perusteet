DELIMETER = ","

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
        
    return DELIMETER.join(words)

def analyseWords(words1):
    wordlength = words1.count(DELIMETER) +1 if words1 else 0
    print(f"- {wordlength} Words")
    total_char = len(words1.replace(DELIMETER, ""))
    

    Avg = total_char / wordlength
    print(f"- {total_char} Characters")
    print("- {:.2f} Average word length".format(Avg))   
    return 


def main():
    print("Program starting.")
    words= collectWords()
    words1 = analyseWords(words)
    print("Program ending. ")

main()



