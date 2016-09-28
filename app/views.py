from app import app
from flask import redirect

@app.route('/')
@app.route('/index')
@app.route('/deck')
def deck():  
  return redirect("https://docs.google.com/presentation/d/10Wux1jnxM16b4E1cBmffjlPYOxQiJFZVGKsUBoEwRWE/edit?usp=sharing", code=302)
