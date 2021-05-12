"""Lightweight Timezone API with Flask and TimezoneFinderL"""
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from timezonefinder import TimezoneFinderL

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('lat', type=float, required=True, location='args')
parser.add_argument('lng', type=float, required=True, location='args')

class timezone(Resource):
    def get(self):
        args = parser.parse_args(strict=True)
        tifi = TimezoneFinderL(in_memory=True)

        try:
            return jsonify({'tz_name': tifi.timezone_at(lng=args['lng'], lat=args['lat']), 'status': 200})
        except ValueError:
            return jsonify(message="lat lng out of bounds", status=422)


api.add_resource(timezone, '/')

if __name__ == '__main__':
    app.run()
