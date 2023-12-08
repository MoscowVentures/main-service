from database import DB
import json
from random import randint
import logging

def Question(user_uuid, themes, failed, completed):
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

  return {"question": question}
