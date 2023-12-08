from database import DB
from .jwtcoder import JwtCoder
import logging
import random

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def take_uuid_by_phone(phone):
  conn = DB.connect()
  cur = conn.cursor()
  cur.execute(DB.get_prepared('get_user_by_phone'), (phone,))
  uuid = cur.fetchone()
  logging.info(uuid)
  conn.close()   
  return uuid

def create_user(phone, name, year):
    conn = DB.connect()
    cur = conn.cursor()
    cur.execute(DB.get_prepared('create_user'), (name, year, phone,))
    conn.commit()
    conn.close()

def send_code(redis, uuid):
    random_code = '0000'
    redis.set(uuid, random_code)

def Login(redis, phone, name, year):
    uuid = take_uuid_by_phone(phone)
    if uuid is None:
        create_user(phone, name, year)
    uuid = take_uuid_by_phone(phone)[0]
    send_code(redis, uuid)
    return {}

def is_code_valid(redis, phone, code):
    uuid = take_uuid_by_phone(phone)
    if uuid is None:
        return False
    right_code = redis.get(uuid)
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
        redis.set("salt_" + uuid, salt)
        return {"token": token}
    return {}

def verify(encoded):
    parts = encoded.split('.')

    header_bs64 = parts[0]
    payload_bs64 = parts[1]
    signature_bs64 = parts[2]

    uuid = JwtCoder.__bs64decode_with_fix_padding(payload_bs64)['uuid']
    salt = redis.get("salt_" + uuid)

    signature_income: bytes = JwtCoder.__bs64decode_with_fix_padding(signature_bs64)
    right_signature: bytes = JwtCoder(salt).__create_check_signature(header_bs64, payload_bs64)

    return signature_income == right_signature, uuid

