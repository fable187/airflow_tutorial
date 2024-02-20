#!/bin/bash

cassandra -R
# # Execute the CQL script to create the user
cqlsh -f /app/create_user.cql

# Keep the container running
tail -f /dev/null
