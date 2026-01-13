import time
import redis

def get_redis_connection():
    max_retries = 5
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            r = redis.Redis(
                host='redis',
                port=6379, 
                decode_responses=True
            )
            return r
        except redis.ConnectionError as e:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                raise