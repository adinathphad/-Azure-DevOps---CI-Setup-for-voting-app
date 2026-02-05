-- Runs automatically when Postgres container starts first time

CREATE TABLE IF NOT EXISTS votes(
    id SERIAL PRIMARY KEY,
    choice TEXT
);
