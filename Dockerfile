# pull official base image
FROM python:3.9.5-slim-buster AS build

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip

# Build the virtualenv as a separate step: Only re-execute this step when requirements.txt changes
FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Copy the virtualenv into a distroless image
FROM python:3.9.5-slim-buster
COPY --from=build-venv /venv /venv

# set work directory
WORKDIR /usr/src/app

# Set Virtual ENV
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV=development
ENV FLASK_APP=app.py

# Copy Project
COPY app.py /usr/src/app/
COPY entrypoint.sh /usr/src/app/

# run gunicorn
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]