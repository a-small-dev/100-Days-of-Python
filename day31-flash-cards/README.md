# CS Flashcards – Python Computer Science Terms

A simple interactive flashcard application built with Python and Tkinter to help users study and memorize foundational computer science concepts.

This project uses a dataset of 60+ core CS terms and definitions and presents them in a randomized flashcard format with a graphical user interface.

---

## Features

- Randomized flashcard generation
- Tkinter-based graphical user interface
- “Remember” and “Don’t Remember” buttons
- Automatic transition to next card
- Removes mastered terms dynamically
- Clean wrapped text for readability
- Built from a real CS vocabulary dataset

---

## Dataset

The dataset is a CSV file with two columns:

Term – computer science concept  
Definition – explanation of the concept  

Example:

Algorithm – step-by-step procedure to solve a problem efficiently  
Stack – Last-In, First-Out data structure  

---

## Technologies Used

- Python 3
- Tkinter
- Pandas
- Random module
- Textwrap module

---

## Project Structure

project/
- main.py  
- top_60_cs_terms.csv  
- README.md  

---

## How It Works

1. A random term is selected from the dataset  
2. The definition is displayed on the screen  
3. User chooses:
   - Don’t Remember ("X" button) → card returns later  
   - Remember ("Y" button) → card is removed  
4. Process repeats until deck is empty  

---

## Purpose

This project was built as a learning tool to improve understanding of core computer science vocabulary while practicing Python GUI development.

---

## License

This project is free to use.
