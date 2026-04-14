from flask import Flask, render_template, request, jsonify
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

app = Flask(__name__, template_folder='../templates')

geocoder = Nominatim(user_agent='nyc_bathroom_finder')

# Popular NYC public restrooms with reliable coordinates
NYC_TOILETS = [
    {'name': 'Bryant Park', 'address': '40 West 42nd Street', 'borough': 'Manhattan', 'lat': 40.7537509, 'lng': -73.9835428},
    {'name': 'Madison Square Park', 'address': 'Madison Ave at 23rd St', 'borough': 'Manhattan', 'lat': 40.7452, 'lng': -73.9868},
    {'name': 'Battery Park', 'address': 'Battery Place', 'borough': 'Manhattan', 'lat': 40.7033, 'lng': -74.0170},
    {'name': 'Central Park Restroom', 'address': 'Central Park (Multiple Locations)', 'borough': 'Manhattan', 'lat': 40.7829, 'lng': -73.9654},
    {'name': 'Washington Square Park', 'address': 'Washington Square', 'borough': 'Manhattan', 'lat': 40.7314, 'lng': -73.9988},
    {'name': 'Tompkins Square Park', 'address': 'East 10th Street', 'borough': 'Manhattan', 'lat': 40.7764, 'lng': -73.9769},
    {'name': 'Union Square Park', 'address': '14th Street & Broadway', 'borough': 'Manhattan', 'lat': 40.7357, 'lng': -73.9911},
    {'name': 'Times Square Duffy Square', 'address': '46th Street at Broadway', 'borough': 'Manhattan', 'lat': 40.7575, 'lng': -73.9855},
    {'name': 'Riverside Park', 'address': 'West 96th Street', 'borough': 'Manhattan', 'lat': 40.7976, 'lng': -73.9777},
    {'name': 'Prospect Park', 'address': 'BrooklynEntrances', 'borough': 'Brooklyn', 'lat': 40.6602, 'lng': -73.9776},
    {'name': 'Astoria Park', 'address': 'Ditmars Boulevard', 'borough': 'Queens', 'lat': 40.7619, 'lng': -73.9261},
    {'name': 'Flushing Meadows Corona Park', 'address': 'queens Boulevard', 'borough': 'Queens', 'lat': 40.7282, 'lng': -73.8385},
    {'name': 'Pelham Bay Park', 'address': 'Orchard Beach', 'borough': 'Bronx', 'lat': 40.8513, 'lng': -73.8324},
    {'name': 'New York Public Library (Main)', 'address': '476 5th Avenue', 'borough': 'Manhattan', 'lat': 40.7532, 'lng': -73.9822},
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

        user_location = (location.latitude, location.longitude)

        closest = None
        min_distance = float('inf')

        for toilet in NYC_TOILETS:
            toilet_location = (toilet['lat'], toilet['lng'])
            distance = geodesic(user_location, toilet_location).miles
            if distance < min_distance:
                min_distance = distance
                closest = toilet

        if closest:
            result = {
                'name': closest['name'],
                'address': closest['address'],
                'borough': closest['borough'],
                'distance': round(min_distance, 2),
                'search_location': location.address,
            }
        else:
            result = {'error': 'No toilets found'}

    except Exception as e:
        result = {'error': str(e)}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
