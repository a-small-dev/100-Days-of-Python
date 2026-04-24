import data_manager, flight_search, flight_data

def get_codes(loc_data):
    codes = []
    flight_price = {}
    for location in loc_data:
        codes.append(location['iatacode'])
        flight_price[location['iatacode']] = location['price']
    return ",".join(codes), codes, flight_price

flight_info = data_manager.DataManager()
location_data = flight_info.get_location_data()
location_codes, code_list, price_list = get_codes(location_data)
flight_manager = flight_search.FlightSearch(flight_list=location_codes)
search_info = flight_manager.check_prices()
search_results = flight_data.FlightData(data=search_info, codes=code_list, location_data=price_list)
