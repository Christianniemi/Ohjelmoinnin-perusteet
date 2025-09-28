print("Program starting. ")
print("String comparisons ")
word1 = input("Insert first word: ")
Char = input("Insert a character: ")
if (Char in word1):
    print(f"Word \"{word1}\" contains character \"{Char}\"")
else:
    print(f"Word {word1} doesn't contain character \"{Char}\"")
word2 = input("Insert second word: ")
if (word1 < word2):
    print(f"The first word \"{word1}\" is before the second word \"{word2}\" alphabetically. ")
elif(word2 < word1):
    print(f"The second word \"{word1}\" is before the first word \"{word2}\" alphabetically. ")
else:
    print(f"Both inserted words are the same alphabetically, \"{word1}\"")
print("Program ending. ")