#!/bin/sh

files=$(find data/*)

echo '================================================================================'
echo 'load pg_normalized'
echo '================================================================================'

time echo "$files" | parallel python3 load_tweets.py --db=postgresql://hello_flask:hello_flask@localhost:10260/hello_flask_dev --inputs

