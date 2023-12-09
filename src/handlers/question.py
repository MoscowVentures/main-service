from database import DB
import json
from random import randint
import logging

from flask import Response

import os

import requests

NEURO_BASEURL = os.environ.get('NEURO_BASEURL')
ANTIFRAUD_DURATION = 300

# def antifraud(user_uuid):
#   conn = DB.connect()
#   cur = conn.cursor()
#   cur.execute(DB.get_prepared('select_last_answers'), 
#               (user_uuid,))
#   row = cur.fetchone()
#   conn.close()

#   return True

def GetNeuroQuestion(user_uuid):
  # if (antifraud(user_uuid)):
  #   return {}

  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('get_user_stat'), 
              (user_uuid,))
  rows = cur.fetchall()
  conn.close()

  theme_uuid = row[2]

  themes = []
  for row in rows:
    themes.append({'res': row[0], 'theme_uuid': theme_uuid, 'theme_name': row[3]})
  response = requests.post(NEURO_BASEURL + '/', json={'themes':themes})

  question = {}

  question = response.json['question']
  right_answers = response.json['right_answers']
  level = response.json['level']
  age = response.json['age']

  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('insert_question'), 
              (1,question,right_answers,level,age,theme_uuid))
  row = cur.fetchone()
  conn.close()

  return {'question': question}
  

def GetQuestion(user_uuid, themes, failed, completed):
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('select_questions'), 
              (user_uuid,
               0,10,
               0,99,
               themes,
               failed,
               completed))
  rows = cur.fetchall()
  questions = []
  for row in rows:
    questions.append(row[0])

  if len(questions) == 0:
    return {}

  question = {'uuid': questions[randint(0, len(questions) - 1)]}

  cur.execute(DB.get_prepared('select_question'), 
              (question['uuid'],))
  row = cur.fetchone()
  theme_uuid = row[5]

  content = json.loads(row[2])
  question['title'] = content['title']
  question['answers'] = content['answers']

  cur.execute(DB.get_prepared('select_theme'), 
              (theme_uuid,))
  row = cur.fetchone()
  question['theme'] = row[1]
  
  conn.close()

  return {'question': question}


def Question(user_uuid, themes, failed, completed, neuro):
  neuro = False

  if neuro:
    return GetNeuroQuestion(user_uuid)
  else:
    return GetQuestion(user_uuid, themes, failed, completed)