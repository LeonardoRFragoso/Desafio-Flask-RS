from flask import Blueprint, request, jsonify
from . import db
from .models import Refeicao

bp = Blueprint('routes', __name__)

@bp.route('/refeicoes', methods=['POST'])
def criar_refeicao():
    data = request.get_json()
    nova_refeicao = Refeicao(
        nome=data['nome'],
        descricao=data.get('descricao'),
        data_hora=datetime.fromisoformat(data['data_hora']),
        dentro_dieta=data['dentro_dieta']
    )
    db.session.add(nova_refeicao)
    db.session.commit()
    return jsonify({'id': nova_refeicao.id}), 201

@bp.route('/refeicoes/<int:id>', methods=['GET'])
def ver_refeicao(id):
    refeicao = Refeicao.query.get(id)
    if refeicao is None:
        return jsonify({'error': 'Refeição não encontrada'}), 404
    return jsonify({
        'id': refeicao.id,
        'nome': refeicao.nome,
        'descricao': refeicao.descricao,
        'data_hora': refeicao.data_hora.isoformat(),
        'dentro_dieta': refeicao.dentro_dieta
    })

@bp.route('/refeicoes/<int:id>', methods=['PUT'])
def editar_refeicao(id):
    data = request.get_json()
    refeicao = Refeicao.query.get(id)
    if refeicao is None:
        return jsonify({'error': 'Refeição não encontrada'}), 404

    refeicao.nome = data['nome']
    refeicao.descricao = data.get('descricao')
    refeicao.data_hora = datetime.fromisoformat(data['data_hora'])
    refeicao.dentro_dieta = data['dentro_dieta']

    db.session.commit()
    return jsonify({'message': 'Refeição atualizada'})

@bp.route('/refeicoes/<int:id>', methods=['DELETE'])
def apagar_refeicao(id):
    refeicao = Refeicao.query.get(id)
    if refeicao is None:
        return jsonify({'error': 'Refeição não encontrada'}), 404

    db.session.delete(refeicao)
    db.session.commit()
    return jsonify({'message': 'Refeição deletada'})

@bp.route('/refeicoes', methods=['GET'])
def listar_refeicoes():
    refeicoes = Refeicao.query.all()
    return jsonify([
        {
            'id': r.id,
            'nome': r.nome,
            'descricao': r.descricao,
            'data_hora': r.data_hora.isoformat(),
            'dentro_dieta': r.dentro_dieta
        }
        for r in refeicoes
    ])
