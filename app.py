# print "hello world" to the console
print("hello world")

# write a code that takes a user input of rock, paper or scissiors and randomly selects one of the three for the computer
# The code should then determine the winner of the game
# The code should then ask the user if they would like to play again
import random
def rock_paper_scissors():
    while True:
        print("Welcome to rock, paper, scissors")
        user_input = input("Enter rock, paper or scissors: ")
        computer_input = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose {computer_input}")
        if user_input == computer_input:
            print("It's a draw!")
        elif user_input == "rock" and computer_input == "scissors":
            print("You win!")
        elif user_input == "rock" and computer_input == "paper":
            print("You lose!")
        elif user_input == "paper" and computer_input == "rock":
            print("You win!")
        elif user_input == "paper" and computer_input == "scissors":
            print("You lose!")
        elif user_input == "scissors" and computer_input == "paper":
            print("You win!")
        elif user_input == "scissors" and computer_input == "rock":
            print("You lose!")
        else:
            print("Invalid input!")
        print("Would you like to play again?")
        if input("Enter 'yes' or 'no': ") == "no":
            break

rock_paper_scissors()

