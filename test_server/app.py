from flask import Flask, request, jsonify
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/api/product-action', methods=['POST'])
def product_action():
    """
    Test endpoint to receive product action requests
    """
    try:
        data = request.get_json()
        
        # Log the received data
        logger.info("Received product action request:")
        logger.info(f"Product ID: {data.get('product_id')}")
        logger.info(f"Product Name: {data.get('product_name')}")
        logger.info(f"Timestamp: {data.get('timestamp')}")
        logger.info(f"User: {data.get('user')}")
        logger.info(f"Headers: {dict(request.headers)}")
        
        # Return a success response
        return jsonify({
            'status': 'success',
            'message': f'Received action for product {data.get("product_id")}',
            'received_at': datetime.utcnow().isoformat(),
            'data': data
        })
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    logger.info("Starting test server on http://0.0.0.0:8000")
    # Allow access from any host and disable debug mode for security
    app.run(host='0.0.0.0', port=8000, debug=False)
