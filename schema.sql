
CREATE TABLE Users (
  id          SERIAL PRIMARY KEY,
  name        TEXT NOT NULL,
  password    TEXT NOT NULL,
  email       TEXT UNIQUE NOT NULL
);

-- we will at least need to add sessions and question tables