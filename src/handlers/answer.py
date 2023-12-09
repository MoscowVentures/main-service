from database import DB
import json
from random import randint
import logging

def Answer(user_uuid, question_uuid, answers):
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('select_question'),
              (question_uuid,))

  answers_set = set(answers)

  row = cur.fetchone()
  right_answers = json.loads(row[6])['right_answers']
  right_answers_set = set(right_answers)

  cur.execute(DB.get_prepared('insert_answer'),
              (question_uuid,
               user_uuid,
               answers_set == right_answers_set))

  conn.close()
  
  return 
