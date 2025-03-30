from models.demonstracoes_contabeis_model import DemonstracoesContabeisModel
from database import db
from sqlalchemy import text

class DemonstracoesContabeis(db.Model):
    
    @staticmethod
    def get_by_reg_ans(reg_ans):
        return DemonstracoesContabeisModel.query.filter_by(reg_ans=reg_ans).all()
    
    @staticmethod
    def get_by_descricao(descricao):
        return DemonstracoesContabeisModel.query.filter(DemonstracoesContabeisModel.descricao.like(f'%{descricao}%')).all()
    
    @staticmethod
    def get_by_relevance(data, descricao):
        sql_query = """ 
        SELECT *, 
       (vl_saldo_final * 100) - (vl_saldo_inicial * 100) AS diff 
        FROM teste.demonstracoes_contabeis 
        WHERE data = :data 
        AND descricao LIKE :descricao
        ORDER BY diff ASC
        LIMIT 10; 
        """

        result = db.session.execute(text(sql_query), {"data": data, "descricao": f"%{descricao}%"})
        columns = result.keys()
        rows = result.fetchall()
        result_dicts = [dict(zip(columns, row)) for row in rows]  
        print(f"Resultados encontrados: {result_dicts}")
        return result_dicts