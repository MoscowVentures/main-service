INSERT INTO app.questions_x_users (
  question_uuid, user_uuid, completed
) VALUES (
  %s, %s, %s
)
ON CONFLICT (question_uuid, user_uuid)
DO UPDATE SET 
  completed = EXCLUDED.completed
  created_at = now();
