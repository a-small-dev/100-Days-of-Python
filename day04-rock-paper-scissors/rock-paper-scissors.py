import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ['Rock', 'Paper', 'Scissors']
art = [rock, paper, scissors]

bot_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))

while user_choice != 0 and user_choice != 1 and user_choice != 2:
    print("Invalid choice. Try again.")
    user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors."))

if user_choice == 0:
    print("You chose Rock")
    print(rock)
elif user_choice == 1:
    print("You chose Paper")
    print(paper)
else:
    print("You chose Scissors")
    print(scissors)

print(f"The computer chose {choices[bot_choice]}")
print(art[bot_choice])
if user_choice == bot_choice:
    print("Tie")
elif user_choice == 0 and bot_choice == 1:
    print("You lose")
elif user_choice == 0 and bot_choice == 2:
    print("You win")
elif user_choice == 1 and bot_choice == 0:
    print("You win")
elif user_choice == 1 and bot_choice == 2:
    print("You lose")
elif user_choice == 2 and bot_choice == 0:
    print("You lose")
else:
    print("You win")
