"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, Vehicle
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/users', methods=['GET', 'POST'])
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
        return jsonify(new_user.serialize()), 201
    except Exception as error:
        return jsonify(error.args[0]), error.args[1]


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
        return jsonify(error.args[0]), error.args[1]


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
        return jsonify(error.args[0]), error.args[1]


@api.route('/vehicles', methods=['GET', 'POST'])
def get_vehicles():
    if request.method == 'GET':
        vehicles = Planet.query.all()
        vehicles_dictionaries = []
        for vehicle in vehicles:
            vehicles_dictionaries.append(vehicle.serialize())
        return jsonify(vehicles_dictionaries), 200

    new_vehicle_data = request.json
    try:
        new_vehicle = Vehicle.create(**new_vehicle_data)
        return jsonify(new_vehicle.serialize()), 201
    except Exception as error:
        return jsonify(error.args[0]), error.args[1]
    