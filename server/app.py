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
        return make_response({'user': user.to_dict()}, 201)

api.add_resource(Users, '/api/v1/users')

class Streams(Resource):
    def get(self):
        all_streams = [s.to_dict() for s in Stream.query.all()]
        return make_response(all_streams, 200)

api.add_resource(Streams, '/streams')

class Animes(Resource):
    def get(self):
        all_animes = [a.to_dict() for a in Anime.query.all()]
        return make_response(all_animes, 200)

    def post(self):
        params = request.json
        try:
            anime = Anime(name = params['name'], image = params['image'], num_episodes = params['num_episodes'], summary = params['summary'], completed = params['completed'], likes = params['likes'])
        except ValueError as v_error:
            return make_response({"Errors": [str(v_error)]}, 422)
        db.session.add(anime)
        db.session.commit()
        return make_response(anime.to_dict(), 201)

api.add_resource(Animes, '/animes')

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

api.add_resource(AnimesById, '/animes/<int:id>')

class AnimesInStream(Resource):
    def get(self, id):
        stream_id = Stream.query.get(id)
        if not stream_id:
            return make_response({"Error": "No Streams with that id."}, 404)
        animes_in_stream = stream_id.animes
        anime_shows = [a.to_dict() for a in animes_in_stream]
        return make_response(anime_shows, 200)

api.add_resource(AnimesInStream, '/streams/<int:id>/animes')




@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

