SELECT
    ROUND((SUM(completed) / COUNT(*)) * 100, 2) AS stat,
    user_uuid,
    theme_uuid
FROM
    questions_x_users
    NATURAL JOIN questions
GROUP BY user_uuid, theme_uuid