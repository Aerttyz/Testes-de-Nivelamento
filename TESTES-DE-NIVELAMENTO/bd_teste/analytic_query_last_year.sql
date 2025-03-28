SELECT *,
		(vl_saldo_final * 100) - (vl_saldo_inicial * 100) AS diff 
FROM teste.demonstracoes_contabeis 
WHERE YEAR(data) = 2024
AND descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' 
ORDER BY diff ASC
LIMIT 10;