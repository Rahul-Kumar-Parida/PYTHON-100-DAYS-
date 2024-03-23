import random

def get_user_choice():
    user_choice = input("Enter 'snake', 'water', or 'gun': ").lower()
    if user_choice not in ['snake', 'water', 'gun']:
        print("Invalid choice. Please enter 'snake', 'water', or 'gun'.")
        return get_user_choice()
    return user_choice

def get_computer_choice():
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif user == 'snake':
        if computer == 'water':
            return "You win! Snake beats Water."
        else:
            return "Computer wins! Gun beats Snake."
    elif user == 'water':
        if computer == 'gun':
            return "You win! Water beats Gun."
        else:
            return "Computer wins! Snake beats Water."
    elif user == 'gun':
        if computer == 'snake':
            return "You win! Gun beats Snake."
        else:
            return "Computer wins! Water beats Gun."

def play_game():
    print("Welcome to Snake Water Gun game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()
