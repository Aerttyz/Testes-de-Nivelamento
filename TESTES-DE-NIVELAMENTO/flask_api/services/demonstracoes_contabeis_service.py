from repositories.demonstracoes_contabeis_repository import DemonstracoesContabeis

class DemonstracoesContabeisService:
    @staticmethod
    def get_by_reg_ans(reg_ans):
        
        operators = DemonstracoesContabeis.get_by_reg_ans(reg_ans)
        if operators:
            return [op.to_dict() for op in operators]  
        return None 
    @staticmethod
    def get_by_descricao(descricao):
        
        operators = DemonstracoesContabeis.get_by_descricao(descricao)
        if operators:
            return [op.to_dict() for op in operators]  
        return None
   
    
    