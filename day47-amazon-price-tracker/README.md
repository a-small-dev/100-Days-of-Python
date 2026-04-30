# Amazon Price Tracker

A Python-based web scraping tool that monitors the price of a product on Amazon and sends an email alert when the price drops below a defined threshold.

This project demonstrates web scraping, environment variable management, and automated email notifications using Python.

---

## Features

- Scrapes real-time product price from Amazon
- Extracts pricing data using BeautifulSoup
- Compares current price against a target threshold
- Sends automated email alerts when price drops
- Uses environment variables for secure credential storage
- SMTP integration for Gmail or custom email servers

---

## How It Works

### Web Scraping
The script sends a request to the Amazon product page and parses the HTML to locate:

- Whole price (`a-price-whole`)
- Fractional price (`a-price-fraction`)

These values are combined into a single float for comparison.

---

### Price Monitoring
- The current price is compared against a predefined threshold (e.g. 240.00)
- If the price is lower, the alert system is triggered

---

### Email Notification
- Uses SMTP to send an automated email
- Credentials are securely loaded from environment variables
- Sends product link and alert message to the user

---

## Example Email Alert

Subject: CAR SEAT PRICE ALERT  

The price for the product is currently below your target price.

Product Link:  
https://www.amazon.com/...

This message was automatically sent from a Python program.

---

## Technologies Used

- requests
- BeautifulSoup4
- smtplib
- python-dotenv
- Amazon product page scraping

---

## Learning Outcomes

- Web scraping dynamic product pages
- Parsing HTML with BeautifulSoup
- Working with environment variables securely
- Automating email notifications with SMTP
- Building real-world monitoring tools in Python
