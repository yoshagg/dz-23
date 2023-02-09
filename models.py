from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD = ("filter", "map", "sort", "unique", "limit")


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
