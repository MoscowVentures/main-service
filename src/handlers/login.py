from database import DB
from .jwtcoder import JwtCoder
import logging
import json
import random
from flask import Response


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# кто это нагавногкодил блять почему take_uuid_by_phone возвращает row?
def take_uuid_by_phone(phone):
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('get_user_by_phone'), (phone,))
  row = cur.fetchone()
  if row is None:
    return None
  uuid = row[0]
  logging.getLogger('service').info(uuid)
  conn.close()   
  return uuid

def create_user(phone, name, year):
    conn = DB.connect()
    cur = conn.cursor()
    cur.execute(DB.get_prepared('create_user'), (name, year, phone,))
    conn.commit()
    conn.close()

def send_code(uuid):
    return '0000'

def Login(redis, phone, name, year):
    uuid = take_uuid_by_phone(phone)
    if uuid is None:
        create_user(phone, name, year)
    uuid = take_uuid_by_phone(phone)
    redis.set(uuid, send_code(uuid))
    return {}

def is_code_valid(redis, phone, code):
    logging.getLogger('service').info('phone:' + str(phone))
    logging.getLogger('service').info('code:' + str(code))
    uuid = take_uuid_by_phone(phone)
    logging.getLogger('service').info('uuid:' + str(uuid))
    if uuid is None:
        return False
    right_code = redis.get(uuid)
    logging.getLogger('service').info('rigth-code:' + str(right_code))
    if right_code == code:
        return True
    return False

def get_token(redis, phone, code):
    chars = []
    for i in range(16):
        chars.append(random.choice(ALPHABET))
    if is_code_valid(redis, phone, code):
        uuid = take_uuid_by_phone(phone)
        salt = "".join(chars)
        token = JwtCoder(salt).encode({"uuid": uuid})
        logging.getLogger("service").info("salt_" + str(uuid))
        logging.getLogger("service").info(salt)
        redis.set("salt_" + uuid, salt)
        logging.getLogger("service").info(redis.get("salt_" + str(uuid)))
        return {"token": token}
    return Response(status=400)

def verify(redis, encoded):
    if encoded == '':
        return False, ''
    parts = encoded.split('.')
    if len(parts) < 3:
        return False, ''

    header_bs64 = parts[0]
    payload_bs64 = parts[1]
    signature_bs64 = parts[2]

    uuid = json.loads(JwtCoder.bs64decode_with_fix_padding(payload_bs64))['uuid']
    salt = None
    try:
        salt = redis.get("salt_" + uuid)
    except Exception:
        pass
    if salt is None:
        return False, ""
    logging.getLogger('service').info(uuid)
    logging.getLogger('service').info(salt)

    signature_income: bytes = JwtCoder.bs64decode_with_fix_padding(signature_bs64)
    right_signature: bytes = JwtCoder(salt).create_check_signature(header_bs64, payload_bs64)

    return signature_income == right_signature, uuid

