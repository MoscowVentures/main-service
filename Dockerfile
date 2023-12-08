FROM app-base-img

WORKDIR /app

RUN mkdir -p src
RUN mkdir -p src/sql
RUN mkdir -p log

COPY src/* ./src/
COPY src/sql/* ./src/sql/

CMD python3 src/mainloop.py