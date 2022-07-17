FROM python:3.10

ENV PATH="/scripts:${PATH}"

# install requirements 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# prepare dirs
WORKDIR /app
ADD . /app
COPY . /app

