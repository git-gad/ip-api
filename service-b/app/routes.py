from fastapi import APIRouter, HTTPException
import os
from dal import get_redis_connection

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