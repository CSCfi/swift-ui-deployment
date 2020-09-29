#!/bin/bash
set -e

# The script expects the database to have a readily created user called
# request, and a database called swiftrequest with rights the user
# request set as the owner.

psql -v ON_ERROR_STOP=1 --username "request" --dbname "swiftrequest" <<-EOSQL
    CREATE TABLE IF NOT EXISTS Requests(
        container TEXT,
        container_owner TEXT,
        recipient TEXT,
        created TIMESTAMP,
        PRIMARY KEY(container, container_owner, recipient)
    );
    CREATE TABLE IF NOT EXISTS Tokens(
        token_owner TEXT,
        token TEXT,
        identifier TEXT,
        PRIMARY KEY(token_owner, identifier)
    );
EOSQL
