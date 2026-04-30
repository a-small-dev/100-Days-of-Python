import requests, smtplib, os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

response = requests.get(url="https://www.amazon.com/Chicco-ClearTex®-Rear-Facing-Compatible-Strollers/dp/B0DTLRY7RP/ref="
                            "mp_s_a_1_26_sspa?dib=eyJ2IjoiMSJ9.oXvA3AXCU6r-dKSNAICcGP-1mCSbyBSH9WJoSl_96j91lyFHlomugwkkl"
                            "zR-t1SsGeyY2J2YzT0uric6RNlNiPL7D4Ed5Yb9hKx1r_lIVl82ATsREFOLSXG2Dg2kOOTZ9zBvXEQMcl8KDESnSDcd"
                            "teuyRL5Bz7adyRFS4RwwsJBVq1AQmvCDpc9jhxYpSCocWBNKDWzolkEKs9iQ66DIeQ.h7SXA5vUX7_1pxhzoB5w5W2B"
                            "cf6o35dX--SYF2vOvLw&dib_tag=se&keywords=babycar+seat+with+newborn&qid=1777507266&sbo=RZvfv%"
                            "2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=8-26-spons&xpid=cw32Tl9prHW7K&sp_csd=d2lkZ2V0TmFtZT1zcF9waG"
                            "9uZV9zZWFyY2hfbXRm&psc=1")
response.raise_for_status()
html_data = BeautifulSoup(response.text, "html.parser")

price_dollars = html_data.find(name="span", class_="a-price-whole")
price_cents = html_data.find(name="span", class_="a-price-fraction")
current_price = f"{price_dollars.text}{price_cents.text}"

if float(current_price) < 240.00:
    connection = smtplib.SMTP(os.getenv("SMTPHOST"), 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                        msg=f"Subject: CAR SEAT PRICE ALERT\n\nThe price for the car seat is low right now\n"
                            "\nhttps://www.amazon.com/Chicco-ClearTex®-Rear-Facing-Compatible-Strollers/dp/B0DTLRY7RP/ref="
                            "mp_s_a_1_26_sspa?dib=eyJ2IjoiMSJ9.oXvA3AXCU6r-dKSNAICcGP-1mCSbyBSH9WJoSl_96j91lyFHlomugwkkl"
                            "zR-t1SsGeyY2J2YzT0uric6RNlNiPL7D4Ed5Yb9hKx1r_lIVl82ATsREFOLSXG2Dg2kOOTZ9zBvXEQMcl8KDESnSDcd"
                            "teuyRL5Bz7adyRFS4RwwsJBVq1AQmvCDpc9jhxYpSCocWBNKDWzolkEKs9iQ66DIeQ.h7SXA5vUX7_1pxhzoB5w5W2B"
                            "cf6o35dX--SYF2vOvLw&dib_tag=se&keywords=babycar+seat+with+newborn&qid=1777507266&sbo=RZvfv%"
                            "2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=8-26-spons&xpid=cw32Tl9prHW7K&sp_csd=d2lkZ2V0TmFtZT1zcF9waG"
                            "9uZV9zZWFyY2hfbXRm&psc=1\n\nThis message was automatically"
                            "sent from my Python program.")
    connection.close()

