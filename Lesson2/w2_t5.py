print("Program starting.\n ")

Word = input("Insert a closed compound word: ")

print(f"The word you inserted is '{Word}' and in reverse it is '{Word[::-1]}'.")
print(f"The inserted word lenght is The inserted word length is {len(Word)}")
print(f"Last character is '{Word[-1]}'")
print("\nTake substring from the inserted word by inserting...")

Feed = int(input("1) Starting point: "))
Feed = int(input("2) Ending point: "))
Feed = int(input("3) Step size: "))

print(f"\nThe word '{Word}' sliced to the defined substring is '{Word[0:4:1]}'.")
print("Program ending. ")