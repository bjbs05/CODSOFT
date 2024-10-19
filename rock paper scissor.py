import random

# Function to determine the winner
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!!"
    else:
        return "You lose :("

# Main game function
def game():
    user_score = 0
    computer_score = 0
    
    # Map shorthand inputs to full names
    choice_map = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors'
    }
    
    while True:
        # User input
        user_choice = input("Enter your choice between 'rock', 'paper', or 'scissors' (or use 'r', 'p', 's'): ").lower()

        # Check for accidental Enter press (empty input)
        if user_choice == "":
            print("You didn't enter anything! Please try again.")
            continue

        # Convert shorthand to full word
        if user_choice in choice_map:
            user_choice = choice_map[user_choice]
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Please enter a valid choice...")
            continue

        # Computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        # Determine and display result
        result = winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!!":
            user_score += 1
        elif result == "You lose :(":
            computer_score += 1

        # Display score
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play again
        while True:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower()

            # If user pressed Enter, confirm if they really want to exit
            if play_again == "":
                confirm = input("You pressed Enter. Do you really want to exit? (yes/no): ").lower()

                # If they press Enter again, prompt them to make a clear decision
                if confirm == "":
                    print("Please enter a valid choice (yes or no).")
                    continue  # Ask again for confirmation
                
                if confirm not in ["yes", "y"]:
                    print("Thanks for playing!")
                    return  # Exit the game
            elif play_again not in ["yes", "y"]:
                print("Thanks for playing!")
                return  # Exit the game
            else:
                break  # Continue playing if they choose "yes"

# Run the game
game()
