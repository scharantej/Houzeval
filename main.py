
# Import required libraries
from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
import os
import requests
import json
import re
from PIL import Image
import numpy as np
import tensorflow as tf

# Set up the Flask application
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the address validation route
@app.route('/validate_address', methods=['POST'])
def validate_address():
    address = request.form['address']

    # Use Google Maps API to validate the address
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={os.getenv("GOOGLE_MAPS_API_KEY")}'
    response = requests.get(url)
    data = json.loads(response.text)

    # Check if the address is valid
    if data['status'] == 'OK':
        return 'success'
    else:
        return 'error'

# Define the photo upload route
@app.route('/upload_photos', methods=['POST'])
def upload_photos():
    # Get the uploaded photos
    interior_photo = request.files['interior_photo']
    exterior_photo = request.files['exterior_photo']

    # Save the photos to the server
    interior_photo_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(interior_photo.filename))
    exterior_photo_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(exterior_photo.filename))
    interior_photo.save(interior_photo_path)
    exterior_photo.save(exterior_photo_path)

    # Resize and preprocess the photos
    interior_photo = Image.open(interior_photo_path)
    interior_photo = interior_photo.resize((224, 224))
    interior_photo = np.array(interior_photo) / 255.0
    exterior_photo = Image.open(exterior_photo_path)
    exterior_photo = exterior_photo.resize((224, 224))
    exterior_photo = np.array(exterior_photo) / 255.0

    # Predict the estimated value of the property
    model = tf.keras.models.load_model('model.h5')
    prediction = model.predict([interior_photo, exterior_photo])

    # Round the estimated value to the nearest thousand
    estimated_value = round(prediction[0][0] * 1000)

    # Return the estimated value
    return str(estimated_value)

# Define the main function
if __name__ == '__main__':
    app.run(debug=True)
