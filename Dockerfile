# syntax=docker/dockerfile:1

FROM nginx:alpine
RUN apk add python3
RUN apk add py3-pip

# FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN mkdir /app/staticfiles
RUN pip3 install -r requirements.txt
COPY . /app/
RUN python3 manage.py makemigrations && python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput
EXPOSE 8000
EXPOSE 80
# RUN apk add nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
CMD nginx && gunicorn --workers=3 --threads=3 gmaps_project.wsgi:application --bind unix:/app/guni.sock
