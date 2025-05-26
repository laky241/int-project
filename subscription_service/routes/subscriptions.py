from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Subscription, Plan, db
from schemas import SubscriptionSchema
from datetime import datetime

subs_bp = Blueprint('subscriptions', __name__)
sub_schema = SubscriptionSchema()

@subs_bp.route('', methods=['POST'])
@jwt_required()
def create_sub():
    user = get_jwt_identity()
    data = request.get_json()
    plan = Plan.query.get_or_404(data['plan_id'])
    sub = Subscription(user_id=user, plan_id=plan.id)
    sub.update_end_date()
    db.session.add(sub)
    db.session.commit()
    return jsonify(sub_schema.dump(sub)), 201

@subs_bp.route('/<string:user_id>', methods=['GET'])
def get_sub(user_id):
    sub = Subscription.query.filter_by(user_id=user_id).first_or_404()
    return jsonify(sub_schema.dump(sub)), 200

@subs_bp.route('/<string:user_id>', methods=['PUT'])
@jwt_required()
def update_sub(user_id):
    sub = Subscription.query.filter_by(user_id=user_id).first_or_404()
    data = request.get_json()
    sub.plan_id = data.get('plan_id', sub.plan_id)
    sub.status = data.get('status', sub.status)
    sub.start_date = datetime.utcnow()
    sub.update_end_date()
    db.session.commit()
    return jsonify(sub_schema.dump(sub)), 200

@subs_bp.route('/<string:user_id>', methods=['DELETE'])
@jwt_required()
def cancel_sub(user_id):
    sub = Subscription.query.filter_by(user_id=user_id).first_or_404()
    sub.status = 'CANCELLED'
    db.session.commit()
    return jsonify(msg='Cancelled'), 200
