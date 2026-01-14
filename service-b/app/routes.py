from fastapi import APIRouter, HTTPException
import os
from dal import get_redis_connection, save_to_db, get_all_items
from schemas import CoordinatesData

router = APIRouter()

@router.get('/')
def root_health_check():
    return {
        'status': 'healthy',
        'service': 'redis'
    }
    
@router.get('/health')
def redis_health_check():
    try:
        r = get_redis_connection()
        r.ping()
        r.close()
        return {
            "status": "healthy",
            "redis": "connected"
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Redis unavailable: {str(e)}")
    
@router.post('/coordinates')
def add_coordinates_to_db(data: dict):
    item_id = save_to_db(data)
    return {
        'item_id': item_id,
        'data': data
    }
    
@router.get('/coordinates')
def retrieve_all():
    items = get_all_items()
    return items