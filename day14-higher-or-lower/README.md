# Higher or Lower

A terminal-based Python game where you guess which of two public figures or entities has more followers. Correct guesses increase your score; a wrong guess ends the game. This project demonstrates Python basics including functions, loops, data handling, and terminal UI.

---

## About the Project

The game compares two contestants from a dataset and asks the player to guess who has more followers. If the guess is correct, the player's score increases and a new challenger appears. The game ends when the player guesses incorrectly.

Key features:

- Interactive terminal gameplay
- Automatically generates new comparisons
- Tracks player score
- ASCII art stored in `art.py`
- Dataset stored in `game_data.py`
- Simple terminal screen clearing using multiple newlines

---

## Project Structure

- `main.py` — main game logic and loop  
- `art.py` — ASCII art and game logo  
- `game_data.py` — dataset used for comparisons  

---

## How to Run the Game

1. Make sure Python 3 is installed.  
2. Clone the repository:

   `git clone https://github.com/a-small-dev/100-Days-of-Python.git`  

3. Navigate to the project folder:

   `cd day14-higher-or-lower`  

4. Run the game:

   `python main.py`  

---

## How the Game Works

1. You are shown **Contestant A** and **Contestant B**.  
2. Type **A** or **B** to guess who has more followers.  
3. If correct:
   - Your score increases
   - Contestant B becomes the new Contestant A
   - A new challenger is chosen
4. One wrong guess ends the game

---

## Dependencies

- Python 3 (built-in modules only)  
- Local modules: `art.py`, `game_data.py`  
- No external packages required  

---

## Code Highlights

- Game logic organized into functions: `compare`, `initial_comparison`, `additional_comparison`  
- Input validation ensures only **A** or **B** is accepted  
- Screen clearing is done by printing multiple empty lines:

  `print("\n" * 40)`

- Main game loop repeats until an incorrect answer is given

---

## License

This project is free for learning and personal use. You can fork or modify it.
