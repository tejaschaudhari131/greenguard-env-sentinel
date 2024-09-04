import numpy as np
import base64
from PIL import Image
import io

def preprocess_image(image_data):
    """Convert base64 image data into a format suitable for prediction."""
    try:
        # Decode the base64 image
        image = Image.open(io.BytesIO(base64.b64decode(image_data)))

        # Resize image to the input shape required by the model (e.g., 128x128)
        image = image.resize((128, 128))

        # Convert image to numpy array and normalize it
        image_array = np.asarray(image) / 255.0

        return image_array
    except Exception as e:
        raise ValueError(f"Image preprocessing failed: {str(e)}")
