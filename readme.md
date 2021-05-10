# Timezone API

timezone-api is lightweight Flask app with TimezoneFinder(L) python library and
provides a simple interface. Your request the timezone information for specific
latitude and longtitude pair.

## Request Parameters

Parameters are separated using the ampersand(&) character.

* lat: latitude (eg. lat=52.5061) (Required)
* lng: longtitude (eg. lng=13.358) (Required)

### Example Request

**Request:**

API urls must follow this format:

`https://api.example.com/timezone/api?lng=13.358&lat=52.5061`

**Response:**

`{"status":200,"tz_name":"Europe/Berlin"}`

    - tz_name: Timezone name
    - status: response code
        - 200: the request was successful
        - 400: missing parameter(s)
        - 422: out of bounds error

### API Health

To check the API status or health

**Request:**

`https://api.example.com/timezone/health/`

**Response:**
OK

### API Info

For information about API

**Request:**

`https://api.example.com/timezone/info/`

**Response:**

`{"debug":false,"running-since":1620688782.0930135,"version":"0.0.1"}`

    - debug: APP debug status
    - running-since: API start time
    - version: API version