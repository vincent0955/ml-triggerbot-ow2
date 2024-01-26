import keyboard
import tensorflow as tf
import numpy as np
import PIL
import PIL.Image
import matplotlib.pyplot as plt
import pyautogui
import dxcam
from PIL import Image
import time
import onnxruntime as ort

x1 = 946 # equal to 1920/2-14
x2 = 974 # equal to 1920/2+14
y1 = 526 # equal to 1080/2-14
y2 = 554 # equal to 1080/2+14

model_path = './models/OW2cNoVal.onnx'

session = ort.InferenceSession(model_path)

camera = dxcam.create()

def onnx_1frame_test():
    frame = camera.grab(region=(x1, y1, x2, y2))
    img_array = tf.keras.utils.img_to_array(frame)
    img_array = tf.expand_dims(img_array, 0)
    input = np.reshape(img_array, [1, 28, 28, 3])
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: input})[0]
    print(outputs[0][0])

# onnx_1frame_test()
    
def keras_1frame_test():
    model = tf.keras.models.load_model('./models/OW2a.keras')
    frame = camera.grab(region=(x1, y1, x2, y2))
    img_array = tf.keras.utils.img_to_array(frame)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    print(predictions[0][0])

# keras_1frame_test() # 0.15370327



while True:
    frame = camera.grab(region=(x1, y1, x2, y2))  # alternative to pyscreenshot ImageGrab
    try:
        img_array = tf.keras.utils.img_to_array(frame)
        img_array = tf.expand_dims(img_array, 0)
        input = np.reshape(img_array, [1, 28, 28, 3])
        input_name = session.get_inputs()[0].name
        outputs = session.run(None, {input_name: input})[0]
        print(outputs[0][0])
        if outputs[0][0] > 0.94:
            pyautogui.click()
            print('CLICK')

            # screenshot
            # im = Image.fromarray(frame)
            # save_path = "./trainingshots/" + str(time.time()) + ".png"
            # im.save(save_path)
        else:
            print("NO CLICK")
    except: 
        continue
    time.sleep(0.001)