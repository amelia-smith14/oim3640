from flask import Flask, render_template, request, jsonify
import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

app = Flask(__name__, template_folder='../templates')

geocoder = Nominatim(user_agent='nyc_bathroom_finder')

@app.route('/')
def home():
    return render_template('index.html')

def get_osm_restrooms(lat, lng, radius=5000):
    """
    Query Overpass API for public restrooms near coordinates.
    Radius in meters (default 5km)
    """
    overpass_url = "https://overpass-api.de/api/interpreter"
    
    # Overpass query for toilets and restrooms
    overpass_query = f"""
    [out:json];
    (
      node["amenity"="toilets"](around:{radius},{lat},{lng});
      way["amenity"="toilets"](around:{radius},{lat},{lng});
      relation["amenity"="toilets"](around:{radius},{lat},{lng});
      node["amenity"="restroom"](around:{radius},{lat},{lng});
      way["amenity"="restroom"](around:{radius},{lat},{lng});
    );
    out center;
    """
    
    try:
        response = requests.get(overpass_url, params={'data': overpass_query}, timeout=15)
        data = response.json()
        
        restrooms = []
        for element in data.get('elements', []):
            # Get coordinates
            if 'lat' in element and 'lon' in element:
                restrooms.append({
                    'lat': element['lat'],
                    'lng': element['lon'],
                    'name': element.get('tags', {}).get('name', 'Public Restroom'),
                    'address': element.get('tags', {}).get('addr:full', 'Address not available'),
                })
            elif 'center' in element:
                restrooms.append({
                    'lat': element['center']['lat'],
                    'lng': element['center']['lon'],
                    'name': element.get('tags', {}).get('name', 'Public Restroom'),
                    'address': element.get('tags', {}).get('addr:full', 'Address not available'),
                })
        
        return restrooms
    except Exception as e:
        print(f"Overpass API error: {e}")
        return []

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

        # Get restrooms from OpenStreetMap
        restrooms = get_osm_restrooms(location.latitude, location.longitude, radius=5000)

        if not restrooms:
            return jsonify({'error': 'No public restrooms found in this area. Try a different location.'})

        closest = None
        min_distance = float('inf')

        for restroom in restrooms:
            restroom_location = (restroom['lat'], restroom['lng'])
            distance = geodesic(user_location, restroom_location).miles
            if distance < min_distance:
                min_distance = distance
                closest = restroom

        if closest:
            result = {
                'name': closest['name'],
                'address': closest['address'],
                'distance': round(min_distance, 2),
                'search_location': location.address,
            }
        else:
            result = {'error': 'No restrooms found'}

    except Exception as e:
        result = {'error': f'Error: {str(e)}'[:100]}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
