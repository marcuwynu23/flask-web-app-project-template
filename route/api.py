from flask import Blueprint,jsonify


api = Blueprint('api',__name__)


@api.route('/users')
def api_users():
  return jsonify({
		"users": [
    {1: "Mark Wayne Menorca"}
		]
	})