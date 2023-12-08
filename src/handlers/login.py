def take_token(redis, uuid, code):
    # res = redis.set(code + uuid, code)
    # print(res)
    token = redis.get(code + uuid)
    print(token)
    return token