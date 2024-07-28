#!/usr/bin/env python3
import math
import argparse

# Threshold for determining if a point is near a POI, approx 100 meters
THRESHOLD_DISTANCE = 0.1  # about 100 meters in decimal degrees

def read_tracking_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    # Parse the first line for POIs, the rest for tracking data
    pois = [tuple(map(float, loc.strip('[] \n').split(','))) for loc in data[0].strip().strip('[]').split('], [')]
    tracking = [tuple(map(float, line.strip('[]\n').split(','))) for line in data[1:]]
    return pois, tracking

def calculate_distance(lat1, lon1, lat2, lon2):
    """ Calculate the distance between two coordinates. """
    R = 6371  # Radius of the Earth in km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def find_pois_with_long_stays(tracking, pois, duration_threshold=15):
    """ Find POIs where the duration of stay is more than the threshold in minutes. """
    long_stays = []
    if not tracking:
        return long_stays

    current_location = tracking[0]
    current_duration = 1  # Start with the first minute

    for i in range(1, len(tracking)):
        distance = calculate_distance(current_location[0], current_location[1], tracking[i][0], tracking[i][1])
        if distance < THRESHOLD_DISTANCE:
            current_duration += 1
        else:
            if current_duration > duration_threshold:
                # Check if current_location is near any POI
                for poi in pois:
                    if calculate_distance(current_location[0], current_location[1], poi[0], poi[1]) < THRESHOLD_DISTANCE:
                        long_stays.append(poi)
                        break
            current_location = tracking[i]
            current_duration = 1

    # Check the last collected location
    if current_duration > duration_threshold:
        for poi in pois:
            if calculate_distance(current_location[0], current_location[1], poi[0], poi[1]) < THRESHOLD_DISTANCE:
                long_stays.append(poi)
                break

    return long_stays

def main():
    parser = argparse.ArgumentParser(description='Find POIs with long stays from tracking data.')
    parser.add_argument('input_file', type=str, help='Filename for input tracking data')
    parser.add_argument('output_file', type=str, help='Filename for output results')
    args = parser.parse_args()
    
    pois, tracking = read_tracking_data(args.input_file)
    long_stays = find_pois_with_long_stays(tracking, pois)
    
    with open(args.output_file, 'w') as out_file:
        for poi in long_stays:
            out_file.write(f"[{poi[0]:.6f}, {poi[1]:.6f}]\n")

if __name__ == "__main__":
    main()

