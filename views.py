from flask import Blueprint, request, Response, jsonify

from builder import query_builder

from app import main
from models import RequestParams, BatchRequestParams

from marshmallow import ValidationError


main_bp = Blueprint("main", __name__)


@main_bp.route("/perform_query", methods=["POST"])
def perform_query() -> Response:
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    data = request.json
    try:
        RequestParams().load(data=data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    return jsonify(query_builder(data["cmd"], data["value"]))
