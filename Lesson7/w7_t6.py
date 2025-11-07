import random
random.seed(1234)

# ASCII-artit
ART = {
    1: """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    2: """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    3: """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

CHOICES = {1: "rock", 2: "paper", 3: "scissors"}

def get_result(player_choice, bot_choice, player_name):
    if player_choice == bot_choice:
        return f"Draw! Both players chose {CHOICES[player_choice]}.", "draw"
    elif (player_choice == 1 and bot_choice == 3) or \
         (player_choice == 2 and bot_choice == 1) or \
         (player_choice == 3 and bot_choice == 2):
        reason = f"{player_name} {CHOICES[player_choice]} beats RPS-3PO {CHOICES[bot_choice]}."
        return reason, "win"
    else:
        reason = f"RPS-3PO {CHOICES[bot_choice]} beats {player_name} {CHOICES[player_choice]}."
        return reason, "loss"

def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

    wins = 0
    losses = 0
    draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 3.")
            continue

        if choice == 0:
            break
        if choice not in [1, 2, 3]:
            print("Invalid choice. Please select 1, 2, 3 or 0.")
            continue

        bot_choice = random.randint(1, 3)

        print("Rock! Paper! Scissors! Shoot!\n")
        print("#" * 25)
        print(f"{player_name} chose {CHOICES[choice]}.\n")
        print(ART[choice])
        print("#" * 25)
        print(f"RPS-3PO chose {CHOICES[bot_choice]}.\n")
        print(ART[bot_choice])
        print("#" * 25)

        result_text, outcome = get_result(choice, bot_choice, player_name)
        print(f"\n{result_text}\n")

        if outcome == "win":
            wins += 1
        elif outcome == "loss":
            losses += 1
        else:
            draws += 1

    print("\nResults:")
    print(f"{player_name} - wins ({wins}), losses ({losses}), draws ({draws})")
    print(f"RPS-3PO - wins ({losses}), losses ({wins}), draws ({draws})")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
