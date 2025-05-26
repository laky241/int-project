from flask import Blueprint, request, jsonify
from models import Plan, db
from schemas import PlanSchema

plans_bp = Blueprint('plans', __name__)
plan_schema = PlanSchema()
plans_schema = PlanSchema(many=True)

@plans_bp.route('', methods=['GET'])
def get_plans():
    plans = Plan.query.all()
    return jsonify(plans_schema.dump(plans)), 200

@plans_bp.route('', methods=['POST'])
def create_plan():
    data = plan_schema.load(request.get_json())
    plan = Plan(**data)
    db.session.add(plan)
    db.session.commit()
    return jsonify(plan_schema.dump(plan)), 201
