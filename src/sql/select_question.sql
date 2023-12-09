SELECT uuid, question_type, content, level, age, theme_uuid, right_answers
FROM app.questions
WHERE uuid = %s;