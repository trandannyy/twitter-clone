#!/bin/sh

files='/data/tweets/geoTwitter21-01-03.zip
/data/tweets/geoTwitter21-01-04.zip'

echo '================================================================================'
echo 'load pg_normalized'
echo '================================================================================'

time echo "$files" | parallel python3 load_tweets.py --db=postgresql://hello_flask:hello_flask@localhost:10260/hello_flask_prod --inputs
