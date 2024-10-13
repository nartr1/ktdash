#! /bin/bash

if [ $SEED_DB == "True" ]; then
echo "Seeding database..."
mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -D$DB_NAME < /dataseeding.sql
fi