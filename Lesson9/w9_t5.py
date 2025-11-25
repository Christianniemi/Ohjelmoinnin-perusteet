ValueMin = 0
ValueMax = 255

def askIntByte(name: str) -> int:
    raw = input(f"Insert {name}: ")
    try:
        fval = float(raw)
        if not fval.is_integer():
            raise ValueError(f"Value \"{raw}\" is not an integer.")
        value = int(fval)
    except ValueError:
        raise ValueError(f"Value \"{raw}\" is non-numeric.")

    if not (ValueMin <= value <= ValueMax):
        raise ValueError(f"Value \"{raw}\" is out of the range 0-255.")

    return value


def createHex(r: int, g: int, b: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def main():
    print("Program starting.")
    try:
        r = askIntByte("red")
        g = askIntByte("green")
        b = askIntByte("blue")

        hex_color = createHex(r, g, b)
        print(hex_color)
        print(format(r, "08b"))
        print(format(g, "08b"))
        print(format(b, "08b"))

    except ValueError as e:
        print(e)
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


if __name__ == "__main__":
    main()


                
        
            
                 
            
            

        

   