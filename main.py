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
        lat = location.latitude
        lon = location.longitude
        return lat, lon, city
    else:
        print("Could not find that specific area. Try a nearby landmark.")
        return None

def find_hospital(lat,lon):
    url = "https://overpass.kumi.systems/api/interpreter"
    query = f'[out:json];node["amenity"="hospital"](around:5000,{lat},{lon});out body;'
    headers = {'User-Agent': 'EmergencyLocatorProject/1.0'}
    try:
        response = requests.post(url, data={'data': query}, headers=headers)

        if response.status_code != 200:
            print(f"Server returned an error: {response.status_code}")
            return
        data = response.json()
        hospitals = []

        for item in data.get('elements', []):
            name = item.get('tags', {}).get('name', 'General Hospital')
            hospitals.append({
                'name': name,
                'lat': item['lat'],
                'lon': item['lon']
            })

        if hospitals:
            print(f"\nFound {len(hospitals)} hospitals nearby. Top 5:")
            for h in hospitals[:5]:
                print(f"- {h['name']} (Lat: {h['lat']}, Lon: {h['lon']})")
        else:
            print("No hospitals found in a 5km radius.")

    except Exception as e:
        print(f"Error reading server data: {e}")
def main():
    result = nearby_hospital()

    if result:
        lat, lon, city = result
        find_hospital(lat, lon)
if __name__ == "__main__":
   main()
