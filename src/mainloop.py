from typing import Union

from database import DB

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
def read_item():
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('select_theme'), ("123",))
  rows = cur.fetchone()
  conn.close()
  return

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

  APP.run(host=os.environ.get('SERVICE_HOST'), port=os.environ.get('SERVICE_PORT'))