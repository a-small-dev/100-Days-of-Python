import requests

class DataManager:
    def __init__(self):
        self.SHEET_DATA_API = "GOOGLE SHEET API HERE"

    def get_location_data(self):
        response = requests.get(url=self.SHEET_DATA_API)
        data = response.json()
        locations = []
        for location in data['sheet1']:
            location_data = {"location": location['location'],
                             "iatacode": location['iataCode'],
                             "price": location['price']}
            locations.append(location_data)
        return locations