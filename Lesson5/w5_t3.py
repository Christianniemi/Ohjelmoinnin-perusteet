def askName():
    name = input("Insert Name: ")
    return name

def greetUser(name):
    pname = name
    print(f"Hello {pname}!")
    return None

def main():
    print("Program starting.")
    name = askName()
    pname = greetUser(name)
    print("Program ending. ")
    return None

main()