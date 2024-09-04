import os
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import googleapiclient.discovery

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load Machine Learning Model
model = tf.keras.models.load_model('models/pollution_detection_model.h5')

# Google Maps and Earth Engine credentials
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
GOOGLE_EARTH_ENGINE_CREDENTIALS = os.getenv("GOOGLE_EARTH_ENGINE_CREDENTIALS")

# Setup Google Earth Engine API
def setup_earth_engine():
    credentials = service_account.Credentials.from_service_account_info(
        GOOGLE_EARTH_ENGINE_CREDENTIALS
    )
    earth_engine = googleapiclient.discovery.build(
        'earthengine', 'v1', credentials=credentials
    )
    return earth_engine

earth_engine = setup_earth_engine()

# Home Route
@app.route('/')
def home():
    return render_template('index.html', google_maps_api_key=GOOGLE_MAPS_API_KEY)

# Endpoint to receive satellite images and perform pollution detection
@app.route('/detect_pollution', methods=['POST'])
def detect_pollution():
    try:
        # Get the image data from the request (for example, URL to the satellite image)
        image_data = request.json['image_data']
        
        # Preprocess the image data (you would preprocess according to how your model was trained)
        processed_image = preprocess_image(image_data)
        
        # Make prediction using the model
        prediction = model.predict(np.array([processed_image]))

        # Return the pollution detection result
        return jsonify({'pollution_level': float(prediction[0][0])})
    except Exception as e:
        return jsonify({'error': str(e)})

def preprocess_image(image_data):
    # This function will handle preprocessing the image before passing it to the model
    # Example: resize, normalize, etc.
    return np.array(image_data)  # For now, returning image data directly

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
