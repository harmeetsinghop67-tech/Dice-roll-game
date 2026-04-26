import random

#  Function to roll dice 
def roll_dice():
    return random.randint(1, 6)


#  Game Logic 
def play_game():
    input("\n Press Enter to roll the dice...")

    user = roll_dice()
    computer = roll_dice()

    print(f"\nYou rolled: {user}")
    print(f"Computer rolled: {computer}")

    if user > computer:
        print(" You win!")
    elif user < computer:
        print(" Computer wins!")
    else:
        print(" It's a tie!")


#  Menu 
def menu():
    while True:
        print("\n" + "="*30)
        print("🎮 DICE ROLL GAME")
        print("="*30)
        print("1. Play Game")
        print("2. Exit")
        print("="*30)

        choice = input(" Enter your choice: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            print(" Thanks for playing!")
            break
        else:
            print(" Invalid choice. Try again.")


#  Run Program 
menu()