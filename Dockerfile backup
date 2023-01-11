FROM python:3.9-alpine3.17
EXPOSE 8000
WORKDIR /site3/
COPY requirements.txt .
RUN apk update \
    && apk add gcc musl-dev mariadb-connector-c-dev
RUN pip3 install -r requirements.txt --no-cache-dir
RUN apk del gcc musl-dev

COPY ./site3/ .
COPY run.sh .
RUN chmod +x run.sh
CMD ./run.sh
