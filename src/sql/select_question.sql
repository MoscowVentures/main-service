SELECT uuid, question_type, content, level, age, theme, right_answers
FROM app.questions
WHERE uuid = %s;