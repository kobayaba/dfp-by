FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

WORKDIR /home/by/projects/dfp/

COPY Pipfile Pipfile.lock /home/by/projects/dfp/
RUN pip install pipenv && pipenv install --system

COPY . /home/by/projects/dfp/