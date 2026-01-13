import requests

URL = 'http://ip-api.com/json/'
FIELDS = 'lat,lon'
API_URI = 'http://redis-api:8080'

def get_ip_coordinates(ip):
    response = requests.get(f'{URL}{ip.ip}?fields={FIELDS}')
    return {'ip': ip.ip,
        'coordinates': response.text
    }
    
def post_to_db(data):
    requests.post(f'{API_URI}/coordinates', json=data)
    
def get_items():
    response = requests.get(f'{API_URI}/coordinates')
    return response
    