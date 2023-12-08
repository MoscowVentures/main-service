SELECT uuid, question_type, content, level, age, theme
FROM app.questions
WHERE uuid = %s;