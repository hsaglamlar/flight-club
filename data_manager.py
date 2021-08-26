import requests

AUTH_SHEETY = "**********"  #use your own authirazation for sheety
ENDPOINT_SHEETY = "********"#use your own endpoint for sheety


class DataManager:
    '''This class is responsible for talking to the Google Sheet using sheety api.'''

    def __init__(self):
        self.destination_data = {}
        self.header = {"Authorization": AUTH_SHEETY}

    def get_destination_data(self):
        response = requests.get(url=ENDPOINT_SHEETY, headers=self.header)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_row(self, row):
        endpoint = ENDPOINT_SHEETY + "/" + str(row["id"])
        data = {"price": row}
        response = requests.put(url=endpoint, json=data, headers=self.header)
        response.raise_for_status()
        return response.status_code == requests.status_codes.codes.ok
