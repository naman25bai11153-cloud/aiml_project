import requests
from first_aid import aid

def hospital_loc(lat, lon):
    sr = [5000, 15000]
    headers = {"User-Agent": "EmergencyHospitalRouteFinder/1.0"}

    endpoints = [
        "https://overpass-api.de/api/interpreter",
        "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
        "https://overpass.private.coffee/api/interpreter",
    ]

    server_connected = False

    for i in sr:
        km = i // 1000
        print(f"Finding emergency hospitals within {km} km...")

        query = f"""
            [out:json][timeout:10];
            (
              node["amenity"="hospital"]["emergency"="yes"](around:{i},{lat},{lon});
              way["amenity"="hospital"]["emergency"="yes"](around:{i},{lat},{lon});
              node["healthcare"="hospital"]["emergency"="yes"](around:{i},{lat},{lon});
              way["healthcare"="hospital"]["emergency"="yes"](around:{i},{lat},{lon});
            );
            out center;
        """

        for url in endpoints:
            try:
                response = requests.post(
                    url, data={"data": query}, headers=headers, timeout=10
                )
                if response.status_code == 200:
                    server_connected = True
                    d = response.json()
                    hos = []

                    for item in d.get("elements", []):
                        name = item.get("tags", {}).get(
                            "name", "Emergency Hospital / Trauma Center"
                        )
                        h_lat = item.get("lat") or item.get("center", {}).get(
                            "lat"
                        )
                        h_lon = item.get("lon") or item.get("center", {}).get(
                            "lon"
                        )

                        if h_lat and h_lon:
                            hos.append(
                                {"name": name, "lat": h_lat, "lon": h_lon}
                            )

                    if hos:
                        print(
                            f"Found {len(hos)} emergency facility/facilities within {km} km:"
                        )
                        for h in hos[:10]:
                            print(
                                f"> {h['name']} : Lat: {h['lat']}, Lon: {h['lon']}"
                            )
                        return hos

                    # Specific message for 5 km failure before stepping to 15 km
                    if i == 5000:
                        print(
                            "Oh no! No hospital found within 5km radius. "
                            "Extending search radius to 15km radius and trying again. "
                            "Do not panic."
                        )
                    break

            except Exception:
                continue

    if not server_connected:
        print(
            "Server unreachable: All Overpass API mirrors failed to respond."
        )
        print("please tell us patient's symptoms so that we can provide appropriate first aid procedure")
        aid()
    else:
        print(
            "Search completed: No emergency hospital found within 15km radius."
        )
        print("please tell us patient's symptoms so that we can provide appropriate first aid procedure")
        aid()

    return []
