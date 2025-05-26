from marshmallow import Schema, fields

class PlanSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    features = fields.Dict()
    duration_days = fields.Int(required=True)

class SubscriptionSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Str(required=True)
    plan_id = fields.Int(required=True)
    status = fields.Str()
    start_date = fields.DateTime()
    end_date = fields.DateTime()
