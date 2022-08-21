import tensorflow as tf
import numpy as np
from PIL import Image
import io

model = tf.keras.models.load_model('model')
# Get the input shape for the model layer
input_shape = model.layers[0].input_shape


def upload_transform(img):
    pil_image = Image.open(io.BytesIO(img))
    print(input_shape)
    # Resize image to expected input shape
    pil_image = pil_image.resize((input_shape[0][1], input_shape[0][2]))

    # Convert from RGBA to RGB *to avoid alpha channels*
    if pil_image.mode == 'RGBA':
        pil_image = pil_image.convert('RGB')

    # Convert image into grayscale *if expected*
    if input_shape[0][3] and input_shape[0][3] == 1:
        pil_image = pil_image.convert('L')

    # Convert image into numpy format
    numpy_image = np.array(pil_image).reshape((input_shape[0][1], input_shape[0][2], input_shape[0][3]))

    # Scale data (depending on your model)
    numpy_image = numpy_image / 255
    # Convert single image to a batch.
    image_array = np.array([numpy_image])

    return image_array


def makeprediction(img):

    img = upload_transform(img)

    pred = model.predict(img)
    prediction = np.argmax(pred[0])
    if prediction == 0:
        return {f'ANIMAL': 'CAT'}
    else:
        return {f'ANIMAL': 'DOG'}

