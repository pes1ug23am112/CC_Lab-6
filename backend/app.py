from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os
import threading

app = Flask(__name__)
CORS(app)

# In-memory data storage with thread safety
data_store = []
request_count = 0
data_lock = threading.Lock()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    global request_count
    with data_lock:
        request_count += 1
    return jsonify({
        'status': 'healthy',
        'service': 'backend-api',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/data', methods=['GET'])
def get_data():
    """Retrieve all data"""
    global request_count
    with data_lock:
        request_count += 1
        data_copy = list(data_store)
    return jsonify({
        'success': True,
        'data': data_copy,
        'count': len(data_copy)
    })

@app.route('/api/data', methods=['POST'])
def create_data():
    """Create new data entry"""
    global request_count
    
    try:
        with data_lock:
            request_count += 1
            
        content = request.get_json()
        if not content:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        with data_lock:
            entry = {
                'id': len(data_store) + 1,
                'content': content.get('content', ''),
                'timestamp': datetime.now().isoformat()
            }
            data_store.append(entry)
        
        return jsonify({
            'success': True,
            'data': entry,
            'message': 'Data created successfully'
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    """Retrieve specific data by ID"""
    global request_count
    with data_lock:
        request_count += 1
        data_copy = list(data_store)
    
    for item in data_copy:
        if item['id'] == data_id:
            return jsonify({
                'success': True,
                'data': item
            })
    
    return jsonify({
        'success': False,
        'error': 'Data not found'
    }), 404

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get service statistics"""
    global request_count
    with data_lock:
        request_count += 1
        total_entries = len(data_store)
        total_reqs = request_count
    
    return jsonify({
        'success': True,
        'stats': {
            'total_requests': total_reqs,
            'total_entries': total_entries,
            'service_uptime': 'running',
            'timestamp': datetime.now().isoformat()
        }
    })

@app.route('/', methods=['GET'])
def root():
    """Root endpoint"""
    return jsonify({
        'service': 'Backend API Service',
        'version': '1.0.0',
        'endpoints': [
            '/api/health',
            '/api/data',
            '/api/stats'
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
