from database import DB

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
  row = cur.fetchone()
  logging.getLogger('service').info(uuid)
  conn.close()   
  return row


def Profile(uuid):
    user_data = get_user_by_uuid(uuid)
    user_stat = get_user_stat(uuid)
    statistics = []
    for row in user_stat:
      stat = {}
      stat["res"]] = row[0]
      stat["user_uuid"] = row[1]
      stat["theme_uuid"] = row[2]
      statistics.append(stat)
    response = {}
    response["url"] = user_data[1]
    response["name"] = user_data[2]
    response["year"] = user_data[3]
    response["phone"] = user_data[4]
    response["statistics"] = statistics
    return response

    