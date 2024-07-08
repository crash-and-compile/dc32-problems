#!/usr/bin/env python3
import random
import math

# Constants
MIN_STOP_TIME = 16    # Minimum stop time in minutes
MAX_STOP_TIME = 200   # Maximum stop time in minutes
MIN_TRAVEL_TIME = 10  # Minimum travel time in minutes
MAX_TRAVEL_TIME = 200 # Maximum travel time in minutes
MIN_CYCLES = 50       # Minimum number of cycles
MAX_CYCLES = 100       # Maximum number of cycles
FAKE_LOITER_TIME = 5  # Time spent in fake loitering
FAKE_LOITER_COUNT = 3 # Number of fake loitering instances
SPEED = 50 / 60       # Speed in km/min (50 km/h)
RADIUS = 402.336      # 250 miles in km
NUM_POI = 100         # Number of points of interest
MIN_DISTANCE_BETWEEN_POI = 0.5  # Minimum distance between POIs in km
MAX_JITTER_DISTANCE = 0.01      # Maximum jitter distance in km (approximately 10 meters)

def generate_initial_coordinates():
    """ Generate a random initial coordinate within the continental United States. """
    lat = random.uniform(25, 49)
    lon = random.uniform(-125, -67)
    return lat, lon

def generate_points_of_interest(lat, lon, num_points):
    """ Generate a list of random points within a specified radius of a given coordinate, ensuring minimum distance between them. """
    points = []
    while len(points) < num_points:
        valid = False
        while not valid:
            bearing = random.uniform(0, 360)
            distance = random.uniform(0, RADIUS)
            new_point = move_coordinate(lat, lon, bearing, distance)
            if all(math.dist(new_point, existing_point) >= MIN_DISTANCE_BETWEEN_POI for existing_point in points):
                points.append(new_point)
                valid = True
    return points

def move_coordinate(lat, lon, bearing, distance_km):
    R = 6371  # Earth's radius in km
    bearing = math.radians(bearing)  # Convert bearing to radians
    lat1 = math.radians(lat)
    lon1 = math.radians(lon)
    lat2 = math.asin(math.sin(lat1) * math.cos(distance_km / R) + math.cos(lat1) * math.sin(distance_km / R) * math.cos(bearing))
    lon2 = lon1 + math.atan2(math.sin(bearing) * math.sin(distance_km / R) * math.cos(lat1), math.cos(distance_km / R) - math.sin(lat1) * math.sin(lat2))
    return [math.degrees(lat2), math.degrees(lon2)]

def calculate_bearing(start_lat, start_lon, end_lat, end_lon):
    """ Calculate the bearing from one coordinate to another. """
    start_lat, start_lon, end_lat, end_lon = map(math.radians, [start_lat, start_lon, end_lat, end_lon])
    d_lon = end_lon - start_lon
    x = math.sin(d_lon) * math.cos(end_lat)
    y = math.cos(start_lat) * math.sin(end_lat) - math.sin(start_lat) * math.cos(end_lat) * math.cos(d_lon)
    initial_bearing = math.atan2(x, y)
    return math.degrees(initial_bearing)

def simulate_tracking():
    initial_lat, initial_lon = generate_initial_coordinates()
    points_of_interest = generate_points_of_interest(initial_lat, initial_lon, NUM_POI)
    cycles = random.randint(MIN_CYCLES, MAX_CYCLES)

    with open("problem.txt", "w") as track_file, open("solution.txt", "w") as sol_file:
        # Write POIs as the first line in the tracking file
        track_file.write("[" + ", ".join(f"[{lat:.6f},{lon:.6f}]" for lat, lon in points_of_interest) + "]\n")

        current_lat, current_lon = initial_lat, initial_lon
        for _ in range(cycles + FAKE_LOITER_COUNT):
            # Select whether to perform a fake loiter or visit a POI
            if random.random() < (FAKE_LOITER_COUNT / (cycles + FAKE_LOITER_COUNT)):
                # Perform a fake loiter near a random POI without recording it as a true visit
                target_lat, target_lon = random.choice(points_of_interest)
                # Fuzz the location slightly off the POI
                bearing = random.uniform(0, 360)
                distance = random.uniform(0, MAX_JITTER_DISTANCE)
                target_lat, target_lon = move_coordinate(target_lat, target_lon, bearing, distance)
                fake_loiter_time = FAKE_LOITER_TIME
                for minute in range(fake_loiter_time):
                    bearing = random.uniform(0, 360)
                    distance = random.uniform(0, MAX_JITTER_DISTANCE)
                    target_lat, target_lon = move_coordinate(target_lat, target_lon, bearing, distance)
                    track_file.write(f"[{target_lat:.6f}, {target_lon:.6f}]\n")
            else:
                # Regular POI visit
                target_lat, target_lon = random.choice(points_of_interest)
                sol_file.write(f"[{target_lat:.6f}, {target_lon:.6f}]\n")

                # Travel to a fuzzed location near the POI
                bearing = random.uniform(0, 360)
                distance = random.uniform(0, MAX_JITTER_DISTANCE)
                target_lat, target_lon = move_coordinate(target_lat, target_lon, bearing, distance)
                travel_time = random.randint(MIN_TRAVEL_TIME, MAX_TRAVEL_TIME)
                for minute in range(travel_time):
                    bearing = calculate_bearing(current_lat, current_lon, target_lat, target_lon)
                    current_lat, current_lon = move_coordinate(current_lat, current_lon, bearing, SPEED)
                    track_file.write(f"[{current_lat:.6f}, {current_lon:.6f}]\n")

                # Stop at the fuzzed point near the POI with small movements
                original_lat, original_lon = target_lat, target_lon
                for minute in range(MAX_STOP_TIME):
                    bearing = random.uniform(0, 360)
                    distance = random.uniform(0, MAX_JITTER_DISTANCE)
                    current_lat, current_lon = move_coordinate(original_lat, original_lon, bearing, distance)
                    track_file.write(f"[{current_lat:.6f}, {current_lon:.6f}]\n")

                # Update current location for the next cycle
                current_lat, current_lon = target_lat, target_lon

if __name__ == "__main__":
    simulate_tracking()

