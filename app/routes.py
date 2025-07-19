from flask import Blueprint, render_template, request, jsonify
from .api import fetch_api_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/data', methods=['POST'])
def get_data():
    user_info = request.json
    result = fetch_api_data(user_info)
    return jsonify(result)
