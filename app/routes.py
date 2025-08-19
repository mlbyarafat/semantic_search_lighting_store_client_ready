from flask import Blueprint, render_template, request, jsonify, current_app
from app.utils.search_engine import semantic_search

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json(force=True)
        query = data.get('query', '') if isinstance(data, dict) else ''
        current_app.logger.info(f"Search query received: {query}")
        if not query:
            return jsonify([])
        results = semantic_search(query, top_k=10)
        return jsonify(results)
    except Exception as e:
        current_app.logger.exception("Error handling /search request")
        return jsonify({"error": "Internal Server Error"}), 500
