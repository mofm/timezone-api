"""Lightweight Timezone API with Flask and TimezoneFinderL"""
import os
import logging
from time import time
from datetime import datetime
import pytz
import flask
from flask import Flask, request, jsonify
from timezonefinder import TimezoneFinderL

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('lat', type=float, required=True, location='args')
parser.add_argument('lng', type=float, required=True, location='args')

@app.route('/timezone/api/', methods=['GET'])
def get_timezone():
    """check values and search timezones."""
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    tstamp = request.args.get('timestamp')
    tfind = TimezoneFinderL(in_memory=True)
    if (None not in {lat, lng, tstamp}) and (0 not in {len(lat), len(lng), len(tstamp)}):
        pass
    else:
        return jsonify(message="missing required argument(s)", status=400)
    try:
        lng, lat = float(lng), float(lat)
        tstamp = int(tstamp)
        tzone = tfind.timezone_at(lng=lng, lat=lat)
        tz = pytz.timezone(tzone)
        tz_time = datetime.fromtimestamp(tstamp)
        dst_offset = tz.dst(tz_time, is_dst=False).total_seconds()
        return jsonify({'dstOffset': dst_offset, 'tzname': tzone, 'status': 200})

    except ValueError:
        return jsonify(message="lat lng out of bounds", status=422)


api.add_resource(timezone, '/')

if __name__ == '__main__':
    app.run()
