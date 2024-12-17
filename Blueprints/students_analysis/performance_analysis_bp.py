from flask import Blueprint, request, jsonify, render_template

bp_performance = Blueprint('bp_performance', __name__)

@bp_performance.route("/sleep_score_relationships", methods=["GET"])
def sleep_score_relationships():
    pass