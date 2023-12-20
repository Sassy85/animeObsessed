#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from models import Anime, Platform, Stream
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api

# Add your model imports
from models import User

class Users(Resource):
    def post(self):
        params = request.json
        user = User(username = params['username'], email = params['email'], password_hash = params['password'])
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        return make_response({'user': user.to_dict()}, 201)

api.add_resource(Users, '/api/v1/users')

@app.route('/api/v1/authorized')
def authorized():
    try:
        #same as query.get(id)
        user = User.query.filter_by(id=session.get('user_id')).first()
        return make_response(user.to_dict(), 200)
    except:
        return make_response({"Error": "User not found"}, 404)

@app.route('/api/v1/logout', methods=['DELETE'])
def logout():
    session['user_id'] = None
    return make_response("", 204)

@app.route('/api/v1/login', methods=['POST'])
def login():
    params = request.json
    try:
        user = User.query.filter_by(username=params['username']).first()
        if user.authenticate(params['password']):
            session['user_id'] = user.id
            return make_response({'user': user.to_dict()}, 200)
        else:
            return make_response({'Error': 'Password Incorrect'}, 401)
    except:
            return make_response({'Error': 'Username Incorrect'}, 401)

class Streams(Resource):
    def get(self):
        all_streams = [s.to_dict() for s in Stream.query.all()]
        return make_response(all_streams, 200)

api.add_resource(Streams, '/api/v1/streams')

class Animes(Resource):
    def get(self):
        all_animes = [a.to_dict() for a in Anime.query.all()]
        return make_response(all_animes, 200)

    def post(self):
        params = request.json
        try:
            anime = Anime(name = params['name'], image = params['image'], num_episodes = params['num_episodes'], summary = params['summary'], stream = params['stream'], likes = params['likes'])
        except ValueError as v_error:
            return make_response({"Errors": [str(v_error)]}, 422)
        db.session.add(anime)
        db.session.commit()
        return make_response(anime.to_dict(), 201)

api.add_resource(Animes, '/api/v1/animes')

class AnimesById(Resource):
    def get(self, id):
        anime_id = Anime.query.get(id)
        if not anime_id:
            return make_response({"Error": "No anime with that id!"}, 404)
        return make_response(anime_id.to_dict(), 200)

    def delete(self, id):
        anime = Anime.query.get(id)
        if not anime:
            return make_response({"Error": "Anime not found!"}, 404)
        db.session.delete(anime)
        db.session.commit()
        return make_response("", 204)

    def patch(self, id):
        anime = Anime.query.get(id)
        if not anime:
            return make_response({"Error": "Anime not found!"}, 404)
        params = request.json
        try:
            for attr in params:
                setattr(anime, attr, params[attr])
        except ValueError as v_error:
            return make_response({"Errors": [str(v_error)]}, 422)
        db.session.commit()
        return make_response(anime.to_dict(), 200)

api.add_resource(AnimesById, '/api/v1/animes/<int:id>')

class AnimesInStream(Resource):
    def get(self, id):
        stream_id = Stream.query.get(id)
        if not stream_id:
            return make_response({"Error": "No Streams with that id."}, 404)
        animes_in_stream = stream_id.animes
        anime_shows = [a.to_dict() for a in animes_in_stream]
        return make_response(anime_shows, 200)

api.add_resource(AnimesInStream, '/api/v1/streams/<int:id>/animes')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.before_request
def check_logged_id():
    if request.endpoint in ['streams', 'animes'] and not session.get('user_id'):
        return make_response({'Error': 'Unauthorized, please login!'}, 401)
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)

