CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DROP SCHEMA IF EXISTS app CASCADE;

CREATE SCHEMA IF NOT EXISTS app;

CREATE TABLE app.users (
  uuid TEXT PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL UNIQUE,
  phone TEXT NOT NULL UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE app.themes (
  uuid TEXT PRIMARY KEY DEFAULT uuid_generate_v4(),
  title TEXT NOT NULL UNIQUE
);

CREATE TABLE app.questions (
  uuid TEXT PRIMARY KEY DEFAULT uuid_generate_v4(),
  type INTEGER,
  content TEXT NOT NULL DEFAULT '{"title":"",}',
  answer TEXT NOT NULL DEFAULT '{"answers":[]}',
  right_answers TEXT NOT NULL DEFAULT '"right_answers":[]',
  level INTEGER NOT NULL,
  age INTEGER NOT NULL,
  theme TEXT NOT NULL
);

CREATE TABLE app.questions_x_users (
  question_uuid TEXT NOT NULL,
  user_uuid TEXT NOT NULL, 
  answered BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);

