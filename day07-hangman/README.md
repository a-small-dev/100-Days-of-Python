# Hangman Game

A Python implementation of the classic Hangman game with ASCII art.

## Description

This project lets a player guess letters to figure out a hidden word.  
The game includes:

- A random word selected from a word list (`hangman_words.py`)  
- ASCII art for the Hangman stages (`hangman_art.py`)  
- Limited lives for incorrect guesses  

The player wins if they guess all letters correctly before running out of lives.

## How to Play

1. Make sure all files are in the same folder:

       main.py
       hangman_words.py
       hangman_art.py

2. Run the main script:

       python main.py

3. Guess one letter at a time.  
   - If the letter is in the word, it will appear in its correct position.  
   - If the letter is not in the word, you lose one life.  
   - Repeat until you either guess the word or run out of lives.

## Example Output

       ****************************6/6 LIVES LEFT****************************
       Guess a letter: a
       Word to guess: _ a _ _ _
       ****************************5/6 LIVES LEFT****************************
       Guess a letter: b
       b is not in the word, you lose a life!
       [ASCII art showing Hangman stage]

       ****************************YOU WIN****************************

## Features

- Random word selection
- Tracks previously guessed letters
- ASCII art stages for visual effect
- Limited lives adds challenge
