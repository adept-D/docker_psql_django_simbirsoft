# docker_psql_django_simbirsoft

Стек: Django, PostgreSQL


# Deploy

## Setup
  ### build and up containers
  `cd app`  
  `docker-compose up`
  ### create superuser for admin
  `docker-compose run web python manage.py createsuperuser`
