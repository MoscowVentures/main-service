# bin/bash

sudo make stop
git pull
make start
psql "postgresql://app:Password12345@localhost:20011/app_db" -f ./gpt_data/testdata.sql