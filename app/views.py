from app import app
from flask import Flask, redirect, jsonify, render_template, request
import redis

@app.route('/deck')
def deck():
  return redirect("https://docs.google.com/presentation/d/10Wux1jnxM16b4E1cBmffjlPYOxQiJFZVGKsUBoEwRWE/edit?usp=sharing", code=302)

@app.route('/_pull')
def get_messages():
    print "get_messages called"
    ps = redis.StrictRedis(host='ec2-52-54-82-137.compute-1.amazonaws.com', port=6379, db=0, password='BFHW6zDv3g7kuxDxRXV7K8Y2pdyfR7kw').pubsub()
    ps.subscribe('tcp.private')
    payloads = []
    for i in xrange(0, 11):
        msg = ps.get_message(True, timeout=1000)
        if msg:
            print str(msg['data'])
            vals = str(msg['data']).split(",")
            payloads.append({"Connection": vals[0], "Protocol": vals[1], "Classification": vals[2]})
    return jsonify(payloads=payloads)

@app.route('/')
def index():
    return render_template('index.html')




