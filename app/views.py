from app import app
from flask import redirect
import redis

@app.route('/')
@app.route('/index')
def get_messages():
    ps = redis.StrictRedis(host='ec2-52-54-82-137.compute-1.amazonaws.com', port=6379, db=0, password='').pubsub()
    ps.subscribe('tcp.private')
    for message in ps.listen():
        print str(message['data'])

@app.route('/deck')
def deck():  
  return redirect("https://docs.google.com/presentation/d/10Wux1jnxM16b4E1cBmffjlPYOxQiJFZVGKsUBoEwRWE/edit?usp=sharing", code=302)
