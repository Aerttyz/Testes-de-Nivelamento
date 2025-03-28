
CREATE TABLE relatorio_cadop (
	registro_ans VARCHAR(6) NOT NULL UNIQUE,
    cnpj VARCHAR(14) NOT NULL UNIQUE,
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(255),
    logradouro VARCHAR(255),
    numero VARCHAR(25),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cidade VARCHAR(255),
    uf CHAR(2),
    cep VARCHAR(8),
    ddd CHAR(2),
    telefone VARCHAR(25),
    fax VARCHAR(25),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao CHAR(1),
    data_registro_ans DATE
);


