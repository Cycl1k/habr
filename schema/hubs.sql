CREATE TABLE hubs(  
    id int NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    hubs_name VARCHAR(128),
    nubs_url VARCHAR(128)
);