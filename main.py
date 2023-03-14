import random

print("Welcome in game 'rock, paper, scissors'")
user_choice = input("Choose:\n"
                    "1 - rock ✊\n"
                    "2 - paper ✋\n"
                    "3 - scissors ✌️\n"
                    "Your choice: ")

# kamien wygrywa z nozyczkami, a przegrywa z papierem
# papier wygrywa z kamieniem, a przegrywa z nozyczkami
# nozyczki wygrywaja z papierem, a przegrywaja z kamieniem

computer_random_choice = random.randint(1, 3)
print(f"Computer choice is {computer_random_choice}")

user_choice_int = int(user_choice)

if user_choice_int < 1 or user_choice_int > 4:
    print("Invalid choice")
elif user_choice_int == 1 and computer_random_choice == 3:
    print("You win")
elif computer_random_choice == 1 and user_choice_int == 3:
    print("Computer win")
elif computer_random_choice > user_choice_int:
    print("Computer win")
elif user_choice_int > computer_random_choice:
    print("You win")
elif computer_random_choice == user_choice_int:
    print("Draw")

