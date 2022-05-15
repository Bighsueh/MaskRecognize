from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
#比對預測分數，並輸出預測結果
def compare_with_result(prediction):
    result = ''
    if prediction[0] < prediction[1]:
        result = '沒戴口罩'
    else:
        result = '有戴口罩'
    return result
def image_recog(image_path):
    # Load the model
    model = load_model('keras_model.h5')

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(image_path)
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    result = compare_with_result(prediction[0])

    print(result)
    print(prediction)
    return result

