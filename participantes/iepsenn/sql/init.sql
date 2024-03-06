CREATE TABLE clients (
    id INTEGER PRIMARY KEY, 
    limit_value INTEGER NOT NULL, 
    opening_balance INTEGER NOT NULL
);
CREATE INDEX clients_id ON clients (id);

CREATE TABLE transactions (
    id_client INTEGER NOT NULL,
    value INTEGER NOT NULL,
    type VARCHAR(1) NOT NULL,
    description VARCHAR(10),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT "clients_fk" FOREIGN KEY ("id_client") REFERENCES clients ("id"),
    UNIQUE (id_client, timestamp)
);

INSERT INTO clients (id, limit_value, opening_balance)
VALUES
	(1, 100000, 0),
    (2, 80000, 0),
    (3, 1000000, 0),
    (4, 10000000, 0),
    (5, 500000, 0);
