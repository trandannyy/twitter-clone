CREATE EXTENSION postgis;
CREATE EXTENSION rum;

\set ON_ERROR_STOP on

BEGIN;

-- TABLES

CREATE TABLE urls (
    id_urls BIGSERIAL PRIMARY KEY,
    url TEXT UNIQUE
);

CREATE TABLE users (
    id_users BIGSERIAL PRIMARY KEY,
    id_urls BIGINT REFERENCES urls(id_urls),
    screen_name TEXT,
    password TEXT
);

CREATE TABLE tweets (
    id_tweets BIGSERIAL PRIMARY KEY,
    id_users BIGINT,
    created_at TIMESTAMPTZ,
    text TEXT
);

-- INDEXES

-- index for username-password search
CREATE INDEX userpw_index ON users(screen_name, password);

-- index for username lookup
CREATE INDEX username_index ON users(screen_name);

-- index for messages
CREATE INDEX created_at_index ON tweets(created_at);
CREATE INDEX tweet_user_index ON tweets(id_users);

-- index for FTS
CREATE INDEX fts_index ON tweets USING RUM(to_tsvector('english', text));

COMMIT;
