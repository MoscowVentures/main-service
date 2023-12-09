from database import DB
import json
from random import randint
import logging
from flask import Response

def Answer(user_uuid, question_uuid, answers):
  logging.getLogger('service').info('question uuid: ' + question_uuid)
  answers_set = set(answers)
  logging.getLogger('service').info('answers_set: ' + str(answers_set))

  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('select_question'),
              (question_uuid,))

  row = cur.fetchone()
  if row is None:
    return {'error':'error'}
  logging.getLogger('service').info(row[6])
  right_answers = json.loads(row[6])['right_answers']
  right_answers_set = set(right_answers)

  logging.getLogger('service').info('right_answers_set: ' + str(right_answers_set))

  correct = (answers_set == right_answers_set)

  cur.execute(DB.get_prepared('insert_answer'),
              (question_uuid,
               user_uuid,
               correct))

  conn.close()
  
  return {'correct': correct}
