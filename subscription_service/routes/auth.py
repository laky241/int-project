from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # dummy check
    if data.get('username') == 'user' and data.get('password') == 'pass':
        token = create_access_token(identity=data['username'])
        return jsonify(access_token=token), 200
    return jsonify(msg='Bad credentials'), 401
