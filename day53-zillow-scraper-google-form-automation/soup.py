import requests
from bs4 import BeautifulSoup
class Parser:
    def __init__(self):
        self.zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
        self.zillow_list = {}

    def get_data(self):
        response = requests.get(url=self.zillow_url)
        response.raise_for_status()
        html_data = BeautifulSoup(response.text, "html.parser")
        return html_data

    def parse_data(self, data_to_parse):
        search_container = data_to_parse.find(name="div", class_="result-list-container")
        listings = search_container.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        i = 1
        for listing in listings:
            url = listing.find(name="a", class_="StyledPropertyCardDataArea-anchor")["href"]
            address = listing.find(name="address")
            cost = listing.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
            info_list = listing.find(name="ul", class_="StyledPropertyCardHomeDetailsList")
            info_items = [li.text for li in info_list.find_all(name="li")]
            bedrooms = info_items[0] if len(info_items) > 0 else "Not Listed"
            bathrooms = info_items[1] if len(info_items) > 1 else "Not Listed"
            self.zillow_list[i] = {"url": url,
                                   "address": address.text.strip(),
                                   "cost": cost.text,
                                   "bedrooms": bedrooms,
                                   "bathrooms": bathrooms}
            i += 1
        return self.zillow_list