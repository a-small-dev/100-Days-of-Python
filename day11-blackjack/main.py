"""
Blackjack Project with ASCII art
"""
# Imports necessary modules
import art
import random

# Initializing variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
draw_art = []
draw_bot_art = []
user_cards = []
user_total = 0
bot_cards = []
bot_total = 0
play = True
run = ""

# Defining Functions

# Start Game
def start_game():
    run = input("Would you like to play? Type 'y' or 'n'. : ").lower()
    while run != "y" and run != "n":
        print(f"{run} is not a valid option.")
        run = input("Would you like to play? Type 'y' or 'n': ").lower()
    if run == "y":
        print("\n" * 3)
        return True
    else:
        print("\n" * 8)
        print(art.end_logo)
        return False

# Initial Card Draw For User
def draw_cards():
    total = 0
    for i in range(2):
        index = random.randint(0, len(cards) - 1)
        card = cards[index]
        user_cards.append(card)
        total += card
        index += (random.randint(1, 5) * 13) % 52
        draw_art.append(index)
    card_art(draw_art)
    print("-" * 15)
    print(f"You have {total}")
    print("-" * 15)
    return total

# Resets Variable Values
def reset_variables():
    global draw_art, user_cards, bot_cards, bot_total, user_total, run, draw_bot_art
    draw_art = []
    draw_bot_art = []
    user_cards = []
    user_total = 0
    bot_cards = []
    bot_total = 0
    run = ""

# Prints Card Art (5 cards MAX)
def card_art(n1):
    if len(n1) == 2:
        for i in range(8):
            print(art.cards[n1[0]].splitlines()[i], art.cards[n1[1]].splitlines()[i])
    elif len(n1) == 3:
        for i in range(8):
            print(art.cards[n1[0]].splitlines()[i], art.cards[n1[1]].splitlines()[i], art.cards[n1[2]].splitlines()[i])
    elif len(n1) == 4:
        for i in range(8):
            print(art.cards[n1[0]].splitlines()[i], art.cards[n1[1]].splitlines()[i], art.cards[n1[2]].splitlines()[i],
                  art.cards[n1[3]].splitlines()[i])
    else:
        for i in range(8):
            print(art.cards[n1[0]].splitlines()[i], art.cards[n1[1]].splitlines()[i], art.cards[n1[2]].splitlines()[i],
                  art.cards[n1[3]].splitlines()[i], art.cards[n1[4]].splitlines()[i])

# Initial Card Draw For User
def draw_bot():
    total = 0
    for i in range(2):
        index = random.randint(0, len(cards) - 1)
        card = cards[index]
        bot_cards.append(card)
        total += card
        index += (random.randint(1, 5) * 13) % 52
        draw_bot_art.append(index)
    card_art(draw_bot_art)
    print("-" * 15)
    print(f"The computer has {total}")
    print("-" * 15)
    return total

# Checks For Game Over Conditions
def check_if_gameover(n1, n2):
    if n1 > 21:
        for i in range(len(user_cards)):
            if user_cards[i] == 11:
                user_cards[i] = 1
                n1 -= 10
                break
            else:
                continue
    if n2 > 21:
        for i in range(len(bot_cards)):
            if bot_cards[i] == 11:
                bot_cards[i] = 1
                n2 -= 10
                break
            else:
                continue
    if n1 > 21 and n2 <= 21:
        print("#" * 15)
        print("#  Game Over! #\n#  You Lose!  #")
        print("#" * 15)
        return False
    elif n1 <= 21 and n2 > 21:
        print("#" * 15)
        print("#  Game Over! #\n#   You Win!  #")
        print("#" * 15)
        return False
    elif n1 == 21 and n2 == 21:
        print("#" * 15)
        print("#  Game Over! #\n#  Tie Game!  #")
        print("#" * 15)
        return False
    elif n1 == 21 and n2 < 21:
        print("#" * 15)
        print("#  Game Over! #\n#   You Win!  #")
        print("#" * 15)
        return False
    elif n1 < 21 and n2 == 21:
        print("#" * 15)
        print("#  Game Over! #\n#  You Lose!  #")
        print("#" * 15)
        return False
    else:
        return True

# Checks To See If User Wants To Draw Again
def drawing():
    choice = input("Would you like to draw another card? Type 'y' or 'n': ").lower()
    while choice != "y" and choice != "n":
        print(f"{choice} is not a valid option.")
        choice = input("Would you like to draw another card? Type 'y' or 'n': ").lower()
    if choice == "y":
        return True
    else:
        return False

# Draw Additional Card For User
def draw_again(n1):
        index = random.randint(0, len(cards) - 1)
        card = cards[index]
        user_cards.append(card)
        n1 += card
        index += (random.randint(1, 5) * 13) % 52
        draw_art.append(index)
        card_art(draw_art)
        if n1 > 21:
            for i in range(len(user_cards)):
                if user_cards[i] == 11:
                    user_cards[i] = 1
                    n1 -= 10
                    break
                else:
                    continue
        print(f"You have {n1}")
        return n1

# Draws Cards For Computer Until A Game Over Condition Is Met
def computers_turn(n1, n2):
    if n2 <= n1:
        print()
        print("Computer draws a card...")
        index = random.randint(0, len(cards) - 1)
        card = cards[index]
        bot_cards.append(card)
        index += (random.randint(1, 5) * 13) % 52
        draw_bot_art.append(index)
        card_art(draw_bot_art)
        n2 += card
        if n2 > 21:
            for i in range(len(bot_cards)):
                if bot_cards[i] == 11:
                    bot_cards[i] = 1
                    n2 -= 10
                    break
        return n2
    else:
        return n2

# Prompts User To See If They Want To Play Again
def play_again():
    print()
    choice = input("Would you like to play again? Type 'y' or 'n': ").lower()
    while choice != "y" and choice != "n":
        print(f"{choice} is not a valid option.")
        choice = input("Would you like to play again? Type 'y' or 'n': ").lower()
    if choice == "y":
        reset_variables()
        main()
    else:
        print("\n" * 8)
        print(art.logo)
        print(art.end_logo)

# Main Game Loop
def main():
    print(art.logo)
    play = start_game()

    # Initial draw
    while play:
        bot_total = draw_bot()
        user_total = draw_cards()
        play = check_if_gameover(user_total, bot_total)

        # Checks for game over
        if not play:
            break

    # Check if user wants more cards
        play_check = drawing()
        while play_check:
            user_total = draw_again(user_total)
            play = check_if_gameover(user_total, bot_total)
            if play == False:
                break
            play_check = drawing()

        # Checks for game over
        if not play:
            break

        # Player -> Computer Turn Transition
        print("-" * 15)
        print(f"The computer has {bot_total}")
        print(f"You decide to stay with {user_total}")
        print("-" * 15)
        print("Computer's turn")

        # Computer's Turn
        while bot_total <= user_total:
            bot_total = computers_turn(user_total, bot_total)
            print(f"Computer has {bot_total}")
            play = check_if_gameover(user_total, bot_total)
            if play == False:
                break
        # Checks for game over
        if not play:
            break

        # Game over sequence
        print("#" * 15)
        print("#  Game Over! #\n#  You Lose!  #")
        print("#" * 15)
        play = False

    # Asks user if they want to play again
    play_again()

# Runs main
main()
