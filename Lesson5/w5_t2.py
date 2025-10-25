def frameWord (word):
    pword = '*' * (len(word) + 4)
    print("")
    print(pword)
    print(f'* {word} *')
    print(pword)
    return None

def main():
    print("Program starting.")
    word = input("Insert word: ")
    frameWord(word)
    print("\nProgram ending.")
    return None
main()

    










    



