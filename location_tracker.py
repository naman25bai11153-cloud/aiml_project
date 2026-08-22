from geopy.geocoders import Nominatim
import geocoder

aaa = Nominatim(user_agent="emergency hospital route finder using bfs")
def hsl():
    print("Detecting exact device location...")
    # Queries the local system / IP router info
    g = geocoder.ip('me')

    if g.ok and g.latlng:
        lat, lon = g.latlng
        city = g.city or "Unknown City"
        print(f"Location detected: {city} ({lat}, {lon})")
        return lat, lon, city
    else:
        print("Failed to get device coordinates.")
        F = input("Do you want to enter location manually: ?")
        F = F.lower()
        if F == "yes":
            c = input("Enter your city name : ")
            a = input("enter your current location as precisely as you can : ")
            add = f"{a}, {c}"
            loc = aaa.geocode(add)
            if loc:
                lat = loc.latitude
                lon = loc.longitude
                return lat, lon, c
            else:
                print("Could not find that area. "
                      "Try a more known landmark/place .")
                return None
