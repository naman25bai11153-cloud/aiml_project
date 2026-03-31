# 🏥 Emergency Hospital Finder

A Python-based application designed to locate the nearest hospitals in real-time based on a user's specific location 📍. This project was developed as a practical implementation for a basic AI/ML course to solve a real-world navigation and resource allocation problem using Search Algorithm principles.

---

## 📋 Overview
In emergency situations, finding the closest medical facility can be life-saving . This tool automates that process by:
1.  **Geocoding** your specific address or landmark into GPS coordinates 🗺️.
2.  **Searching** for all hospitals within a 5km radius using the OpenStreetMap database 🔍.
3.  **Calculating** actual driving distances (not just straight lines) to find the most efficient route 🚗.
4.  **Identifying** the best option based on the shortest road distance 🏆.

---

## 🧠 Core Concepts (AI/ML)
The project utilizes the logic of **Breadth-First Search (BFS)**. In the context of a geographic map:
* The **Root Node** is the user's current location 🏠.
* The **Neighbors** are the hospital nodes found within the 5km search "layer" 🏥.
* The **Goal** is to find the node with the minimum edge weight (driving distance) 🏁.

---

## ✨ Features
* **Real-time Data**: Fetches live hospital locations from the Overpass API 🌐.
* **Accurate Routing**: Uses the OSRM engine to account for actual road networks and one-way streets 🛣️.
* **User-Friendly Input**: Allows users to enter landmarks or specific areas rather than manual GPS coordinates ✍️.

---

## 💻 Technical Requirements
To run this project, you will need:
* **Python 3.x** 🐍
* **Libraries**:
    * `requests`: To handle API calls to OpenStreetMap and OSRM.
    * `geopy`: To handle geocoding and coordinate conversion.

---

## 🚀 Setup and Installation
1.  **Clone the repository or download the source code.**
2.  **Install the required dependencies:**
    `pip install requests geopy`
3.  **Run the application:**
    `python main.py`

---

## 🛠️ How to Use
1.  **Enter City**: When prompted, type your current city (e.g., "Gurugram") 🏙️.
2.  **Enter Location**: Provide a precise landmark or street address (e.g., "Cyber Hub") 📍.
3.  **View Results**: The program will list nearby hospitals and calculate the driving distance to each 📊.
4.  **Optimal Choice**: The script will conclude by stating exactly which hospital is the nearest by road ✅.

---

## 🤝 API Credits
This project leverages the following open-source services:
* **Nominatim (Geopy)**: For location services.
* **Overpass API**: For OpenStreetMap (OSM) data.
* **OSRM**: For road routing and distance calculations.
