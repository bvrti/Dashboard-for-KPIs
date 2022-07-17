FROM python:3.10

ENV PATH="/scripts:${PATH}"

# install requirements 
COPY ./requirements.txt /requirements.txt
RUN apt-get install
RUN pip install -r /requirements.txt

# prepare dirs
RUN mkdir /app
COPY ./* /app/
WORKDIR /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*

# add user to run the application
RUN adduser user
RUN chown -R user:user /app
RUN chmod -R 777 /app
USER user


CMD ["entrypoint.sh"]
