SELECT *,
ROW_NUMBER() OVER(ORDER BY stat DESC) as pos
FROM 
(
    SELECT
        ROUND((SUM(qxu.completed::INTEGER * level)::REAL / SUM(level) * 100)::DECIMAL)::INTEGER AS stat,
        user_uuid
    FROM
        questions_x_users as qxu
        INNER JOIN app.questions AS q ON qxu.question_uuid = q.uuid
    GROUP BY user_uuid
) as TMP;