CREATE TABLE Clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    telefone VARCHAR(50),
    cargo VARCHAR(100),
    data DATE DEFAULT CURRENT_DATE
);

CREATE TABLE Administradores (
    id SERIAL PRIMARY KEY,
    matricula VARCHAR(255),
    senha VARCHAR(255)
);

