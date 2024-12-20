from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.db.Column(db.db.Integer, primary_key=True)
#     email = db.db.Column(db.db.String(120), unique=True, nullable=False)
#     password = db.db.Column(db.db.String(80), unique=False, nullable=False)
#     is_active = db.db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    fecha_suscripcion = db.Column(db.DateTime(timezone=True), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'fecha_suscripcion': self.fecha_suscripcion.isoformat()  # Formato ISO para DateTime
        }


class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'diameter': self.diameter,
            'population': self.population,
            'climate': self.climate
        }
    

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'hair_color': self.hair_color,
            'eye_color': self.eye_color
        }
    

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'vehicle_class': self.vehicle_class,
            'passengers': self.passengers
        }
    

class Create_Planet(db.Model):
    __tablename__ = 'create_planet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_create_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    user = db.relationship("User")
    planet = relationship("Planet")


class Create_Character(db.Model):
    __tablename__ = 'create_character'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    chracter_create_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    user = db.relationship("User")
    character = relationship("Character")


class Create_Vehicle(db.Model):
    __tablename__ = 'create_vehicle'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicle_create_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    user = db.relationship("User")
    vehicle = relationship("Vehicle") 

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)  # Si el favorito es un planeta
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=True)  # Si el favorito es un vehículo
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)

    user = db.relationship("User", backref="favorites")
    planet = db.relationship("Planet", backref="favorited_by", lazy=True)
    vehicle = db.relationship("Vehicle", backref="favorited_by", lazy=True)
    character = db.relationship("Character", backref="favorited_by", lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'planet': self.planet.serialize() if self.planet else None,
            'vehicle': self.vehicle.serialize() if self.vehicle else None,
            'character': self.character.serialize() if self.character else None
        }


class Favorito_Planet(db.Model):
    __tablename__ = 'favorito_planet'
    id = db.Column(db.Integer, primary_key=True)
    planet_favorito_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User")
    planet = relationship("Planet")
    

class Favorito_Character(db.Model):
    __tablename__ = 'favorito_character'
    id = db.Column(db.Integer, primary_key=True)
    character_favorito_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User")
    character = relationship("Character")


class Favorito_Vehicle(db.Model):
    __tablename__ = 'favorito_vehicle'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_favorito_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User")
    vehicle = relationship("Vehicle")
