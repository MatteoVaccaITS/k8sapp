# Import Flask and jsonify for API responses
from flask import Flask, jsonify
# Import CORS to allow cross-origin requests
from flask_cors import CORS

# Create Flask application instance
app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

# Define route for GET requests to /api/hello
@app.route('/api/hello')
def hello():
    # Return a JSON response with a greeting message
    return jsonify({ "message": "Hello from Python backend!" })

if __name__ == '__main__':
    # Run the Flask app on all network interfaces, port 5000
    app.run(host='0.0.0.0', port=5000)