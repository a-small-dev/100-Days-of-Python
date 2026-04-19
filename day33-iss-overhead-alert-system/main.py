import requests, datetime, smtplib, time

# replace these const values with your information
MY_COORDINATES = ("YOUR COORDINATES HERE (LAT, LONG)")
MY_EMAIL = ("YOUR EMAIL HERE")
PASSWORD = ("YOUR APP PASSWORD HERE")
EMAIL_LIST = ["YOUR RECEIVING EMAIL ADDRESSES HERE"]
SUN_PARAMETERS = {"lat": MY_COORDINATES[0], "lng": MY_COORDINATES[1], "tzid": "America/New_York"}
LAT_MIN = MY_COORDINATES[0] - 5
LAT_MAX = MY_COORDINATES[0] + 5
LONG_MIN = MY_COORDINATES[1] - 5
LONG_MAX = MY_COORDINATES[1] + 5

# formats time for logical operations
def format_time(unformatted_time):
    dt = datetime.datetime.strptime(unformatted_time, "%I:%M:%S %p")
    return dt.hour * 10000 + dt.minute * 100 + dt.second

# checks to see if it is currently dark at your location
def is_dark():
    current_date = datetime.datetime.now()
    current_time = current_date.strftime("%I:%M:%S %p")
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=SUN_PARAMETERS)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    formatted_sunrise = format_time(sunrise)
    formatted_sunset = format_time(sunset)
    formatted_current_time = format_time(current_time)
    if formatted_current_time > formatted_sunset or formatted_current_time < formatted_sunrise:
        return True
    else:
        return False

# checks to see if the ISS is near your location
def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = data["iss_position"]["latitude"]
    iss_longitude = data["iss_position"]["longitude"]
    if LAT_MIN < float(iss_latitude) < LAT_MAX and LONG_MIN < float(iss_longitude) < LONG_MAX:
        return True
    else:
        return False

# if it is dark and ISS is near, this will send an email alerting you or friends that live nearby (your email list)
while True:
    time.sleep(60)
    if is_dark() and is_above():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        for email in EMAIL_LIST:
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                                msg=f"Subject: International Space Station Alert\n\nThe ISS is in your area right now!\n"
                                    f"\nTake a look up outside and see if you can spot it!\n\nThis message was automatically"
                                    f"sent from my Python program.")
        connection.close()
