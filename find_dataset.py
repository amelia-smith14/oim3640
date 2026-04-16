import requests

# Try searching for restroom datasets
search_url = 'https://data.cityofnewyork.us/api/views.json'
response = requests.get(search_url, timeout=10)
datasets = response.json()

print('Searching for restroom datasets...')
for dataset in datasets[:100]:  # Check first 100
    name = dataset.get('name', '').lower()
    if 'restroom' in name or 'toilet' in name or 'bathroom' in name or 'public' in name:
        print(f"Found: {dataset['name']}")
        print(f"ID: {dataset['id']}")
        print(f"URL: https://data.cityofnewyork.us/resource/{dataset['id']}.json")
        print('---')