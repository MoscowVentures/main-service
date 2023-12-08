WITH users_questions AS (
  SELECT question_uuid, completed
  FROM app.questions_x_users
  WHERE user = %s
), questions_x_themes AS (
  SELECT app.questions.uuid, app.questions.theme, users_questions.completed
  FROM users_questions
  INNER JOIN app.questions ON app.questions.uuid == users_questions.question_uuid
)