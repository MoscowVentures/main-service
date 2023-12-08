SELECT content, level, age, theme
FROM app.questions
WHERE level < $1 AND level > $1 AND
  age < $2 AND age > $2 AND
  theme = ANY($3::TEXT[]);