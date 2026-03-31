import requests
from geopy.geocoders import Nominatim
aaa = Nominatim(user_agent="emergency hospital route finder using bfs")
# finding coordinates of your location
def hsl():
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
#now we will find nearby hospitals
def hospital_loc(lat,lon):
    print("finding hospitals nearby..")
    #now we will use OSM api to find nearby hospitals near you. OSM is detailed map that provides accurate coordinates
    url = "https://overpass.kumi.systems/api/interpreter"
    query = (f'[out:json];'
             f'node["amenity"="hospital"](around:5000,{lat},{lon});'
             f'out body;')
    headers = {'User-Agent': 'Emergency_route_finder/1.0'}
    try:
        response = requests.post(url, data={'data': query}, headers=headers)

        if response.status_code != 200:
            print(f"Server returned an error: {response.status_code}")
            return []
        d= response.json()
        hos = []

        for item in d.get('elements', []):
            name = item.get('tags', {}).get('name', 'General Hospital')
            hos.append({'name': name,
                'lat': item['lat'],
                'lon': item['lon']})

        if hos:
            print("nearby hospitals are :")
            for h in hos[:10]:
                print(f"> {h['name']} : Lat: {h['lat']}, Lon: {h['lon']}")
            return hos #returns the list of hospitals


        else:
            print("No hospitals found in a 5km radius.")

    except Exception as e:
        print(f"Server Error: {e}")
        return []


def hkv(clat, clon, hlat, hlon):
    # OSRM Public API URL to find the road distance between current location and nearby hospitals.
    # OSRM calculates the disntances from one coordinate to onther on a map

    url = f"http://router.project-osrm.org/route/v1/driving/{clon},{clat};{hlon},{hlat}?overview=false"

    try:
        # adding a small timeout so the program doesn't hang if the server is slow
        response = requests.get(url, timeout=5)
        data = response.json()

        if data['code'] == 'Ok':
            dis = data['routes'][0]['distance']
            # converting distance from meters to killometers
            dis = dis/1000
            dis = round(dis, 2)
            return dis
    except Exception:
        return None
    return None
def main():
    c = hsl() #getting your cordinates
    if c:
        lat, lon, city = c
#        hospital_loc(lat, lon)
        nh = hospital_loc(lat, lon) #list of hospitals
        nd ={}
        print("calculating distances from your location to the nearby hospitals")
        for h in nh[:5]:  # Use first only 5 hospitals to save time
            h_name = h['name']
            hlon = h['lon']
            hlat = h['lat']
            clat = lat
            clon = lon
            # Call your OSRM function to calulate road distanc
            d = hkv(clat, clon, hlat, hlon)

            if d is not None:
                nd[h_name] = d
                print(f"Distance to {h_name}: {d} km")

        # Move these lines inside an 'if' check
        if nd:
            nhp = nd.values()
            g = min(nhp)

            # To shw the hospital NAME (the key) as well as the distance:
            best_hospital = min(nd, key=nd.get)
            print(f" The nearest hospital is {best_hospital} at {g} km.")
        else:
            print("Could not find any road distances. Please check the server or your internet.")




if __name__ == "__main__":
    main()



