from flask import Flask, render_template, request, jsonify
import requests
from geopy.distance import geodesic

app = Flask(__name__, template_folder='../templates')

API_URL = "https://data.cityofnewyork.us/resource/xi7c-iiu2.json?$limit=2000"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find_closest', methods=['POST'])
def find_closest():
    data = request.get_json()
    user_lat = data['lat']
    user_lng = data['lng']
    user_location = (user_lat, user_lng)

    try:
        response = requests.get(API_URL)
        toilets = response.json()

        closest = None
        min_distance = float('inf')

        for toilet in toilets:
            if 'location' in toilet and 'latitude' in toilet['location'] and 'longitude' in toilet['location']:
                lat = float(toilet['location']['latitude'])
                lng = float(toilet['location']['longitude'])
                toilet_location = (lat, lng)
                distance = geodesic(user_location, toilet_location).miles
                if distance < min_distance:
                    min_distance = distance
                    closest = toilet

        if closest:
            result = {
                'name': closest.get('name', 'Unknown'),
                'address': closest.get('address', 'Unknown'),
                'borough': closest.get('borough', 'Unknown'),
                'distance': round(min_distance, 2)
            }
        else:
            result = {'error': 'No toilets found'}

    except Exception as e:
        result = {'error': str(e)}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
