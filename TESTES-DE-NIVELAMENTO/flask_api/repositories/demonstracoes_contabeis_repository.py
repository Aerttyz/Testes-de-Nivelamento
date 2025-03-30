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
    
    