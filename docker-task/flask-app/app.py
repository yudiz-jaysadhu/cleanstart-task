from flask import Flask, request
import redis
import os

app = Flask(__name__)

# Connect to Redis
try:
    r = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379)
    r.ping()
    redis_connected = True
except:
    redis_connected = False

@app.route('/')
def home():
    # Get the host from the request
    host = request.host.split(':')[0]  # Gets IP without port
    
    if redis_connected:
        count = r.incr('visits')
        return f"""
        <h1>Flask App in Docker</h1>
        <p>This page has been visited {count} times</p>
        <p>Redis Status: Connected</p>
        <p><a href="http://{host}:8080">View Static Site</a></p>
        """
    else:
        return f"""
        <h1>Flask App in Docker</h1>
        <p>Redis Status: Not Connected</p>
        <p><a href="http://{host}:8080">View Static Site</a></p>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
