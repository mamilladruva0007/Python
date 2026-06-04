import random

options = ('rock', 'paper', 'scissors')

computer_score = 0
user_score = 0

while True:
    user_input = input("Enter a choice (rock/paper/scissors or q to quit): ").lower()
    
    if user_input == "q":
        break
    elif user_input not in options:
        print("Invalid input")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user_input == computer:
        print("Draw")
        print()
    elif user_input == "rock" and computer == "scissors":
        print("User-Won")
        user_score += 1
    elif user_input == "paper" and computer == "rock":
        print("User-Won")
        user_score += 1
    elif user_input == "scissors" and computer == "paper":
        print("User-Won")
        user_score += 1
    else:
        print("Computer-Won")
        computer_score += 1

print(f"User Score = {user_score}")
print(f"Computer Score = {computer_score}")
