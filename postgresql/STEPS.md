sudo -u postgres psql
CREATE DATABASE alura;
\l

\c alura

CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    cpf CHAR(11),
    observacao TEXT,
    idade INTEGER,
    dinheiro NUMERIC(10,2),
    altura real,
    ativo BOOLEAN,
    data_nascimento DATE,
    hora_aula TIME,
    matricula timestamp
);

\dt
\d aluno

SELECT * FROM aluno;