CREATE TABLE demonstracoes_contabeis (
	data DATE,
    reg_ans VARCHAR(6) NOT NULL,
    cd_conta_contabil VARCHAR(15),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2)
);	