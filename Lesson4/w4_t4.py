print("Program starting. \n")

words = []

while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    words.append(word)

wordcount = len(words)
wordchar = sum(len(word) for word in words)

print("\nYou inserted: ")
print(f"- {wordcount} words" )
print(f"- {wordchar} characters" )

print("\nProgram ending. ")



