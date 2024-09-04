import os
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request, jsonify
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import googleapiclient.discovery
from utils.preprocess import preprocess_image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained machine learning model for pollution detection
MODEL_PATH = os.path.join('models', 'pollution_model.h5')
model = tf.keras.models.load_model(MODEL_PATH)

# Google Maps and Earth Engine API keys
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
GOOGLE_EARTH_ENGINE_CREDENTIALS = os.getenv("GOOGLE_EARTH_ENGINE_CREDENTIALS")

# Setup Google Earth Engine
def setup_earth_engine():
    try:
        credentials = service_account.Credentials.from_service_account_info(
            eval(GOOGLE_EARTH_ENGINE_CREDENTIALS)
        )
        earth_engine = googleapiclient.discovery.build('earthengine', 'v1', credentials=credentials)
        return earth_engine
    except Exception as e:
        print(f"Error setting up Earth Engine API: {e}")
        return None

earth_engine = setup_earth_engine()

# Home route
@app.route('/')
def index():
    return render_template('index.html', google_maps_api_key=GOOGLE_MAPS_API_KEY)

# API endpoint for pollution detection
@app.route('/api/detect_pollution', methods=['POST'])
def detect_pollution():
    try:
        # Retrieve base64 encoded image data
        image_data = request.json.get('image_data')
        if not image_data:
            return jsonify({'error': 'No image data provided'}), 400

        # Preprocess the image
        processed_image = preprocess_image(image_data)

        # Make predictions
        predictions = model.predict(np.array([processed_image]))
        pollution_level = float(predictions[0][0])

        # Return pollution level
        return jsonify({'pollution_level': pollution_level}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handler
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Page not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
