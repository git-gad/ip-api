from fastapi import APIRouter
from schemas import IP
from services import get_ip_coordinates

router = APIRouter()

@router.post('/')
def receive_ip(ip: IP):
    response = get_ip_coordinates(ip)
    return {"mess": response}