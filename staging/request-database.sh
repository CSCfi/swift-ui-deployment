#!/bin/bash
set -e

# The script expects the database to have a readily created user called
# sharing, and a database called swiftsharing with rights the user
# sharing set as the owner.

psql -v ON_ERROR_STOP=1 --username "sharing" --dbname "swiftsharing" <<-EOSQL
    CREATE TABLE IF NOT EXISTS Shares(
        container TEXT,
        container_owner TEXT,
        recipient TEXT,
        r_read BOOL,
        r_write BOOL,
        sharingdate TIMESTAMP,
        address TEXT           NOT NULL,
        PRIMARY KEY(container, container_owner, recipient)
    );
    CREATE TABLE IF NOT EXISTS Tokens(
        token_owner TEXT,
        token TEXT,
        identifier TEXT,
        PRIMARY KEY(token_owner, identifier)
    );
EOSQL
