# Llevame
Carpooling app for the final project in Holberton School

# Deploy development or production
To deploy a development or production environment, (after installing docker) follow the next steps:
- clone this repository.
- Inside the cloned repository run:
    - docker build -t python:llevame .
    - docker-compose up --no-start
    - docker-compose start
