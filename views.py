"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template
from __init__ import app

@app.route('/')
def index():
    return render_template("index.html")
