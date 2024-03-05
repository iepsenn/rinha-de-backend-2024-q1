CREATE TABLE transactions(
    id_client INTEGER REFERENCES clients,
    value INTEGER NOT NULL,
    type CHARACTER(1) NOT NULL,
    description CHARACTER(10),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
)