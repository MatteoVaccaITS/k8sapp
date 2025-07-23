from flask import Flask, jsonify      # Import Flask and jsonify for API responses
from flask_cors import CORS           # Import CORS to allow cross-origin requests

app = Flask(__name__)                 # Create Flask application instance
CORS(app)                             # Enable CORS for all routes

@app.route('/api/hello')              # Define route for GET requests to /api/hello
def hello():
    # Return a JSON response with a greeting message
    return jsonify({ "message": "Hello from Python backend!" })

if __name__ == '__main__':
    # Run the Flask app on all network interfaces, port 5000
    app.run(host='0.0.0.0', port=5000)