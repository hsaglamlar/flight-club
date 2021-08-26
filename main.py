# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

import data_manager
from flight_data import FlightData
from notification_manager import NotificationManager
from flight_search import FlightSearch
import pprint

#instance for sending email or sms to the user when cheap flight allert occurs
notify = NotificationManager()

# get cities to fly from google sheets
cities_fprice_data = data_manager.DataManager()
destination_data = cities_fprice_data.get_destination_data()

# search for all flights
for dest in destination_data:
    flights = FlightSearch()
    
    #if city code not assigned or blank, get the code and save it
    if "iataCode" not in dest:
        dest["iataCode"] = flights.get_location_name(dest["city"])
        cities_fprice_data.update_row(dest)
    elif dest["iataCode"] == "":
        dest["iataCode"] = flights.get_location_name(dest["city"])
        cities_fprice_data.update_row(dest)

    # get the price for current destination
    cheapest_current_flight = FlightData(flights.get_flight_data(dest["iataCode"]))

    if not hasattr(cheapest_current_flight, "price"):
        cheapest_current_flight = FlightData(flights.get_flight_data(dest["iataCode"], stop_overs=1))
        if not hasattr(cheapest_current_flight, "price"):
            continue
        else:
            print(f"To {dest['iataCode']}, we found flights with 1 stop.")

    #if the price is cheaper than previous price then notify the user with email or sms
    if cheapest_current_flight.price < dest["lowestPrice"]:
        dest["lowestPrice"] = cheapest_current_flight.price
        cities_fprice_data.update_row(dest)

        notify.send_email(cheapest_current_flight,["hsaglamlar@yahoo.com", "hsaglamlar@yahoo.com"])
