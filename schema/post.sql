CREATE TABLE posts(  
    id int NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    post_id int,
    title VARCHAR(128),
    post_date TIMESTAMP,
    post_url VARCHAR(128),
    author_name VARCHAR(128),
    author_url VARCHAR(128)
);