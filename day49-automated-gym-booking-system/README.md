# Automated Gym Booking System (Selenium Bot)

This project is a Python automation tool that simulates interacting with a gym booking website. It logs in, retrieves class schedules, allows users to book classes or join waitlists, and manage existing bookings.

It was built as a learning project to practice:
- Web automation with Selenium
- DOM parsing and dynamic content handling
- Menu-driven CLI applications
- Multi-module Python project structure

---

## ⚠️ Important Note

This project uses a **fake/demo gym website** provided for learning purposes.

If you want to try it out:
- You may need to run the program and sign up/log in using the provided test credentials or create an account on the demo site first
- After the initial setup/login, simply rerun the program and everything should work normally

---

## Features

- Automated login using Selenium
- Fetch and display weekly gym class schedule
- Select classes by day and view details
- Book classes or join waitlists
- View current bookings
- Cancel individual bookings or all bookings
- Menu-driven CLI interface

---

## Tech Stack

- Python 3
- Selenium WebDriver
- PrettyTable
- Chrome WebDriver

---

## Project Structure

project/
│
├── main.py          # Program entry point and flow control
├── menu.py          # User interface / menu logic
├── web_driver.py    # Selenium automation and scraping logic

---

## How It Works

1. Launches Chrome and logs into the gym site automatically  
2. Retrieves schedule data from the website  
3. Displays a CLI menu for user interaction  
4. Allows booking, viewing, and cancelling classes  
5. Handles navigation between schedule and bookings pages  

---

## Setup Instructions

### 1. Install dependencies
pip install selenium prettytable

### 2. Ensure ChromeDriver is installed
Make sure your ChromeDriver version matches your installed Chrome browser.

### 3. Run the program
python main.py

---

## Notes

- This project uses a persistent Chrome profile (`chrome_profile`) so login sessions may persist between runs.
- The automation is designed for a demo environment and may break if the site structure changes.
- Some waits are handled using Selenium's WebDriverWait.

---

## What I Learned

- Structuring a multi-file Python project
- Using Selenium for real-world automation tasks
- Handling dynamic web elements and asynchronous loading
- Designing menu-driven CLI systems
- Managing application state across modules
