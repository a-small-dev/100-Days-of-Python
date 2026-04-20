# Simple CS Trivia App

A simple GUI-based quiz application built with Python that fetches real-time trivia questions from the Open Trivia Database API. The app presents True/False questions, tracks your score, and provides immediate feedback using a clean Tkinter interface.

---

## Features

* Fetches live quiz questions from an online API
* True/False question format
* Score tracking
* Instant feedback with color indicators (green/red)
* Simple and responsive GUI using Tkinter
* Clean modular code structure

---

## Project Structure

```
.
├── main.py              # Entry point of the application
├── quiz_brain.py        # Core quiz logic (question flow, scoring)
├── question_model.py    # Question object model
├── data.py              # API request and data handling
├── ui.py                # Tkinter GUI interface
├── images/
│   ├── true.png         # True button image
│   └── false.png        # False button image
```

---

## How It Works

1. `data.py` fetches 10 boolean (True/False) questions from the Open Trivia Database API.
2. `question_model.py` converts raw data into `Question` objects.
3. `quiz_brain.py` manages quiz progression, checks answers, and tracks score.
4. `ui.py` handles all user interaction through a Tkinter GUI.
5. `main.py` ties everything together and launches the app.

---

## Usage

Run the application:

```bash
python main.py
```

* Click the **True** or **False** buttons to answer questions.
* The background will flash:

  * **Green** for correct answers
  * **Red** for incorrect answers
* Your score updates in real time.

---

## API Used

* Open Trivia Database
  https://opentdb.com/

---

## Requirements

* Python 3.x
* `requests` library

---

## Future Improvements

* Add multiple-choice questions
* Timer for each question
* Difficulty selection
* Category selection
* High score saving
* Sound effects

---

## License

This project is free to use and modify.
