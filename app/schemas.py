from marshmallow import Schema, fields


class ExerciseSummarySchema(Schema):
    """Schema representing contractual presentation/validation of ExerciseSummary data."""

    id = fields.Int(dump_only=True)
    created_at = fields.DateTime()
    subject = fields.Str()
