import os

import flwr as fl
import tensorflow as tf

import hub
ds_train = hub.load('hub://activeloop/fer2013-public-test', read_only=True)
# ds_test = hub.load('hub://activeloop/fer2013-public-test',read_only=True)
# ds_pv = hub.load('hub://activeloop/fer2013-private-test')
# Make TensorFlow log less verbose
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# Load model and data (ResNet50, FER2013)
model = tf.keras.applications.resnet50.ResNet50(
    include_top=True,
    weights='imagenet',
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
)
dl_train = ds_train.tensorflow()
# dl_test = ds_pv.tensorflow()
print(ds_train)
# model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
# sklearn.model_selection.train_test_split()

# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# print(x_test)
# # Define Flower client
# class CifarClient(fl.client.NumPyClient):
#     def get_parameters(self):
#         return model.get_weights()

#     def fit(self, parameters, config):
#         model.set_weights(parameters)
#         model.fit(x_train, y_train, epochs=1, batch_size=32)
#         return model.get_weights(), len(x_train), {}

#     def evaluate(self, parameters, config):
#         model.set_weights(parameters)
#         loss, accuracy = model.evaluate(x_test, y_test)
#         return loss, len(x_test), {"accuracy": accuracy}


# # Start Flower client
# fl.client.start_numpy_client("[::]:8080", client=CifarClient())
