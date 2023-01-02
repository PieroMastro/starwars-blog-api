from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, **kwargs):
        self.email = kwargs['email']
        self.username = kwargs['username']
        self.password = kwargs['password']

    @classmethod
    def create(cls, **kwargs):
        new_user = cls(**kwargs)
        db.session.add(new_user) # INSERT INTO

        try:
            db.session.commit() #  INSERT INTO IS EXECUTED
            return 
        except Exception as error:
            raise Exception(error.args[0], 400)
            
    # def __repr__(self):
    #     return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    height  = db.Column(db.String(50))
    skin_color  = db.Column(db.String(50))
    birth_year  = db.Column(db.String(50))

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.gender = kwargs['gender']
        self.hair_color = kwargs['hair_color']
        self.eye_color = kwargs['eye_color']
        self.height = kwargs['height']
        self.skin_color = kwargs['skin_color']
        self.birth_year = kwargs['birth_year']

    @classmethod
    def create(cls, *kwargs):
        new_character = cls(*kwargs)
        db.session.add(new_character)

        try:
            db.session.commit()
            return new_character
        except Exception as error:
            raise Exception(error.args[0], 400)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "height": self.height,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year,
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    diameter = db.Column(db.String(50))
    orbital_period = db.Column(db.String(50))
    population = db.Column(db.String(50))
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.diameter = kwargs['diameter']
        self.orbital_period = kwargs['orbital_period']
        self.population = kwargs['population']
        self.climate = kwargs['climate']
        self.terrain = kwargs['terrain']

    @classmethod
    def create(cls, *kwargs):
        new_planet = cls(**kwargs)
        db.session.add(new_planet)

        try:
            db.session.commit()
            return new_planet
        except Exception as error:
            raise Exception(error.args[0], 400)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
        }


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    model = db.Column(db.String(50))
    vehicle_class = db.Column(db.String(50))
    cost_in_credits = db.Column(db.String(50))
    length = db.Column(db.String(50))
    passengers = db.Column(db.String(50))

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.model = kwargs['model']
        self.vehicle_class = kwargs['vehicle_class']
        self.cost_in_credits = kwargs['cost_in_credits']
        self.length = kwargs['length']
        self.passengers = kwargs['passengers']

    @classmethod
    def create(cls, **kwargs):
        new_vehicle = cls(**kwargs)
        db.session.add(new_vehicle)
        try:
            db.session.commit()
            return new_planet
        except Exception as error:
            raise Exception(error.args[0], 400)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "passengers": self.passengers,
        }


# class Favorite(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
#     planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
#     vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"))
    