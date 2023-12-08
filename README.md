
## How to run all in docker

### Postgres
```bash
docker run --name bot_postgres \
  -e POSTGRES_PASSWORD=KbZ72URs2AkRLCza8Ru9 \
  -e POSTGRES_USER=bot \
  -e POSTGRES_DB=bot_db \
  -v ~/bot/data/postgres:/var/lib/postgresql/data \
  -p 20000:5432 -d postgres:15
```

### Redis
```bash
docker run -d --name bot_redis \
  -v ~/bot/data/redis:/data \
  -p 20001:6379 \
  -d redis:3.2 redis-server --appendonly yes \
  --requirepass "eWvmwkLYmWa719sW23P1"
```