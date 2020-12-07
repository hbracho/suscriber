from python:alpine

#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requeriments.txt /app/requeriments.txt

WORKDIR /app
ENV HOST="localhost"
ENV USER_NAME="training"
ENV PORT="27017"
ENV DATABASE="training"
ENV PASSWORD="password"
ENV AUTHSOURCE="training"

RUN pip install -r requeriments.txt

COPY . /app
EXPOSE 80
ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
