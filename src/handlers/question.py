from database import DB
import json
from random import randint
import logging

def Question(user_uuid, themes, failed, completed):
  conn = DB.connect()
  print('lool1')
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

  question = {'uuid': questions[randint(0, len(questions) - 1)]}

  cur.execute(DB.get_prepared('select_question'), 
              (question['uuid']))
  row = cur.fetchone()

  logging.getLogger('service').info("WTF???")

  content = json.loads(row['content'])

  question['title'] = content['title']
  question['answers'] = content['answers']

  return {"question": json.dumps(question)}
