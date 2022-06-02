from flask import Blueprint, request, jsonify
from app.scrap import get_playlist_videos

index_bp = Blueprint('index_bp', __name__)

@index_bp.post('/')
def index():
    try:
        url = request.json.get('url')
        if not url:
            return jsonify({'error': 'Url not provided.'}), 401
        return jsonify(get_playlist_videos(url)), 200
    except Exception as e:
            return jsonify({'error': 'Internal error.'}), 500