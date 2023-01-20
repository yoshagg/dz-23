from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD = ("filter", "map", "sort", "unique", "limit")

class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values):
        if values["cmd"] not in VALID_CMD:
            raise ValidationError("cmd contains invalid value")


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)

