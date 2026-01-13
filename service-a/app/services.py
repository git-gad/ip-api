import requests

URL = 'http://ip-api.com/json/'
FIELDS = 'lat,lon'

def get_ip_coordinates(ip):
    response = requests.get(f'{URL}{ip}?fields={FIELDS}')
    print(response)
    return response