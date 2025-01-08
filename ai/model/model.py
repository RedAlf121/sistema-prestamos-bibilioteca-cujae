import joblib
from ai.model import MODEL_PATH


def save_model(model):
    return joblib.dump(model,MODEL_PATH)

def load_model():
    return joblib.load(MODEL_PATH)