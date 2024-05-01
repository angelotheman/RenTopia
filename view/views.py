#!/usr/bin/python3
"""This is the views or routes for the website"""
from view import views
from flask import render_template


@views.route('/', strict_slashes=False, methods=['GET'])
def home_page():
    """Landing page"""
    return ('<h1>Welcome to RenTopia! Enjoy!</h1>')
