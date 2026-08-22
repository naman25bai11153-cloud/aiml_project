import requests

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
