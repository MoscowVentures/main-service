WITH completed_questions AS (
  SELECT question_uuid 
  FROM app.questions_x_users
  WHERE user_uuid = %s AND completed = TRUE
), failed_questions AS (
  SELECT question_uuid 
  FROM app.questions_x_users
  WHERE user_uuid = %s AND completed = FALSE
)

SELECT content, level, age, theme
FROM app.questions
WHERE level < $1 AND level > $1 AND
  age < $2 AND age > $2 AND
  theme = ANY($3::TEXT[]);