LOAD DATA INFILE 'caminho/para/arquivo.csv'
INTO TABLE demonstracoes_contabeis
FIELDS terminated by ';'
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 ROWS
(data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    -- Alguns arquivos CSV contém a data em formato diferente
    -- data = STR_TO_DATE(@data, '%d/%m/%Y'),
	vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',','.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',','.');
;
