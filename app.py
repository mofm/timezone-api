"""Lightweight Timezone API with Flask and TimezoneFinderL"""
import os
import logging
from time import time
from datetime import datetime
import pytz
import flask
from flask import Flask, request, jsonify
from timezonefinder import TimezoneFinderL


# Version of this APP template
__version__ = '0.0.1'
# Read env variables
SERVICE_START_TIMESTAMP = time()
DEBUG = os.environ.get('DEBUG', False)


app = Flask(__name__)
# Gunicorn log level as Flask's log level
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


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
        return jsonify(message="Missing required argument(s)", status=400)
    try:
        lng, lat = float(lng), float(lat)
        tstamp = int(tstamp)
        tzone = tfind.timezone_at(lng=lng, lat=lat)
        tz = pytz.timezone(tzone)
        tz_time = datetime.fromtimestamp(tstamp)
        dst_offset = tz.dst(tz_time, is_dst=False).total_seconds()
        return jsonify({'dstoffset': dst_offset, 'tzname': tzone, 'status': 200})

    except ValueError:
        return jsonify(message="Parameter(s) out of bounds", status=422)


@app.route('/timezone/health/', methods=['GET'])
def health_check():
    """api status"""
    return flask.Response("OK", status=200)


@app.route('/timezone/info/', methods=['GET'])
def api_info():
    """api infos"""
    info = {
        'version':  __version__,
        'running-since': SERVICE_START_TIMESTAMP,
        'debug': DEBUG
    }
    return jsonify(info)


if __name__ == '__main__':
    app.run()
