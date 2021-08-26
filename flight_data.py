class FlightData:
    '''Class object for flight data'''

    def __init__(self, flight_dict):
        if flight_dict is not None:
            self.price = flight_dict[0]["price"]
            self.departure_airport_code = flight_dict[0]["flyFrom"]
            self.departure_city_name = flight_dict[0]["cityFrom"]
            self.arrival_airport_code = flight_dict[0]["flyTo"]
            self.arrival_city_name = flight_dict[0]["cityTo"]
            self.stop_over = 2
            self.via_city = flight_dict[0]["route"][0]["cityTo"]
            self.outbound_date = flight_dict[0]["local_departure"].split("T")[0]
            self.inbound_date = flight_dict[1]["local_departure"].split("T")[0]
        else:
            self = None

