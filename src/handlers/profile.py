from database import DB
import logging

def get_user_by_uuid(uuid):
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('get_user_by_uuid'), (uuid,))
  row = cur.fetchone()
  logging.getLogger('service').info(uuid)
  conn.close()   
  return row

def get_user_stat(uuid):
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('get_user_stat'), (uuid,))
  row = cur.fetchall()
  logging.getLogger('service').info(uuid)
  conn.close()   
  return row

def get_user_pos(uuid):
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('get_user_pos'), (uuid,) )
  row = cur.fetchone()
  logging.getLogger('service').info(uuid)
  logging.getLogger('service').info(row)
  conn.close()
  return row

def get_leaderbord():
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('get_leaderboard'))
  rows = cur.fetchall()
  logging.getLogger('service').info(rows)
  conn.close()
  return rows


def Profile(uuid):
    user_data = get_user_by_uuid(uuid)
    user_stat = get_user_stat(uuid)
    user_pos = get_user_pos(uuid)
    statistics = []
    if user_stat is not None:
      for row in user_stat:
        stat = {}
        stat["res"] = row[0]
        stat["user_uuid"] = row[1]
        stat["theme_uuid"] = row[2]
        statistics.append(stat)
    response = {}
    logging.getLogger('service').info(user_data)
    logging.getLogger('service').info(user_stat)
    logging.getLogger('service').info(user_data[1])
    response["url"] = user_data[1]
    response["name"] = user_data[2]
    response["year"] = user_data[3]
    response["phone"] = user_data[4]
    response["statistics"] = statistics
    response["pos"] = user_pos[2]
    return response

def Leaderbord():
  rows = get_leaderbord()
  leaderbord = []
  for row in rows:
    leaderbord.append({
      "res": row[0],
      "name": row[1],
      "pos": row[2]
    })
  return leaderbord
