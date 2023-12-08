import psycopg2
import logging

class Postgers:
  def set(self, conn_str):
    self.conn_str = conn_str
    self.requests = {}
  
  def connect(self):
    return psycopg2.connect(self.conn_str)

  def prepare(self, name):
    with open("./src/sql/{}.sql".format(name), 'r') as f:
      request_raw = f.read()
    self.requests[name] = request_raw
  
  def get_prepared(self, name):
    return self.requests[name]

DB = Postgers()