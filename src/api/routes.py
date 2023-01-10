"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, Vehicle, Favorite
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#     }

#     return jsonify(response_body), 200


@api.route('/users', methods=['GET','POST'])
def get_users():
    if request.method == 'GET':
        users = User.query.all()
        users_dictionaries = []

        for user in users:
            users_dictionaries.append(user.serialize())
        return jsonify(users_dictionaries), 200
    
    new_user_data = request.json
            # new_user = User.create(
            #     email = new_user_data['email'],
            #     username = new_user_data['username'],
            # )
    try:
        new_user = User.create(**new_user_data)
        return jsonify(new_user.serialize()),201
    except Exception as error:
        return jsonify(error.args[0]),error.args[1] if len(error.args) > 1 else 500


@api.route('/characters', methods=['GET', 'POST'])
def get_characters():
    if request.method == 'GET':
        characters = Character.query.all()
        characters_dictionaries = []
        for character in characters:
            characters_dictionaries.append(character.serialize())
        return jsonify(characters_dictionaries), 200

    new_character_data = request.json
    try:
        new_character = Character.create(**new_character_data)
        return jsonify(new_character.serialize()), 201
    except Exception as error:
        return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500

@api.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Character.query.filter_by(id = character_id)
    try:
        return jsonify(caracter[0].serialize())
    except Exception as error:
        return jsonify({"message": "Couldn't find the character."})


@api.route('/planets', methods=['GET', 'POST'])
def get_planets():
    if request.method == 'GET':
        planets = Planet.query.all()
        planets_dictionaries = []
        for planet in planets:
            planets_dictionaries.append(planet.serialize())
        return jsonify(planets_dictionaries), 200

    new_planet_data = request.json
    try:
        new_planet = Planet.create(**new_planet_data)
        return jsonify(new_planet.serialize()), 201
    except Exception as error:
        return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    character = Planet.query.filter_by(id = planet_id)
    try:
        return jsonify(planet[0].serialize())
    except Exception as error:
        return jsonify({"message": "Couldn't find the planet."})


@api.route('/vehicles', methods=['GET', 'POST'])
def get_vehicles():
    if request.method == 'GET':
        vehicles = Vehicle.query.all()
        vehicles_dictionaries = []
        for vehicle in vehicles:
            vehicles_dictionaries.append(vehicle.serialize())
        return jsonify(vehicles_dictionaries), 200

    new_vehicle_data = request.json
    try:
        new_vehicle = Vehicle.create(**new_vehicle_data)
        return jsonify(new_vehicle.serialize()), 201
    except Exception as error:
        return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500

@api.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = Vehicle.query.filter_by(id = vehicle_id)
    try:
        return jsonify(vehicle[0].serialize())
    except Exception as error:
        return jsonify({"message": "Couldn't find the vehicle."})


@api.route('users/<int:user_id>/favorites', methods=['GET'])
def get_favorites(user_id):
    favorites = Favorite.query.filter_by(user_id = user_id)
    favorites_dictionary = []
    for favorite in favorites:
        favorites_dictionary.append(favorite.serialize())
    return jsonify(favorites_dictionary), 200


@api.route('favorite/characters/<int:user_id>/<int:character_id>', methods=['POST'])
def add_character_to_favorites(character_id, user_id):

    new_favorite_data = request.json
    favorites = Favorite.query.filter_by(user_id = user_id, character_id = character_id).first()
    if favorites is not None:
        return jsonify({"message": "The character is already in favorites."}), 401
    else:
        try:
            new_favorite = Favorite.create_favorite(user_id = user_id, character_id = character_id, **new_favorite_data)
            return jsonify(new_favorite.serialize()), 201
        except Exception as error:
            return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500

@api.route('favorite/characters/<int:user_id>/<int:character_id>', methods=['DELETE'])  
def delete_character_from_favorites(character_id, user_id):
    favorite_to_delete = Favorite.query.filter_by(user_id = user_id, character_id = character_id).first()
    try:
        delete_char = Favorite.delete_favorite(favorite_to_delete)
        return jsonify(delete_char), 200
    except Exception as error:
        return jsonify(error.args[0]),error.args[1] if len(error.args) > 1 else 500


@api.route('favorite/planets/<int:user_id>/<int:planet_id>', methods=['POST'])
def add_planet_to_favorites(planet_id, user_id):

    new_favorite_data = request.json
    favorites = Favorite.query.filter_by(user_id = user_id, planet_id = planet_id).first()
    if favorites is not None:
        return jsonify({"message": "The planet is already in favorites."}), 401
    else:
        try:
            new_favorite = Favorite.create_favorite(user_id = user_id, planet_id = planet_id, **new_favorite_data)
            return jsonify(new_favorite.serialize()), 201
        except Exception as error:
            return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500

@api.route('favorite/planets/<int:user_id>/<int:planet_id>', methods=['DELETE'])  
def delete_planet_from_favorites(planet_id, user_id):
    favorite_to_delete = Favorite.query.filter_by(user_id = user_id, planet_id = planet_id).first()
    try:
        delete_planet = Favorite.delete_favorite(favorite_to_delete)
        return jsonify(delete_planet), 200
    except Exception as error:
        return jsonify(error.args[0]),error.args[1] if len(error.args) > 1 else 500


@api.route('favorite/vehicles/<int:user_id>/<int:vehicle_id>', methods=['POST'])
def add_vehicle_to_favorites(vehicle_id, user_id):

    new_favorite_data = request.json
    favorites = Favorite.query.filter_by(user_id = user_id, vehicle_id = vehicle_id).first()
    if favorites is not None:
        return jsonify({"message": "The vehicle is already in favorites."}), 401
    else:
        try:
            new_favorite = Favorite.create_favorite(user_id = user_id, vehicle_id = vehicle_id, **new_favorite_data)
            return jsonify(new_favorite.serialize()), 201
        except Exception as error:
            return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500

@api.route('favorite/vehicles/<int:user_id>/<int:vehicle_id>', methods=['DELETE'])  
def delete_vehicle_from_favorites(vehicle_id, user_id):
    favorite_to_delete = Favorite.query.filter_by(user_id = user_id, vehicle_id = vehicle_id).first()
    try:
        delete_vehicle = Favorite.delete_favorite(favorite_to_delete)
        return jsonify(delete_vehicle), 200
    except Exception as error:
        return jsonify(error.args[0]),error.args[1] if len(error.args) > 1 else 500
