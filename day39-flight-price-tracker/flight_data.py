from notification_manager import NotificationManager

class FlightData(NotificationManager):
    def __init__(self, data, codes, location_data):
        super().__init__()
        self.codes = codes
        self.loc_data = location_data
        self.sort_data(data)

    def sort_data(self, data):
        for flight_group in data['other_flights']:
            price = flight_group['price']
            flights = flight_group['flights']
            for flight in flights:
                if flight['arrival_airport']['id'] in self.codes:
                     if self.loc_data[flight['arrival_airport']['id']] > price:
                         location = flight['arrival_airport']['name']
                         code = flight['arrival_airport']['id']
                         time = flight['arrival_airport']['time']
                         self.send_alert(location=location, code=code, time=time, price=price)