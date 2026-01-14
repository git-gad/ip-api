import time
import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def get_redis_connection():
    max_retries = 5
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            r = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
            )
            return r
        except redis.ConnectionError as e:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                raise

def save_to_db(data: dict):
    r = get_redis_connection()
    item_id = r.incr('items:id:seq')
    r.hset(f'item:{item_id}', mapping=data)
    r.rpush('items:ids',item_id)
    
    return item_id

def get_all_items():
    r = get_redis_connection()
    ids = r.lrange("items:ids", 0, -1)

    items = []
    for item_id in ids:
        data = r.hgetall(f"item:{item_id}")
        if data:
            items.append({"id": int(item_id), **data})

    return items