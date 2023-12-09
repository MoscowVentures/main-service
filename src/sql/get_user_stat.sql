WITH user_questions(qu, uu, c) AS (
    SELECT question_uuid, user_uuid, completed
    FROM
        questions_x_users
    WHERE user_uuid = %s
)
SELECT
    ROUND((SUM(c::INTEGER * level)::REAL / SUM(level) * 100)::DECIMAL)::INTEGER AS stat,
    uu,
    theme_uuid,
    app.themes.title
FROM
    user_questions
    INNER JOIN app.questions AS q ON qu = q.uuid
    INNER JOIN app.themes ON theme_uuid = app.themes.uuid
GROUP BY uu, theme_uuid, app.themes.title;