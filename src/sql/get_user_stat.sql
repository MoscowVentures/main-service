WITH user_questions(qu, uu, c) AS (
    SELECT question_uuid, user_uuid, completed
    FROM
        questions_x_users
    WHERE user_uuid = 'user_uuid1'
)
SELECT
    ROUND((SUM(c::INTEGER)::REAL / COUNT(*) * 100)::DECIMAL)::INTEGER AS stat,
    uu,
    theme_uuid
FROM
    user_questions
    INNER JOIN questions as q ON qu = q.uuid
GROUP BY uu, theme_uuid;