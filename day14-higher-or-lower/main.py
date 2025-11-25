"""
Higher or Lower Project
"""
# Imports necessary modules
import random
import art
import game_data


# Declaring Variables
game_over = False # Boolean to check if game over conditions are met
winning = False # Boolean to check if additional comparisons should be done
score = 0 # Player score
contestant = 0 # Passes the bottom contender to the next round

# Defining Functions

# Clears terminal
def clear_screen():
   print("\n" * 40)

# Game over screen
def game_over_screen():
    clear_screen()
    print(art.logo)
    print(f"Sorry you lost your total score is: {score}.")

# Compare and returns result of answers
def compare(choice, n1, n2):
    global winning
    global contestant
    global score
    if game_data.data[n1]['follower_count'] > game_data.data[n2]['follower_count'] and choice == "A":
        winning = True
        contestant = n2
        score += 1
        return False
    elif game_data.data[n1]['follower_count'] < game_data.data[n2]['follower_count'] and choice == "B":
        winning = True
        contestant = n2
        score += 1
        return False
    else:
        winning = False
        return True

# Runs the initial comparison
def initial_comparison():
    n1 = random.randint(0,50)
    n2 = random.randint(0,50)
    while n1 == n2:
        n2 = random.randint(0,50)
    print(f"Compare A: {game_data.data[n1]['name']}, a {game_data.data[n1]['description']}, from {game_data.data[n1]['country']}.")
    print(art.vs)
    print(f"Against B: {game_data.data[n2]['name']}, a {game_data.data[n2]['description']}, from {game_data.data[n2]['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    while choice != "A" and choice != "B":
        input(f"{choice} is not a valid choice. Please try again.")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    result = compare(choice, n1, n2)
    return result

# Runs additional comparisons
def additional_comparison(n1):
    clear_screen()
    n2 = random.randint(0, 50)
    while n1 == n2:
        n2 = random.randint(0, 50)
    print(art.logo)
    print(f"You're right! Current score: {score}.")
    print(f"Compare A: {game_data.data[n1]['name']}, a {game_data.data[n1]['description']}, from {game_data.data[n1]['country']}.")
    print(art.vs)
    print(f"Against B: {game_data.data[n2]['name']}, a {game_data.data[n2]['description']}, from {game_data.data[n2]['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    while choice != "A" and choice != "B":
        input(f"{choice} is not a valid choice. Please try again.")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    result = compare(choice, n1, n2)
    return result


# Main game loop
while not game_over:
    print(art.logo)
    game_over = initial_comparison()
    if game_over:
        break
    while winning:
        game_over = additional_comparison(contestant)
        if not winning:
            break
game_over_screen()