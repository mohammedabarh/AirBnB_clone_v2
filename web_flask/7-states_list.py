#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page displaying all State objects stored in the database.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
