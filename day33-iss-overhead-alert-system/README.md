# ISS Overhead Alert System

## Overview
This is a Python automation script that checks whether the International Space Station (ISS) is currently overhead your location during nighttime. If both conditions are met, it sends an email alert so you can step outside and try to see it.

The program runs continuously in the background and checks every 60 seconds.

---

## Features
- Tracks real-time ISS position using a public API  
- Determines sunrise and sunset based on your location  
- Detects whether it is currently dark outside  
- Checks if the ISS is within a visible range of your coordinates  
- Sends email alerts to one or more recipients  
- Runs continuously with automatic updates every minute  

---

## Technologies Used
- Python 3  
- requests (API calls)  
- datetime (time handling)  
- smtplib (email sending)  
- time (loop control)  

---

## APIs Used
- ISS Location API: http://api.open-notify.org/iss-now.json  
- Sunrise-Sunset API: https://api.sunrise-sunset.org/json  

---

## Setup Instructions

### 1. Install dependencies
```bash
pip install requests
```

---

### 2. Configure the script

Open `main.py` and set the following values directly in the code:

```python
MY_COORDINATES = (latitude, longitude)
MY_EMAIL = "your_email@example.com"
PASSWORD = "your_email_app_password"
EMAIL_LIST = ["recipient1@example.com", "recipient2@example.com"]
```

---

### 3. Run the program
```bash
python main.py
```

---

## How It Works
1. The script runs in an infinite loop with a 60-second delay.  
2. It checks whether it is currently night at your location.  
3. It retrieves the current position of the ISS.  
4. It checks if the ISS is within a defined coordinate range of your location.  
5. If both conditions are true, an email alert is sent.  

---

## Notes
- The ISS is only visible when it is dark at your location and the station is sunlit.  
- Visibility also depends on weather and sky conditions.  
- You may receive multiple alerts during a visible pass depending on timing.  
- Keep the script running in a terminal or background process.  

---

## License
Free to use for learning and personal projects.
