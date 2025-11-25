import sys
import os

def showHelp() -> None:
    
    print("[USAGE] python w9_t7.py src_file dst_file".format(sys.argv[0]))
    print("Program ending. ")
    return None


def copyFile(PSrcFile: str, PDstFile: str) -> None:
    
    proceed = True

    # Jos kohdetiedosto on jo olemassa, kysytään lupa ylikirjoitukseen
    if os.path.exists(PDstFile):
        choice = input(f'Destination file "{PDstFile}" already exists.\nDo you want to overwrite (y/n)? ').strip().lower()
        if choice != "y":
            
            proceed = False

    if proceed:
        try:
            print(f'Copying file "{PSrcFile}" to "{PDstFile}".')
            with open(PSrcFile, "r", encoding="UTF-8") as src:
                contents = src.read()
            with open(PDstFile, "w", encoding="UTF-8") as dst:
                dst.write(contents)
            
        except OSError:
            sys.exit(-1)


def main() -> None:
    print("Program starting.")

    # Tarkistetaan argumenttien määrä
    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        sys.exit(-1)

    srcFile = sys.argv[1]
    dstFile = sys.argv[2]

    print(f'Source file "{srcFile}"')
    print(f'Destination file "{dstFile}"')

    copyFile(srcFile, dstFile)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()

