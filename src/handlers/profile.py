from database import DB

def get_user_by_uuid(uuid):
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('get_user_by_uuid'), (uuid,))
  row = cur.fetchone()
  logging.getLogger('service').info(uuid)
  conn.close()   
  return row


def Profile(uuid):
    row = get_user_by_uuid(uuid)

    