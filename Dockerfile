from python:3.9-slim


ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install flask gunicorn google-cloud-storage

ENV PORT 80

EXPOSE 80

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app1:app