# Flight Price Tracker

A Python-based flight monitoring tool that checks for low prices on selected routes and sends email alerts when deals are found.

## Features

- Fetches destination data from a Google Sheet (via Sheety API)
- Searches real-time flight prices using SerpAPI (Google Flights engine)
- Compares live prices against your target price thresholds
- Sends automated email alerts when cheaper flights are found
- Modular design with clean separation of concerns

---

## How It Works

1. **DataManager**
   - Retrieves destination cities, IATA codes, and target prices from a remote sheet.

2. **FlightSearch**
   - Queries the SerpAPI Google Flights endpoint for current flight data.

3. **FlightData**
   - Filters and compares flight prices against your predefined thresholds.

4. **NotificationManager**
   - Sends an email alert when a cheaper flight is detected.

---

## Project Structure


├── main.py  
├── data_manager.py  
├── flight_search.py  
├── flight_data.py  
├── notification_manager.py  
└── README.md  

---

## Setup & Installation

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/flight-price-tracker.git  
cd flight-price-tracker  

### 2. Install Dependencies

pip install requests python-dateutil  

---

## Environment Variables (IMPORTANT)

Before running the project, replace sensitive values with environment variables.

### Example:

SERP_API_KEY=your_serp_api_key  
EMAIL=your_email@gmail.com  
EMAIL_PASSWORD=your_app_password  
SHEETY_API_URL=your_sheety_endpoint  

Then update your code to use:

import os  
os.environ.get("SERP_API_KEY")  

**Never commit your API keys or passwords to GitHub.**

---

## Usage

Run the main script:

python main.py  

If a flight is found below your target price, you'll receive an email like:

Subject: ALERT: Low Flight Price  

Location: Paris  
Flight Code: CDG  
Departure Time: 2026-05-01 18:30  
Flight Price: $350  

---

## Example Workflow

- Your Google Sheet contains:
  - City name
  - IATA code
  - Target price  

- The script:
  - Pulls that data  
  - Searches flights from your departure airport  
  - Compares prices  
  - Sends alerts if a deal is found  

---

## Technologies Used

- Python 3  
- requests (API calls)  
- smtplib (email notifications)  
- python-dateutil (date calculations)  
- SerpAPI (Google Flights data)  
- Sheety API (Google Sheets integration)  

---

## Email Setup (Gmail)

To use Gmail SMTP:
- Enable 2FA  
- Generate an App Password  
- Use that instead of your real password  

---

## License

This project is licensed under the MIT License.
