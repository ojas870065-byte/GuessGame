import random


def play_game():
    secret_number = random.randint(0, 100)

    for attempt in range(3):
        try:
            guess = int(input("Guess a value from 0 to 100: "))
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue

        if guess == secret_number:
            print("You won!")
            return
        elif attempt == 2:
            print(f"You lost. The correct guess was: {secret_number}")
        else:
            print("Wrong guess. Try again.")
            if guess > secret_number:
                print("Hint: Guess a smaller number.")
            else:
                print("Hint: Guess a higher number.")


def main():
    while True:
        play_game()

        choice = input("Do you want to play again? (Y/N): ").upper()
        if choice == 'Y':
            continue
        elif choice == 'N':
            print("Thank you for playing. You have exited the game.")
            break
        else:
            print("Invalid input. Exiting the game.")
            break


if __name__ == "__main__":
    main()