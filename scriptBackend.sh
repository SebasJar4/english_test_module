#!/bin/bash

my_docker.sh on

echo \t !!!!! Status \n

my_docker.sh status

docker compose --profile backend_develop up

docker compose ps 

sleep 2

docker compose exec backend_develop sh