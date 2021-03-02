import tensorflow as tf
import tensorflow_hub as hub

from tensorflow.keras import layers
from tensorflow.keras.applications import EfficientNetB7


if __name__ == '__main__':
    # model = hub.KerasLayer("https://tfhub.dev/google/nnlm-en-dim128/2")
    # embeddings = model(["The rain in Spain.", "falls",
    #                     "mainly", "In the plain!"])

    # print(embeddings.shape)
    print('GPU usable: ', tf.test.is_gpu_available())

    exit()

    model = EfficientNetB7(
        include_top=True,
        weights='imagenet',
        input_shape=None,
        pooling=None,
        classes=1000,
        classifier_activation="softmax"
    )

    print(model.summary())