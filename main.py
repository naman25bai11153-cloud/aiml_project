import requests
import geopy
import geocoder
from geopy.geocoders import Nominatim
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Emergency_App")
def nearby_hospital():
    city = input("Enter your city: ")
    loc = input("enter your current location: ")
    address = f"{loc}, {city}"
    location = geolocator.geocode(address)
    if location:
        print(f"Coordinates Found: {location.latitude}, {location.longitude}")
        return location.latitude, location.longitude, city
    else:
        print("Could not find that specific area. Try a nearby landmark.")
        return None
#    url = "https://overpass-api.de/api/interpreter"

nearby_hospital()
