FROM python:3.9-slim

RUN apt-get update && apt-get clean && apt-get -y install libpq-dev

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt

RUN ["chmod", "+x", "entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]