from flask import Blueprint, request, jsonify
from models import data_storage
from models.apartment import Apartment
from models.booking import Booking
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.location import Location
from view.routes import views

@views.route('/apartments', methods=['GET'])
def get_apartments():
    apartments = data_storage.all(Apartment)
    return jsonify([apartment.to_dict() for apartment in apartments.values()])

@views.route('/apartments', methods=['POST'])
def create_apartment():
    data = request.get_json()
    apartment = Apartment(**data)
    data_storage.new(apartment)
    data_storage.save()
    return jsonify(apartment.to_dict()), 201

@views.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = data_storage.all(Booking)
    return jsonify([booking.to_dict() for booking in bookings.values()])

@views.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    booking = Booking(**data)
    data_storage.new(booking)
    data_storage.save()
    return jsonify(booking.to_dict()), 201

@views.route('/users', methods=['GET'])
def get_users():
    users = data_storage.all(User)
    return jsonify([user.to_dict() for user in users.values()])

@views.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    data_storage.new(user)
    data_storage.save()
    return jsonify(user.to_dict()), 201

@views.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = data_storage.all(Review)
    return jsonify([review.to_dict() for review in reviews.values()])

@views.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review = Review(**data)
    data_storage.new(review)
    data_storage.save()
    return jsonify(review.to_dict()), 201

@views.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = data_storage.all(Amenity)
    return jsonify([amenity.to_dict() for amenity in amenities.values()])

@views.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    amenity = Amenity(**data)
    data_storage.new(amenity)
    data_storage.save()
    return jsonify(amenity.to_dict()), 201

@views.route('/locations', methods=['GET'])
def get_locations():
    locations = data_storage.all(Location)
    return jsonify([location.to_dict() for location in locations.values()])

@views.route('/locations', methods=['POST'])
def create_location():
    data = request.get_json()
    location = Location(**data)
    data_storage.new(location)
    data_storage.save()
    return jsonify(location.to_dict()), 201
