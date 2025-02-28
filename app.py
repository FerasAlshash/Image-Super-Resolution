from flask import Flask, request, jsonify, send_file, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__, template_folder='templates')

# Load the pre-trained model with the updated name
model = load_model('enhanced_sequential_sr_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enhance', methods=['POST'])
def enhance_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Convert the file to a BytesIO object
        img_bytes = file.read()
        img_io = BytesIO(img_bytes)

        # Load and preprocess the image
        img = load_img(img_io, target_size=(200, 300))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Perform image enhancement
        enhanced_img_array = model.predict(img_array)
        enhanced_img = enhanced_img_array[0] * 255.0
        enhanced_img = enhanced_img.astype(np.uint8)
        enhanced_img = Image.fromarray(enhanced_img)

        # Save the enhanced image to a bytes buffer
        enhanced_img_io = BytesIO()
        enhanced_img.save(enhanced_img_io, 'JPEG')
        enhanced_img_io.seek(0)

        return send_file(enhanced_img_io, mimetype='image/jpeg', download_name='enhanced_image.jpg')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)