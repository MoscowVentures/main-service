FROM python:3.9 as builder

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

FROM python:3.9-slim

RUN apt-get update \
  && apt-get -y install libpq-dev gcc

COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*