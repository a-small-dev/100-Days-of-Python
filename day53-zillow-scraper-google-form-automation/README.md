# Zillow Scraper → Google Form Automation

This project scrapes real estate listings from a Zillow-style webpage and automatically submits the extracted data into a Google Form using Selenium.

It combines web scraping (BeautifulSoup + requests) with browser automation (Selenium) to simulate a real-world data pipeline.

---

## Features

- Scrapes property listings from a Zillow clone site
- Extracts:
  - Address
  - Price
  - Bedrooms
  - Bathrooms
  - Listing URL
- Automatically fills and submits a Google Form
- Repeats submission for all listings found
- Uses Selenium with Chrome WebDriver

---

## How It Works

### Scraping (soup.py)
- Sends a request to the Zillow clone page
- Parses HTML using BeautifulSoup
- Extracts listing data from each property card
- Stores results in a dictionary

### Automation (driver.py)
- Opens a Google Form using Selenium
- Waits for input fields to load
- Fills in each listing’s data:
  - Address
  - Price
  - Bedrooms
  - Bathrooms
  - URL
- Submits the form
- Clicks “Submit another response” to continue looping

### Main (main.py)
- Initializes the parser and driver
- Scrapes and formats data
- Sends data to Google Form automation
- Closes the browser when complete

---

## Project Structure

main.py        -> Entry point  
driver.py      -> Selenium automation logic  
soup.py        -> Web scraping logic  

---

## Important Notes

- This project uses a Zillow clone site (not real Zillow data)

---

## What I Learned/Practiced

- Web scraping with BeautifulSoup
- Parsing HTML structures
- Browser automation with Selenium
- Data pipelines (scrape → transform → submit)
- Handling dynamic web pages
