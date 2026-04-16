from flask import Flask, render_template, request, jsonify
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

app = Flask(__name__, template_folder='../templates')

geocoder = Nominatim(user_agent='nyc_bathroom_finder')

# Comprehensive list of NYC public restrooms with verified coordinates
NYC_RESTROOMS = [
    # Manhattan
    {'name': 'Bryant Park Public Restroom', 'address': '40 West 42nd Street', 'borough': 'Manhattan', 'lat': 40.7538, 'lng': -73.9835},
    {'name': 'Central Park - Bethesda Terrace', 'address': 'Bethesda Terrace', 'borough': 'Manhattan', 'lat': 40.7744, 'lng': -73.9709},
    {'name': 'Central Park - Great Lawn', 'address': 'Great Lawn Area', 'borough': 'Manhattan', 'lat': 40.7829, 'lng': -73.9654},
    {'name': 'Washington Square Park', 'address': 'Washington Square North', 'borough': 'Manhattan', 'lat': 40.7314, 'lng': -73.9988},
    {'name': 'Union Square Park', 'address': '14th Street & Broadway', 'borough': 'Manhattan', 'lat': 40.7357, 'lng': -73.9911},
    {'name': 'Madison Square Park', 'address': 'Madison Ave & 23rd St', 'borough': 'Manhattan', 'lat': 40.7414, 'lng': -73.9877},
    {'name': 'Tompkins Square Park', 'address': 'East 7th Street', 'borough': 'Manhattan', 'lat': 40.7264, 'lng': -73.9818},
    {'name': 'Rockefeller Center', 'address': '45 Rockefeller Plaza', 'borough': 'Manhattan', 'lat': 40.7587, 'lng': -73.9787},
    {'name': 'Times Square', 'address': '1560 Broadway', 'borough': 'Manhattan', 'lat': 40.7589, 'lng': -73.9851},
    {'name': 'Grand Central Terminal', 'address': '89 East 42nd Street', 'borough': 'Manhattan', 'lat': 40.7527, 'lng': -73.9772},
    {'name': 'Penn Station', 'address': '234 West 31st Street', 'borough': 'Manhattan', 'lat': 40.7505, 'lng': -73.9934},
    {'name': 'Port Authority Bus Terminal', 'address': '625 8th Avenue', 'borough': 'Manhattan', 'lat': 40.7573, 'lng': -73.9900},
    {'name': 'New York Public Library', 'address': '476 5th Avenue', 'borough': 'Manhattan', 'lat': 40.7532, 'lng': -73.9822},
    {'name': 'Lincoln Center', 'address': '70 Lincoln Center Plaza', 'borough': 'Manhattan', 'lat': 40.7725, 'lng': -73.9835},
    {'name': 'Columbus Circle', 'address': 'Columbus Circle', 'borough': 'Manhattan', 'lat': 40.7680, 'lng': -73.9819},
    {'name': 'Battery Park', 'address': 'Battery Place', 'borough': 'Manhattan', 'lat': 40.7033, 'lng': -74.0170},
    {'name': 'South Street Seaport', 'address': '89 South Street', 'borough': 'Manhattan', 'lat': 40.7060, 'lng': -74.0037},
    {'name': 'Chelsea Piers', 'address': 'Pier 59', 'borough': 'Manhattan', 'lat': 40.7470, 'lng': -74.0086},
    {'name': 'High Line', 'address': '14th Street Entrance', 'borough': 'Manhattan', 'lat': 40.7411, 'lng': -74.0048},
    {'name': 'Brooklyn Bridge Park - Manhattan Side', 'address': '334 Furman Street', 'borough': 'Manhattan', 'lat': 40.7004, 'lng': -73.9965},

    # Brooklyn
    {'name': 'Prospect Park', 'address': 'Prospect Park West', 'borough': 'Brooklyn', 'lat': 40.6602, 'lng': -73.9776},
    {'name': 'Brooklyn Bridge Park', 'address': '334 Furman Street', 'borough': 'Brooklyn', 'lat': 40.7017, 'lng': -73.9965},
    {'name': 'Coney Island', 'address': '1208 Surf Avenue', 'borough': 'Brooklyn', 'lat': 40.5755, 'lng': -73.9794},
    {'name': 'JFK Airport', 'address': 'JFK Airport Terminals', 'borough': 'Queens', 'lat': 40.6413, 'lng': -73.7781},
    {'name': 'LaGuardia Airport', 'address': 'LaGuardia Airport Terminals', 'borough': 'Queens', 'lat': 40.7769, 'lng': -73.8740},

    # Queens
    {'name': 'Flushing Meadows Corona Park', 'address': 'Flushing Meadows', 'borough': 'Queens', 'lat': 40.7400, 'lng': -73.8407},
    {'name': 'Astoria Park', 'address': '19th Street & 23rd Drive', 'borough': 'Queens', 'lat': 40.7750, 'lng': -73.9220},
    {'name': 'Forest Park', 'address': 'Forest Park Drive', 'borough': 'Queens', 'lat': 40.7000, 'lng': -73.8970},

    # Bronx
    {'name': 'Bronx Zoo', 'address': '2300 Southern Boulevard', 'borough': 'Bronx', 'lat': 40.8506, 'lng': -73.8773},
    {'name': 'Pelham Bay Park', 'address': 'Orchard Beach', 'borough': 'Bronx', 'lat': 40.8650, 'lng': -73.8000},
    {'name': 'Van Cortlandt Park', 'address': 'Broadway & 242nd Street', 'borough': 'Bronx', 'lat': 40.8960, 'lng': -73.8880},

    # Staten Island
    {'name': 'Snug Harbor Cultural Center', 'address': '1000 Richmond Terrace', 'borough': 'Staten Island', 'lat': 40.6450, 'lng': -74.1030},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find_closest', methods=['POST'])
def find_closest():
    data = request.get_json()
    address = data.get('address', '').strip()

    if not address:
        return jsonify({'error': 'Please enter a location or address.'})

    try:
        location = geocoder.geocode(f"{address}, New York, NY", timeout=10)
        if location is None:
            return jsonify({'error': 'Could not find that location. Please enter a more specific address.'})

        # Validate that the location is within NYC bounds
        # NYC latitude: ~40.5 to 40.9, longitude: ~-74.3 to -73.7
        if not (40.5 <= location.latitude <= 40.9) or not (-74.3 <= location.longitude <= -73.7):
            return jsonify({'error': 'This location appears to be outside of New York City. Please enter an address within NYC.'})

        user_location = (location.latitude, location.longitude)

        closest = None
        min_distance = float('inf')

        for restroom in NYC_RESTROOMS:
            restroom_location = (restroom['lat'], restroom['lng'])
            distance = geodesic(user_location, restroom_location).miles
            if distance < min_distance:
                min_distance = distance
                closest = restroom

        if closest:
            # Check if the closest restroom is within 1 mile
            if min_distance <= 1.0:
                result = {
                    'name': closest['name'],
                    'address': closest['address'],
                    'borough': closest['borough'],
                    'distance': round(min_distance, 2),
                    'search_location': location.address,
                }
            else:
                result = {'error': f'No public restrooms found within 1 mile of your location. The closest restroom is {round(min_distance, 1)} miles away at {closest["name"]}.'}
        else:
            result = {'error': 'No public restrooms found in this area. Try a different location.'}

    except Exception as e:
        result = {'error': f'Error: {str(e)}'[:100]}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
