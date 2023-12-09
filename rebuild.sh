# bin/bash

sudo make stop
git pull
make start
psql -U your_username -d your_database_name -o /path/to/output.txt -f /path/to/script.sql