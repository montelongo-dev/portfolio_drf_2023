FROM python:latest

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/venv

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install software-properties-common -y 
    # && add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update \
    && apt-get install -y \
    python3-pip \
    expect \
    python3 \
    python3-venv \
    python3-dev \
    # postgresql-client \
    libpq-dev \
    # curl \
    # wget \
    # && curl https://cli-assets.heroku.com/install.sh | sh \
    && python3 -m venv $VIRTUAL_ENV

ENV PATH="/venv/bin:$PATH"

COPY . /app/

RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

EXPOSE 8000