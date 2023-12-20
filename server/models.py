from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db, bcrypt

# a stream has many animes through platforms
# an anime had many streams through platforms
# a platform belongs to a stream and an anime
# stream ---< platform >--- anime

class User(db.Model, SerializerMixin):
    __tablename__='users'

    serialize_rules = ('-_password_hash',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    _password_hash = db.Column(db.String)

    @property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, new_password):
        btye_object = new_password.encode('utf-8')
        encrypted_password = bcrypt.generate_password_hash(btye_object)
        hashed_password = encrypted_password.decode('utf-8')
        self._password_hash = hashed_password

    def authenticate(self, password_string):
        byte_object = password_string.encode('utf-8')
        return bcrypt.check_password_hash(self.password_hash, byte_object)

        def __repr__(self):
            return f'<User {self.name}>'

class Stream(db.Model, SerializerMixin):
    __tablename__='streams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)

    platforms = db.relationship('Platform', back_populates = 'stream', cascade = 'all, delete-orphan')
    animes = association_proxy('platforms', 'anime')

    @validates('name')
    def check_name(self, key, new_name):
        if len(new_name) < 3:
            raise ValueError('Name must be at least 4 characters!')
        return new_name

    serialize_rules = ('-platforms',)

    def __repr__(self):
        return f'<Stream {self.name}>'


class Anime(db.Model, SerializerMixin):
    __tablename__='animes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    num_episodes = db.Column(db.Integer)
    summary = db.Column(db.String)
    stream= db.Column(db.String)
    likes = db.Column(db.Integer)

    platforms = db.relationship('Platform', back_populates = 'anime', cascade = 'all, delete-orphan')
    streams = association_proxy('platforms', 'stream')

    @validates('name')
    def check_name(self, key, new_name):
        if len(new_name) < 3:
            raise ValueError('Name must be at least 4 characters!')
        return new_name

    #@validates('num_episodes')
    #def check_num_episodes(self, key, new_num_episodes):
    #    if new_num_episodes < 0:
    #        raise ValueError('Number of episodes more than 0!')
    #    return new_num_episodes

    @validates('summary')
    def check_summary(self, key, new_summary):
        if len(new_summary) < 19:
            raise ValueError('Summary must be at least 20 characters!')
        return new_summary

    serialize_rules = ('-platforms',)

    def __repr__(self):
        return f'<Anime {self.name}>'


class Platform(db.Model, SerializerMixin):
    __tablename__='platforms'
    id = db.Column(db.Integer, primary_key=True)

    anime_id = db.Column(db.Integer, db.ForeignKey('animes.id'))
    stream_id = db.Column(db.Integer, db.ForeignKey('streams.id'))

    anime = db.relationship('Anime', back_populates = 'platforms')
    stream = db.relationship('Stream', back_populates = 'platforms')

    def __repr__(self):
        return f'<Platform {self.id}>'