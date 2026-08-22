import requests
from geopy.geocoders import Nominatim
from location_tracker import hsl
from hospital_finder import hospital_loc
from distance_calculator import hkv
# finding coordinates of your location

#now we will find nearby hospitals

def main():
    c = hsl() #getting your coordinates
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



