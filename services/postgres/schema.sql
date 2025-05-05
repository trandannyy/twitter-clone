CREATE EXTENSION postgis;

\set ON_ERROR_STOP on

BEGIN;

-- TABLES

CREATE TABLE urls (
    id_urls BIGSERIAL PRIMARY KEY,
    url TEXT UNIQUE
);

CREATE TABLE users (
    id_users BIGINT PRIMARY KEY,
    id_urls BIGINT REFERENCES urls(id_urls),
    screen_name TEXT,
    password TEXT
);

CREATE TABLE tweets (
    id_tweets BIGINT PRIMARY KEY,
    id_users BIGINT,
    created_at TIMESTAMPTZ,
    text TEXT
);

-- INDEXES

-- index for username-password search
CREATE INDEX userpw_index ON users(screen_name, password);

COMMIT;
