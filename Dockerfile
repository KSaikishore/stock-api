FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN apt-get -q update && apt-get -qy install netcat
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh
COPY ./wait-for-django.sh  /wait-for-django.sh
RUN chmod +x /wait-for-django.sh
# ENTRYPOINT ["/docker-entrypoint.sh"]