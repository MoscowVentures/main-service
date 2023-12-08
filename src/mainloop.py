from typing import Union
from handlers.login import Login, get_token, verify
from database import DB
import logging

from datetime import datetime

from flask import Flask
from flask import request
from flask import Response
import redis

from handlers.home import Home
from handlers.question import Question

import traceback
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

def ErrorWrapper(func):
  def wrapper():
    try:
      func()
    except Exception as e:
        return {'error': str(e)}
  return wrapper

@APP.route("/login", methods=["POST"])
def LoginHandler():
  phone = request.json['phone']
  name = request.json['name']
  age = request.json['age']
  return Login(REDIS, phone, name, 2023 - age - 1)

@APP.route("/confirm", methods=["GET"])
def ConfirmHandler():
  phone = request.json['phone']
  code = request.json['code']
  return get_token(REDIS, phone, code)

@APP.route("/test", methods=["GET"])
def TestHandler():
  token = request.json["token"]
  return {"result": verify(REDIS, token)}

@APP.route("/home", methods=["POST"])
def HomeHandler():
  return Home('123')

@ErrorWrapper
@APP.route("/question", methods=["POST"])
def QuestionHandler():
  return Question('uuid',
                  request.json['themes'],
                  request.args.get('failed'),
                  request.args.get('completed'))

if __name__ == "__main__":
  logging.getLogger('service').setLevel(logging.INFO)

  logging.basicConfig(filename='log/{}.log'.format(datetime.now().strftime("%d-%m-%Y-%H-%M-%S")), filemode='a')

  logging.basicConfig(filename="log.log",
					format='%(asctime)s %(message)s',
					filemode='w')
  
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
  DB.prepare('select_questions')

  APP.run(host=os.environ.get('SERVICE_HOST'), port=os.environ.get('SERVICE_PORT'))
