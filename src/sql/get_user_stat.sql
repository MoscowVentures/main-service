SELECT
    ROUND((SUM(completed::INTEGER) / COUNT(*)) * 100, 2) AS stat,
    user_uuid,
    theme_uuid
FROM
    questions_x_users
    NATURAL JOIN questions
WHERE user_uuid = %s
GROUP BY user_uuid, theme_uuid