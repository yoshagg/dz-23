from flask import Blueprint, request, jsonify

from builder import query_builder

from models import BatchRequestParams

from marshmallow import ValidationError


main_bp = Blueprint("main", __name__)


@main_bp.route("/perform_query", methods=["POST"])
def perform_query():
    try:
        params = BatchRequestParams().load(data=request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400
    result = None
    for query in params['queries']:
        result = query_builder(
            cmd=query["cmd"],
            value=query["value"],
            data=result
        )

    return jsonify(result)
