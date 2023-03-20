from flask import Blueprint,jsonify
from flask_login import login_required

api = Blueprint('api',__name__)


@api.route('/users')
@login_required
def api_users():
  return jsonify({
		"users": [
    {1: "Mark Wayne Menorca"}
		]
	})