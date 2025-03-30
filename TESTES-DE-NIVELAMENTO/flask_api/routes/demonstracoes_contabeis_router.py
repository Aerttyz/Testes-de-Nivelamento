from services.demonstracoes_contabeis_service import DemonstracoesContabeisService
from flask import Blueprint, jsonify

demonstracoes_bp = Blueprint('demonstracoes', __name__)

@demonstracoes_bp.route('/demonstracoes_contabeis/reg_ans/<string:reg_ans>', methods=['GET'])
def get_demonstracoes_contabeis(reg_ans):
    try:
        demonstracoes = DemonstracoesContabeisService.get_by_reg_ans(reg_ans)
        if demonstracoes:
            return jsonify(demonstracoes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@demonstracoes_bp.route('/demonstracoes_contabeis/descricao/<string:descricao>', methods=['GET'])
def get_demonstracoes_contabeis_by_descricao(descricao):
    try:
        demonstracoes = DemonstracoesContabeisService.get_by_descricao(descricao)
        if demonstracoes:
            return jsonify(demonstracoes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@demonstracoes_bp.route('/demonstracoes_contabeis/relevance/<string:data>/<string:descricao>', methods=['GET'])
def get_demonstracoes_contabeis_by_relevance(data, descricao):
    try:
        demonstracoes = DemonstracoesContabeisService.get_by_relevance(data, descricao)
        print(f"Demonstracoes: {demonstracoes}")
        if demonstracoes:
            return jsonify(demonstracoes), 200
        else:
            return jsonify({"message": "No records found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500