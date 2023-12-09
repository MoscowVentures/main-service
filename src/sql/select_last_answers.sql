SELECT question_uuid, created_at
FROM app.questions_x_users
WHERE user_uuid = %s AND created_at > now() - '15 minutes'::INTERVAL; 