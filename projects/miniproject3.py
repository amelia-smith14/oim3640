from flask import Flask, render_template, request, jsonify
import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

app = Flask(__name__, template_folder='../templates')

geocoder = Nominatim(user_agent='nyc_bathroom_finder')
API_URL = "https://data.cityofnewyork.us/resource/xi7c-iiu2.json?$limit=5000"

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

        response = requests.get(API_URL, timeout=15)
        toilets = response.json()

        closest = None
        min_distance = float('inf')

        for toilet in toilets:
            # Try different coordinate field formats
            lat = lng = None

            # Check for location object with lat/lng
            if 'location' in toilet and isinstance(toilet['location'], dict):
                if 'latitude' in toilet['location'] and 'longitude' in toilet['location']:
                    lat = float(toilet['location']['latitude'])
                    lng = float(toilet['location']['longitude'])
                elif 'coordinates' in toilet['location'] and isinstance(toilet['location']['coordinates'], list):
                    lng, lat = toilet['location']['coordinates']

            # Check for direct lat/lng fields
            elif 'latitude' in toilet and 'longitude' in toilet:
                lat = float(toilet['latitude'])
                lng = float(toilet['longitude'])

            if lat is not None and lng is not None:
                toilet_location = (lat, lng)
                distance = geodesic(user_location, toilet_location).miles
                if distance < min_distance:
                    min_distance = distance
                    closest = toilet

        if closest:
            result = {
                'name': closest.get('name', 'Public Restroom'),
                'address': closest.get('address', 'Address not available'),
                'borough': closest.get('borough', 'Unknown'),
                'distance': round(min_distance, 2),
                'search_location': location.address,
            }
        else:
            result = {'error': 'No public restrooms found in this area. Try a different location.'}

    except Exception as e:
        result = {'error': f'Error: {str(e)}'[:100]}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
