# Timezone API

timezone-api is lightweight Flask app with TimezoneFinder(L) python library and
provides a simple interface. Your request the timezone information for specific
latitude and longtitude pair.

## Request Parameters

Parameters are separated using the ampersand(&) character.

* **lat**: latitude (eg. lat=39.6034810) _(Required)_
* **lng**: longtitude (eg. lng=-119.6822510) _(Required)_
* **timestamp**: timestamp (eg. timestamp=1331161200) _(Required)_

### Example Request

**Request:**

API urls must follow this format:

`https://api.example.com/timezone/api?lng=-119.6822510&lat=39.6034810&timestamp=1331766000`

**Response:**

`{"dstoffset":3600.0,"rawoffset":-28800.0,"status":200,"tzname":"America/Los_Angeles"}`

    - tzname: Timezone name
    - dstoffset: the offset for daylight-savings time in seconds.
    This will be zero if the time zone is not in Daylight Savings Time during the specified timestamp.
    - rawoffset: the offset from UTC (in seconds) for the given location.
    This does not take into effect daylight savings.
    - status: response code
        - 200: the request was successful
        - 400: missing parameter(s)
        - 422: out of bounds error

## API Health

To check the API status or health

**Request:**

`https://api.example.com/timezone/health/`

**Response:**
OK

## API Info

For information about API

**Request:**

`https://api.example.com/timezone/info/`

**Response:**

`{"debug":false,"running-since":1620688782.0930135,"version":"0.0.1"}`

    - debug: APP debug status
    - running-since: API start time
    - version: API version

## Installation

### I. Method: From Docker Hub

`$ docker run -d -p 8080:8000 --name timezone-35 mofm/timezone-api`

* Test

$ curl --request GET  "http://127.0.0.1:8080/timezone/api/?lng=-119.6822510&lat=39.6034810&timestamp=1331766000"

`{
  "dstoffset": 3600.0, 
  "rawoffset": -28800.0, 
  "status": 200, 
  "tzname": "America/Los_Angeles"
}`

### II. Method: Build Docker image

* Clone this repostory

`git clone https://github.com/mofm/timezone-api.git`

* Build Docker image (slim image with Google Distroless)
  
`docker build -t timezone-img .`

* Running Docker image

 `docker run -d -p 8080:8000 --name timezone-api ti
 
* Test

$ curl --request GET  "http://127.0.0.1:8080/timezone/api/?lng=-119.6822510&lat=39.6034810&timestamp=1331766000"

`{
  "dstoffset": 3600.0, 
  "rawoffset": -28800.0, 
  "status": 200, 
  "tzname": "America/Los_Angeles"
}`
