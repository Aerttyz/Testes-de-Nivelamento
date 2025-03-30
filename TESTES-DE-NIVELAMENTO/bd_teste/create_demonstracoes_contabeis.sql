CREATE TABLE demonstracoes_contabeis (
	id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    reg_ans VARCHAR(6) NOT NULL,
    cd_conta_contabil VARCHAR(15),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2)
);	