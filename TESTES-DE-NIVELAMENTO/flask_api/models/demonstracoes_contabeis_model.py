from database import db

class DemonstracoesContabeisModel(db.Model):
    __tablename__ = 'demonstracoes_contabeis'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=True)
    reg_ans = db.Column(db.String(6), nullable=False, name="reg_ans")
    cd_conta_contabil = db.Column(db.String(15), nullable=True)
    descricao = db.Column(db.String(255), nullable=True)
    vl_saldo_final = db.Column(db.Numeric(15, 2), nullable=True)
    vl_saldo_inicial = db.Column(db.Numeric(15, 2), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "data": self.data.strftime('%Y-%m-%d') if self.data else None, 
            "reg_ans": self.reg_ans,
            "cd_conta_contabil": self.cd_conta_contabil,
            "descricao": self.descricao,
            "vl_saldo_final": float(self.vl_saldo_final) if self.vl_saldo_final else None,  
            "vl_saldo_inicial": float(self.vl_saldo_inicial) if self.vl_saldo_inicial else None
        }
    