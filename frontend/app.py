from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Backend service URL
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5001')

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/proxy/health', methods=['GET'])
def proxy_health():
    """Proxy health check to backend"""
    try:
        response = requests.get(f'{BACKEND_URL}/api/health', timeout=5)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Backend service unavailable: {str(e)}'
        }), 503

@app.route('/api/proxy/data', methods=['GET'])
def proxy_get_data():
    """Proxy get data request to backend"""
    try:
        response = requests.get(f'{BACKEND_URL}/api/data', timeout=5)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Backend service unavailable: {str(e)}'
        }), 503

@app.route('/api/proxy/data', methods=['POST'])
def proxy_create_data():
    """Proxy create data request to backend"""
    try:
        data = request.get_json()
        response = requests.post(f'{BACKEND_URL}/api/data', json=data, timeout=5)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Backend service unavailable: {str(e)}'
        }), 503

@app.route('/api/proxy/stats', methods=['GET'])
def proxy_stats():
    """Proxy stats request to backend"""
    try:
        response = requests.get(f'{BACKEND_URL}/api/stats', timeout=5)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Backend service unavailable: {str(e)}'
        }), 503

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
