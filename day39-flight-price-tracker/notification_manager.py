import smtplib

class NotificationManager:
    def __init__(self):
        self.MY_EMAIL = "YOUR GOOGLE EMAIL HERE"
        self.PASSWORD = "YOUR EMAIL PASSWORD HERE"

    def send_alert(self, location, code, time, price):
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=self.MY_EMAIL, password=self.PASSWORD)
        connection.sendmail(from_addr=self.MY_EMAIL, to_addrs=self.MY_EMAIL,
                            msg=f"Subject: ALERT: Low Flight Price\n\nLocation: {location}\n"
                                f"Flight Code: {code}\nDeparture Time: {time}\nFlight Price: ${price}\n\nThis message was automatically"
                                f" sent from my Python program.")
        connection.close()