from fastapi import APIRouter
from schemas import IP
from services import get_ip_coordinates, post_to_db, get_items

router = APIRouter()

@router.get('/')
def healthy():
    return {
        'message': 'ok'
    }

# @router.post('/')
# def send_ip(ip: IP):
#     response = get_ip_coordinates(ip)
#     return {"mess": response}

@router.post('/ip')
def send_coordinates(ip: IP):
    coordinates = get_ip_coordinates(ip)
    print(coordinates)
    print(coordinates['ip'])
    post_to_db(coordinates)
    return {
        'data': coordinates
    }
    
@router.get('/coordinates')
def display_all_coordinates():
    print(get_items, type(get_items))
    items = get_items()
    print(items, type(items))
    return items