import googlemaps

from datetime import datetime

from clients.http_client import HttpClient

class GMapsClient:
    """
    We are using google maps python client for using places, maps, and various other 
    APIs that google provides

    Package details: https://github.com/googlemaps/google-maps-services-python
    """

    def __init__(self):
        """
        TODO get a gmaps key from BU spark.
        """
        self.gmaps = googlemaps.Client("AIzaSyCAkhQSXggIqDGTsR7IeSzXBmD9jPlhUlk")
    
    def get_client(self):
        return self.gmaps
    
    def get_place_by_phone_number(self, phone_number):
        """
        Phone numbers must be in international format (prefixed by a plus sign ("+"), 
        followed by the country code, then the phone number itself).

        For more details: https://developers.google.com/places/web-service/search
        """
        if isinstance(phone_number, int):
            phone_number = str(phone_number)
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+phone_number+"&inputtype=phonenumber&fields=photos,formatted_address,name,opening_hours,rating&locationbias=circle:2000@47.6918452,-122.2226413&key=AIzaSyCAkhQSXggIqDGTsR7IeSzXBmD9jPlhUlk"
        return HttpClient(url,None).get()
    
    
client = GMapsClient()

file = "scraper/data/ampInfo.csv"
import csv
with open(file, 'r') as f:
    reader = csv.reader(f)
    addList = list(reader)
    
places = []
for entry in addList:
    if entry[1] != '':
        placeByPhone = client.get_place_by_phone_number(entry[1])
        for candidate in placeByPhone["candidates"]:
            places.append({"Our address" : entry[0],
                           "Goog address" : candidate['formatted_address'],
                           "Goog name" : candidate['name']})

keys = places[0].keys()
with open('scraper/data/ampGoogAddresses.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(places)


