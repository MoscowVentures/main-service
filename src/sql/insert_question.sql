INSERT INTO app.questions AS (
  question_type, content, right_answers, level, age, theme_uuid
) VALUE (
  %s, %s, %s, %s, %s, %s
) RETURNING uuid;