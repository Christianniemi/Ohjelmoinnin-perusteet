import string

ALPHABET = string.ascii_uppercase

def load_config(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.read().splitlines()
    rotor1 = list(lines[0].split(":")[1])
    rotor2 = list(lines[1].split(":")[1])
    rotor3 = list(lines[2].split(":")[1])
    reflector = list(lines[3].split(":")[1])
    return [rotor1, rotor2, rotor3], reflector

def rotate(rotor_positions):
    rotor_positions[2] += 1
    if rotor_positions[2] == 26:
        rotor_positions[2] = 0
        rotor_positions[1] += 1
        if rotor_positions[1] == 26:
            rotor_positions[1] = 0
            rotor_positions[0] += 1
            if rotor_positions[0] == 26:
                rotor_positions[0] = 0

def forward_pass(letter, rotors, positions):
    index = ALPHABET.index(letter)
    for i in range(3):
        index = (index + positions[i]) % 26
        letter = rotors[i][index]
        index = ALPHABET.index(letter)
    return letter

def reflect(letter, reflector):
    index = ALPHABET.index(letter)
    return reflector[index]

def reverse_pass(letter, rotors, positions):
    index = ALPHABET.index(letter)
    for i in reversed(range(3)):
        index = (index - positions[i]) % 26
        letter = ALPHABET[index]
        index = rotors[i].index(letter)
        letter = ALPHABET[index]
    return letter

def enigma_encrypt(text, rotors, reflector):
    rotor_positions = [0, 0, 0]
    result = ""
    for char in text:
        if char not in ALPHABET:
            continue
        rotate(rotor_positions)
        print(f'Character "{char}" illuminated as ', end="")
        step1 = forward_pass(char, rotors, rotor_positions)
        step2 = reflect(step1, reflector)
        step3 = reverse_pass(step2, rotors, rotor_positions)
        print(f'"{step3}"')
        result += step3
    return result

def main():
    print("Insert config(filename): ", end="")
    config_file = input().strip()
    rotors, reflector = load_config(config_file)

    print("Insert plugs (y/n)?: ", end="")
    plug_input = input().strip().lower()
    if plug_input == "y":
        print("Plugboard not implemented.")
    else:
        print("No extra plugs inserted.")

    print("Enigma initialized.\n")

    while True:
        print("Insert row (empty stops): ", end="")
        row = input().strip().upper()
        if row == "":
            print("Enigma closing.")
            break
        print("\nRotor starting position")
        print("Rotor I   position: 0")
        print("Rotor II  position: 0")
        print("Rotor III position: 0\n")

        converted = enigma_encrypt(row, rotors, reflector)
        print(f'Converted row - "{converted}".\n')

        print("Current rotor position")
        print("Rotor I   position: 0")
        print("Rotor II  position: 0")
        print("Rotor III position: 0\n")
        print("CLEAR")
        print("press enter to reset rotors to position 0 and rerun inserted text\n")

if __name__ == "__main__":
    main()
