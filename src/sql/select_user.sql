SELECT uuid, name, created_at 
FROM app.users
WHERE phone = $1;