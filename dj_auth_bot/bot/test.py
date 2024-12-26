
import redis

# Try connecting to Redis
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)
r.ping()  # This should return True if the connection is successful
