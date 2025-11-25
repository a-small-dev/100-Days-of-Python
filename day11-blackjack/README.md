# Blackjack with ASCII Art

A console-based Blackjack game written in Python, featuring ASCII card art for a visually appealing text-based experience. You play against the computer, draw cards, and see totals with fun ASCII representations. A standalone Windows `.exe` is also included for users who don’t want to install Python.

---

## Features
- Text-based Blackjack with ASCII art.
- Interactive prompts to draw cards or stay.
- Computer opponent that follows simple Blackjack rules.
- Handles Ace values (11 or 1) automatically.
- Option to play multiple rounds without restarting.
- Standalone `.exe` for Windows — no Python installation required.

---

## Installation

**Option 1: Python Version**
1. Clone the repo:
   git clone https://github.com/a-small-dev/100-Days-of-Python/day11-blackjack.git
2. Navigate into the folder:
   cd day11-blackjack
3. Run the game:
   python main.py

**Option 2: Standalone `.exe`**
- Double-click the included `blackjack.exe` to play on Windows — no Python installation required.

---

## How to Play
1. Start the game via Python or `.exe`.
2. Choose `y` to play or `n` to exit.
3. Two cards are dealt to both player and computer.
4. Choose whether to draw another card (`y`) or stay (`n`).
5. The computer will automatically take its turn.
6. The game announces the winner or a tie.
7. Option to play again at the end.

---

## Game Rules
- Number cards = face value.
- Face cards (J, Q, K) = 10 points.
- Ace = 11 or 1, depending on what prevents going over 21.
- Closest to 21 without going over wins.
- Tie if both player and computer have the same total.

---

## Project Structure
day11-blackjack/
├─ main.py           # Main game logic
├─ art.py            # ASCII art for cards and logos
├─ blackjack.exe     # Standalone Windows executable
└─ README.md         # This file

---

## TODO
- Improve ASCII art.
- Enhance computer AI.
- Add betting or scoring.
Open an issue or submit a pull request for improvements.

---

## License
This project is open-source under the MIT License.
