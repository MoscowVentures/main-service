FROM app-base-img

WORKDIR /app

RUN mkdir -p src
RUN mkdir -p log

COPY src/ ./src/

CMD python3 src/mainloop.py