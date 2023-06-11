FROM ubuntu:22.04

# start from an official image
FROM python:3.10.2-slim-bullseye


ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/
RUN pip install pipenv && pipenv install --system

# copy our project code
COPY . /opt/services/djangoapp/src
RUN pip install django-prometheus
RUN pip install psycopg2-binary


RUN cd demo && python3 manage.py collectstatic --no-input -v 2


# expose the port 8000
EXPOSE 80

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "demo", "--bind", ":80", "demo.wsgi:application"]