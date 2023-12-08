from database import DB
import json

def Question(user_uuid):
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('select_active_stories'), ("123",))
  rows = cur.fetchall()
  stories = []
  for row in rows:
    stories.append({'text':row[0], 'image_url':row[1]})

  cur.execute(DB.get_prepared('select_themes'), ("123",))
  rows = cur.fetchall()
  themes = []
  for row in rows:
    themes.append({'uuid':row[0], 'title':row[1]})

  conn.close()


  return json.dumps({'stories': stories, 'themes': themes})
