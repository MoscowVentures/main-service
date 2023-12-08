-- 1 - user uuid
-- 2 - min level
-- 3 - max level
-- 4 - min age
-- 5 - max age
-- 6 - themes
-- 7 - failed_questions
-- 8 - completed_questions

WITH useruuid AS (
  SELECT %s AS uuid
), completed_questions AS (
  SELECT question_uuid AS uuid
  FROM app.questions_x_users
  WHERE user_uuid = (SELECT uuid FROM useruuid) AND completed = TRUE
), failed_questions AS (
  SELECT question_uuid AS uuid
  FROM app.questions_x_users
  WHERE user_uuid = (SELECT uuid FROM useruuid) AND completed = FALSE
), allowed_questions AS (
  SELECT uuid
  FROM app.questions
  WHERE level > %s AND level < %s AND
    age > %s AND age < %s AND
    theme = ANY(%s::TEXT[])
)
SELECT allowed_questions.uuid
FROM allowed_questions
LEFT JOIN failed_questions ON NOT %s = FALSE AND allowed_questions.uuid = failed_questions.uuid
LEFT JOIN completed_questions ON NOT %s = FALSE AND allowed_questions.uuid = completed_questions.uuid;


-- WITH useruuid AS (
--   SELECT 'uuid1' AS uuid
-- ), completed_questions AS (
--   SELECT question_uuid AS uuid
--   FROM app.questions_x_users
--   WHERE user_uuid = (SELECT uuid FROM useruuid) AND completed = TRUE
-- ), failed_questions AS (
--   SELECT question_uuid AS uuid
--   FROM app.questions_x_users
--   WHERE user_uuid = (SELECT uuid FROM useruuid) AND completed = FALSE
-- ), allowed_questions AS (
--   SELECT uuid
--   FROM app.questions
--   WHERE level > 0 AND level < 99 AND
--     age > 0 AND age < 99 AND
--     theme = ANY(ARRAY['uuid1']::TEXT[])
-- )
-- SELECT allowed_questions.uuid
-- FROM allowed_questions
-- LEFT JOIN failed_questions ON NOT TRUE = FALSE AND allowed_questions.uuid = failed_questions.uuid
-- LEFT JOIN completed_questions ON NOT TRUE = FALSE AND allowed_questions.uuid = completed_questions.uuid;