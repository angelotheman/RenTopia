#!/usr/bin/python3
"""This is the views or routes for the website"""

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/', strict_slashes=False, methods=['GET'])
def home_page():
    """Landing page"""
    return render_template('index.html')

@views.route('/login', strict_slashes=False, methods=['GET'])
def login():
    """Login page"""
    return render_template('login.html')


@views.route('/signup', strict_slashes=False, methods=['GET'])
def signup():
    """Signup page"""
    return render_template('signup.html')
