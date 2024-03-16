import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    user_move = input("Enter your choice (Rock, Paper, or Scissors): ")
    possible_moves = ["Rock", "Paper", "Scissors"]
    computer_move = random.choice(possible_moves)
    print(f"\nYou chose {user_move}, computer chose {computer_move}.\n")

    if user_move == computer_move:
        print(f"Both players selected {user_move}. It's a tie!")
    elif (user_move == "Rock" and computer_move == "Scissors") or (user_move == "Paper" and computer_move == "Rock") or (user_move == "Scissors" and computer_move == "Paper"):
        print(f"{user_move} beats {computer_move}! You win!")
    else:
        print(f"{computer_move} beats {user_move}! You lose!")

    play_again = input("Do you want to play again? (Yes/No): ")
    if play_again != "Yes":
        print("Thanks for playing!")
        break
