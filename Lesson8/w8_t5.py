import loginLib

def user_menu(username: str):
    while True:
        print("\nUser menu options:")
        print("1 - View profile")
        print("2 - Change password (not implemented)")
        print("0 - Logout")
        choice = input("Your choice: ")

        if choice == "1":
            profile = loginLib.viewProfile(username)
            if profile:
                print(f"Profile:\n- ID: {profile[0]}\n- Username: {profile[1]}\n- Password hash: {profile[2]}")
            else:
                print("Profile not found.")
        elif choice == "2":
            print("Change password not implemented.")
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def main():
    print("Program starting.")
    while True:
        print("\nOptions:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            username = input("Insert username: ")
            password = input("Insert password: ")
            if loginLib.login(username, password):
                print("Login successful!")
                user_menu(username)
            else:
                print("Login failed. Wrong username or password.")
        elif choice == "2":
            username = input("Insert username: ")
            password = input("Insert password: ")
            loginLib.register(username, password)
            print("User registration completed!")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
    print("Program ending.")

if __name__ == "__main__":
    main()
