import requests,datetime as dt
import dateutil.relativedelta as dutil

class FlightSearch:
    def __init__(self, flight_list):
        self.six_months = dt.datetime.now() + dutil.relativedelta(months=6)
        self.SERP_API = "YOUR API HERE"
        self.FLIGHTS_URL = "https://serpapi.com/search?engine=google_flights"
        self.FLIGHT_LOCATIONS = flight_list
        self.COUNTRY_CODE = "us"
        self.LANGUAGE_CODE = "en"
        self.DEPARTURE_CODE = "YOUR LOCAL AIRPORT CODE HERE"
        self.TYPE_OF_FLIGHT = 2
        self.SORT_TYPE = 2
        self.OUTBOUND_DATE = dt.datetime.now().strftime("%Y-%m-%d")

    def check_prices(self):
        flight_params = {"departure_id": self.DEPARTURE_CODE,
                         "arrival_id": self.FLIGHT_LOCATIONS,
                         "gl": self.COUNTRY_CODE,
                         "hl": self.LANGUAGE_CODE,
                         "type": self.TYPE_OF_FLIGHT,
                         "outbound_date": self.OUTBOUND_DATE,
                         "sort_by": self.SORT_TYPE,
                         "api_key": self.SERP_API}
        response = requests.get(url=self.FLIGHTS_URL, params=flight_params)
        data = response.json()
        return data