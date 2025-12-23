import os
import redis

REDIS_URL = os.getenv("REDIS_URL")

redis_client = None

if REDIS_URL:
    try:
        redis_client = redis.from_url(REDIS_URL, decode_responses=True)
        redis_client.ping()
        print("Redis connected")
    except Exception as e:
        print("Redis connection failed:", e)
        redis_client = None
