import requests
import datetime

API_KEY = "***********" #use your own key
API_ENDPOINT = "https://tequila-api.kiwi.com"
FLY_FROM = "IST"


class FlightSearch:
    '''flight search class using tequila api'''
    def __init__(self):
        self.destination_data = {}
        self.header = {"apikey": API_KEY}

    def get_location_name(self, city):
        query = {"term": city}
        response = requests.get(url=API_ENDPOINT + "/locations/query", params=query, headers=self.header)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def get_flight_data(self, arrival_city_code, stop_overs=0):
        dateFrom = datetime.datetime.now().strftime("%d/%m/%Y")
        dateTo = (datetime.datetime.now() + datetime.timedelta(days=6 * 30)).strftime("%d/%m/%Y")
        parameters = {"fly_from": FLY_FROM,
                      "fly_to": arrival_city_code,
                      "dateFrom": dateFrom,
                      "dateTo": dateTo,
                      "nights_in_dst_from": 7,
                      "nights_in_dst_to": 28,
                      "flight_type": "round",
                      "max_stopovers": stop_overs,
                      "curr": "TRY"}

        response = requests.get(url=API_ENDPOINT + "/v2/search", params=parameters, headers=self.header)
        response.raise_for_status()
        self.destination_data = response.json()["data"]
        if self.destination_data:
            print(f"Flights for {arrival_city_code} is taken.")
        else:
            print(f"No flights found for {arrival_city_code}.")
            self.destination_data = None
        return self.destination_data


