from django.apps import AppConfig
import os
import keras
import tensorflow
from django.conf import settings
from tensorflow.keras.models import model_from_json

class GestureConfig(AppConfig):
    name = 'gesture'
    path = os.path.join(settings.MODELS, "gesture_model1.h5")
