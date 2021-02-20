#!/bin/bash

find logs -type f -name *.log -delete
docker-compose up --build --remove-orphans
