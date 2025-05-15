# twitter-clone
[![](https://github.com/trandannyy/twitter-clone/actions/workflows/main.yml/badge.svg)](https://github.com/trandannyy/twitter-clone/actions/workflows/main.yml)

# Overview

This repo utilizes the Instagram tech stack in order to create a CRUD (Create, Read, Update, Destroy) website inspired by  Twitter. 

**Tech Stack Description**

- Python
- HTML/CSS
- Flask
- PostgreSQL
- Docker
- Nginx
- Gunicorn

# Features

This project has six pages with different functionaltiy.

**Home**

This page displays all messages in the system, 20 messages per page.

**Login**

This page is a login system which stores cookies to log a user in.

**Logout**

This page deletes cookies to log a user out.

**Create User**

This page allows for the creation of a new user. It requires a user to type their password in twice.

**Create Message**

This page allows a user to create a message. It requires that a user is logged in.

**Search**

This page takes user input and searches for the input in the tweets in the database (similar to Ctrl-F). This page uses a RUM index to speed up the full-text search (FTS).

# How to Use

To bring this website up on your computer, ensure that portforwarding is enabled for the respective ports (development or production).

Here are the commands to bring the containers:

For the development container:

```
$ docker compose up -d --build
```

For the production container:

```
$ docker compose -f docker-compose.prod.yml up -d --build
```

Now that the containers are up, we can load the data in using one of the two following scripts:

- `load_tweets_parallel.sh`
- `load_tweets_large.sh`

The `load_tweets_parallel.sh` script will load in a small amount of test data (on the order of thousands). On the other hand, the `load_tweets_large.sh` script will load in a large amount of data (on the order of millions).

To load the data in, we can run the following in the terminal:

```
$ bash load_tweets_parallel.sh
```

OR

```
$ bash load_tweets_large.sh
```

Note that you will have to create a file named `.env.prod` file that is similar to `.env.dev` and a file named `.env.prod.db` with `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` defined.

Once the data is loaded in, you are ready to view the website. Using a search engine of your choice, go to "localhost:YOURPORT" and test out the website!

If you would like to bring down the containers, you can run these commands (depending on which docker-compose file you are using:

```
$ docker compose down
```

OR

```
$ docker compose -f docker-compose.prod.yml down
```

*Note that bringing the containers down does not delete the data because they are stored in the volumes. To also delete the data, simply add* `-v` *to the end of the command you use.*
