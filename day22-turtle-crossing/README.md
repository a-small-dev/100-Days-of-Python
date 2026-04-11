# The Turtle vs 460

A simple arcade-style game built with Python’s Turtle graphics module.  
Guide your turtle safely across the road while avoiding incoming cars that get faster each level.

---

## Gameplay

You control a turtle trying to cross a busy road. Each time you successfully reach the top of the screen, you advance to the next level—but the cars get faster and more dangerous.

Get hit too many times, and it's game over!

---

##  Features

- Increasing difficulty (cars speed up each level)
- Randomly generated cars with different colors
- Collision detection system
- Lives system
- Level tracking
- Game over screen with final level reached

---

## Controls

| Key | Action |
|-----|--------|
| ↑ (Up Arrow) | Move forward |
| Release ↑ | Stop moving |

---

## Project Structure

```bash
.
├── main.py          # Main game loop and logic
├── user.py          # Player movement and behavior
├── cars.py          # Car generation and movement
├── scoreboard.py    # Score, level, and lives display
```
## Game Over

The game ends when you run out of lives.  
A message will display showing the highest level you reached.

---

## Built With

- Python
- Turtle Graphics

---

##  License

This project is open-source and free to use.
