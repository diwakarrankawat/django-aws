# syntax=docker/dockerfile:1
FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN mkdir /app/staticfiles
RUN pip3 install -r requirements.txt
COPY . /app/
EXPOSE 8080
CMD ["gunicorn", "gmaps_project.wsgi:application", "--bind", "0.0.0.0:8000"]
