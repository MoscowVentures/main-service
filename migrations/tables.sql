CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DROP SCHEMA IF EXISTS app CASCADE;

CREATE SCHEMA IF NOT EXISTS app;

CREATE TABLE app.users (
  uuid TEXT PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL,
  year INTEGER NOT NULL,
  phone TEXT NOT NULL UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE app.themes (
  uuid TEXT PRIMARY KEY DEFAULT uuid_generate_v4(),
  title TEXT NOT NULL UNIQUE
);

CREATE TABLE app.question_types (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL UNIQUE
);

CREATE TABLE app.questions (
  uuid TEXT PRIMARY KEY DEFAULT uuid_generate_v4(),
  question_type INTEGER,
  content TEXT NOT NULL DEFAULT '{"title":""}',
  right_answers TEXT NOT NULL DEFAULT '"right_answers":[]',
  level INTEGER NOT NULL,
  age INTEGER NOT NULL,
  theme TEXT NOT NULL,

  CONSTRAINT fk__question_type__questions
    FOREIGN KEY (question_type) 
      REFERENCES app.question_types(id),
  CONSTRAINT fk__theme__questions
    FOREIGN KEY (theme) 
      REFERENCES app.themes(uuid)
);

CREATE TABLE app.questions_x_users (
  question_uuid TEXT NOT NULL,
  user_uuid TEXT NOT NULL, 
  completed BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL DEFAULT now(),
  
  CONSTRAINT unique__questions_x_users UNIQUE (question_uuid, user_uuid),

  CONSTRAINT fk__user_uuid__questions_x_users 
    FOREIGN KEY (user_uuid) 
      REFERENCES app.users(uuid),
  CONSTRAINT fk__question_uuid__questions_x_users 
    FOREIGN KEY (question_uuid) 
      REFERENCES app.questions(uuid)
);

CREATE TABLE app.stories (
  uuid TEXT PRIMARY KEY DEFAULT uuid_generate_v4(),
  show BOOLEAN DEFAULT TRUE,
  text TEXT,
  image_url TEXT NOT NULL
);
