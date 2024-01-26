import tensorflow as tf
import onnx
import tf2onnx

model = tf.keras.models.load_model('./models/OW2cNoVal.keras')

onnx_model, _ = tf2onnx.convert.from_keras(model, opset=13)
onnx.save(onnx_model, "./models/OW2cNoVal.onnx")