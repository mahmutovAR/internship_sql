#!/bin/bash

source .env



docker run -d \
    --name $PGSQL_PROJECT_NAME \
    -p $PGSQL_DATABASE_PORT:$PGSQL_DATABASE_PORT \
    -e POSTGRES_USER=$PGSQL_DATABASE_USER \
    -e POSTGRES_PASSWORD=$PGSQL_DATABASE_PASSWORD \
    -e POSTGRES_DB=$PGSQL_DATABASE_NAME \
    postgres:16.4-bookworm

