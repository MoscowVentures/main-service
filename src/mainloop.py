from typing import Union
from handlers.login import Login, get_token
from database import DB
import logging

from flask import Flask
from flask import request
from flask import Response
import redis

from handlers.home import Home

import os

REDIS = redis.StrictRedis(
  host=os.environ.get('REDIS_HOST'), 
  port=os.environ.get('REDIS_PORT'), 
  db=0, 
  password=os.environ.get('REDIS_PASSWORD'),
  charset="utf-8", 
  decode_responses=True
)
APP = Flask(__name__)

@APP.route("/login", methods=["POST"])
def login():
  phone = request.json['phone']
  name = request.json['name']
  year = request.json['year']
  return Login(REDIS, phone, name, year)

@APP.route("/confirm", methods=["GET"])
def confirm():
  phone = request.json['phone']
  code = request.json['code']
  return get_token(REDIS, phone, code)


@APP.route("/home", methods=["POST"])
def HomeHandler():
  return Home()

if __name__ == "__main__":
  DB.set("dbname='{}' user='{}' port={} host='{}' password='{}'".format(
    os.environ.get('POSTGRES_DB'),
    os.environ.get('POSTGRES_USER'),
    os.environ.get('POSTGRES_PORT'),
    os.environ.get('POSTGRES_HOST'),
    os.environ.get('POSTGRES_PASSWORD')
  ))
  DB.prepare('select_themes')
  DB.prepare('select_active_stories')
  DB.prepare('create_user')

  DB.prepare('get_user_by_phone')
  APP.run(host=os.environ.get('SERVICE_HOST'), port=os.environ.get('SERVICE_PORT'))
