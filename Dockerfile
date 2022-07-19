FROM python:3.10


RUN apt-get update
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir -p /var/django/projects/dashboard
COPY . /var/django/projects/dashboard
WORKDIR /var/django/projects/dashboard

EXPOSE 8880

CMD ["bash", "./dashboard_start.sh"]