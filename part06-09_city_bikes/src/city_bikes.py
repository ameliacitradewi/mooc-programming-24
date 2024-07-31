# Write your solution here
import math
def get_station_data(filename: str) -> dict:
    stations = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the header
            parts = line.strip().split(';')
            if len(parts) < 7:
                continue
            name = parts[3]
            longitude = float(parts[0])
            latitude = float(parts[1])
            stations[name] = (longitude, latitude)
    return stations

def distance(stations: dict, station1: str, station2: str) -> float:
    lon1, lat1 = stations[station1]
    lon2, lat2 = stations[station2]
    
    x_km = (lon1 - lon2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km

def greatest_distance(stations: dict) -> tuple:
    max_distance = 0
    station1 = station2 = None
    
    station_names = list(stations.keys())
    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            s1 = station_names[i]
            s2 = station_names[j]
            dist = distance(stations, s1, s2)
            if dist > max_distance:
                max_distance = dist
                station1 = s1
                station2 = s2
    
    return (station1, station2, max_distance)