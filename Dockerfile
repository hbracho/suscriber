from python:alpine


# RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requeriments.txt /app/requeriments.txt

WORKDIR /app
# ENV HOST="localhost"
# ENV USER_NAME="training"
# ENV PORT="27017"
# ENV DATABASE_NAME="training"
# ENV PASSWORD="password"
# ENV AUTHSOURCE="training"
RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requeriments.txt \
  && apk del build-dependencies
#RUN pip install -r requeriments.txt

COPY . /app
EXPOSE 80
ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
