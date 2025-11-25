# Coffee Machine Project

A console-based coffee machine simulator written in Python. Choose between **espresso**, **latte**, and **cappuccino**; the program checks resources, accepts coin input, returns change, and displays coffee ASCII art when a drink is served.

---

## Features
- Drink options: `espresso`, `latte`, `cappuccino`
- Resource management (water, milk, coffee)
- Coin input with validation (quarters, dimes, nickels, pennies)
- Change calculation and total money tracking
- `report` command for viewing machine status
- `off` command to shut down the machine
- ASCII art display when a drink is dispensed (stored in `art.py`)

---

## Files in this Repository
- **main.py** – core logic and user interface  
- **data.py** – drink recipes (`MENU`) and starting machine resources  
- **art.py** – ASCII art used for the machine logo and coffee graphic

---

## Installation

1. Clone the repository:
    
    git clone https://github.com/a-small-dev/100-Days-of-Python.git

2. Enter the project directory:
    
    cd day15-coffee-machine

3. Run the program:
    
    python main.py

---

## How It Works
- User selects a drink.
- The machine checks available resources needed for that drink.
- If resources are sufficient, the user is prompted to insert coins.
- Coin totals are calculated, the cost is deducted, and change is returned.
- Resources are updated and coffee ASCII art is printed.
- The `report` command shows current resources and total money.
- The `off` command stops the program.

---

## Skills Practiced
This project helped me reinforce several core Python fundamentals:

- **Control flow**  
  Using loops, conditionals, and structured branching.

- **Error handling**  
  Implementing `try`/`except` blocks for safe input validation.

- **Functions and modularity**  
  Organizing code into separate functions for clarity and reusability.

- **Working with external modules**  
  Importing and using supporting files like `data.py` and `art.py`.

- **Basic arithmetic and data processing**  
  Calculating coin totals, updating resources, and processing drink costs.

---

## License

MIT License
