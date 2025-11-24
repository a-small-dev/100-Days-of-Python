# PyPassword Generator

A Python program that generates secure, randomized passwords based on user input.

## Description

This project allows users to create strong passwords with a mix of letters, numbers, and symbols.  
The program first generates a password with the requested number of letters, numbers, and symbols, then shuffles the characters to create a randomized, secure password.

## How to Use

1. Run the Python script:

       python py_password_generator.py

2. Enter the number of letters, symbols, and numbers you want in your password when prompted.

3. The program will display:

   - The password in the order of letters, symbols, and numbers.
   - A fully randomized password with all characters shuffled.

## Example Output

       Welcome to the PyPassword Generator!
       How many letters would you like in your password?
       4
       How many symbols would you like?
       2
       How many numbers would you like?
       2
       abcd!$12
       1b$2c!ad

## Features

- Generates passwords of any length
- Mixes letters (uppercase and lowercase), numbers, and symbols
- Randomizes character order for added security
