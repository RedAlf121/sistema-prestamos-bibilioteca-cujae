from dataclasses import dataclass
import pandas as pd

from model.model import PredictionInput, load_encoders
from train.preprocess_functions import apply_encoder


def predict(input: PredictionInput, model):
    encoder = load_encoders()
    encoded_dataframe = apply_encoder(input.to_dataframe(), encoder)
    return model.predict(encoded_dataframe)