import requests
from pprint import pprint
import os
from dotenv import load_dotenv
from openai import OpenAI

#response = requests.get('https://oim.108122.xyz/words/random')
#print(response.json())

response = requests.get("https://oim.108122.xyz/mass", 
                        headers={"X-Token": "ameliaamelia"},
)
data = response.json()

print(data['name'])
print(data['governor'])

for town in data['data'][:5]:
    print(f"{town['name']}: pop {town['population']:,}")

requests.post('https://oim.108122.xyz/message',
                headers={"X-Token": "ameliaamelia"},
                json={"message": "Hello from Amelia!"}
)



load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')
url = f"http://api.openweathermap.org/data/2.5/weather?q=Saint%20Pete%20Beach&appid={API_KEY}&units=imperial"

print(url)
data = requests.get(url).json()
print(f"Current temperature in Saint Pete Beach: {data['main']['temp']}°F, {data['weather'][0]['description']}")


client=OpenAI()
response = client.responses.create(
    model="gpt-5-nano", input= "Write a haiku about the weather in Saint Pete Beach.")
print(response.output_text)