FROM python:3.7-alpine3.11

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev bash
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib


WORKDIR /app
ADD    ./requirements.txt   /app/
RUN    pip install -r requirements.txt

COPY . /app/
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
