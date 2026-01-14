import requests

URL = 'http://ip-api.com/json/'
FIELDS = 'lat,lon'
API_URI = 'http://service-b-api:8000'

def get_ip_coordinates(ip):
    response = requests.get(f'{URL}{ip.ip}?fields={FIELDS}')
    return {'ip': str(ip),
        'coordinates': response.text
    }
    
def post_to_db(data):
    requests.post(f'{API_URI}/coordinates', json=data)
    
def get_items():
    response = requests.get(f'{API_URI}/coordinates')
    response.raise_for_status()
    return response.json()
    
    