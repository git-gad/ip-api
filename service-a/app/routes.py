from fastapi import APIRouter
from schemas import IP
from services import get_ip_coordinates, post_to_db, get_items

router = APIRouter()

@router.get('/')
def healthy():
    return {
        'message': 'ok'
    }

@router.post('/')
def receive_coordinates(ip: IP):
    response = get_ip_coordinates(ip)
    return {"mess": response}

@router.post('/coordinates')
def send_coordinates(data):
    post_to_db(data)
    return {
        'mess': 'ok'
    }
    
@router.get('/coordinates')
def display_all_coordinates():
    items = get_items()
    return items