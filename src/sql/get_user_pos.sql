SELECT *,
ROW_NUMBER() OVER(ORDER BY stat DESC) as pos
FROM 
(
    SELECT
        ROUND((SUM(qxu.completed::INTEGER * level)::REAL / SUM(level) * 100)::DECIMAL)::INTEGER AS stat,
        u.name
    FROM
        questions_x_users as qxu
        INNER JOIN app.questions AS q ON qxu.question_uuid = q.uuid
        INNER JOIN app.users AS u ON qxu.user_uuid = u.uuid
    WHERE user_uuid = %s
    GROUP BY user_uuid
) as TMP
WHERE user_uuid = %s;