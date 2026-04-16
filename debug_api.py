import requests

url = 'https://data.cityofnewyork.us/api/views/xi7c-iiu2/rows.json?accessType=DOWNLOAD'
response = requests.get(url, timeout=10)
data = response.json()

print('Meta view columns:')
for col in data['meta']['view']['columns']:
    print(f"{col['fieldName']}: position {col['position']}")

print('\nSample record (first 15 elements):')
print(data['data'][0][:15])

print('\nSample record (all elements):')
print(data['data'][0])

# Check if there are coordinates
print('\nChecking for coordinates in first few records:')
for i, record in enumerate(data['data'][:5]):
    print(f'Record {i}:')
    for j, val in enumerate(record):
        if isinstance(val, str) and ('40.' in val or '-7' in val):
            print(f'  Position {j}: {val}')