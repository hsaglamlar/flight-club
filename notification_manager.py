from flight_data import FlightData
from twilio.rest import Client
import smtplib

TWILIO_SID = "************"  #use your own SID
TWILIO_AUTH_TOKEN = "*************" #use your own token
TWILIO_VIRTUAL_NUMBER = "+*******"  #use your own number
TWILIO_VERIFIED_NUMBER = "+*************" #use your own number

MY_EMAIL = "********@gmail.com" #use your own email and password
PASSWORD = "*****"              


class NotificationManager:
    '''This class responsible for sending email or sms to the defined user'''

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.connection = None

    def send_sms(self, flight: FlightData):
        text = "Low price alert! Only " + str(flight.price) + " TL to fly from " + \
               flight.departure_city_name + "-" + flight.departure_airport_code + \
               " to " + flight.arrival_city_name + "-" + flight.departure_airport_code + " from " + \
               flight.outbound_date + " to " + flight.inbound_date
        print(text)

        message = self.client.messages.create(body=text,
                                              from_=TWILIO_VIRTUAL_NUMBER,
                                              to=TWILIO_VERIFIED_NUMBER
                                              )
        print(message.status)

    def send_email(self, flight: FlightData, emails):
        text = "Low price alert! Only " + str(flight.price) + " TL to fly from " + \
               flight.departure_city_name + "-" + flight.departure_airport_code + \
               " to " + flight.arrival_city_name + "-" + flight.departure_airport_code + " from " + \
               flight.outbound_date + " to " + flight.inbound_date
        print(text)

        with smtplib.SMTP("smtp.gmail.com:587") as self.connection:
            self.connection.ehlo()
            self.connection.starttls()
            self.connection.login(user=MY_EMAIL, password=PASSWORD)
            for email in emails:
                print(f"sending email to {email}")
                self.connection.sendmail(from_addr=MY_EMAIL,
                                         to_addrs=email,
                                         msg=f"Subject: Flight Allert!...\n\n {text}")
