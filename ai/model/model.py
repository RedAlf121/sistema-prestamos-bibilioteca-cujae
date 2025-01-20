from dataclasses import dataclass
import os
import joblib
import pandas as pd
from . import MODEL_PATH, ENCODER_PATH

@dataclass
class PredictionInput:
    Numero_Prestamos_Anteriores: int
    Solicitudes_No_Satisfechas: int
    Numero_Renovaciones: int
    Disponibilidad_Actual: int
    Categoria_Libro: str

    def to_dataframe(self):
        return pd.DataFrame([{
            'Numero_Prestamos_Anteriores': self.Numero_Prestamos_Anteriores,
            'Solicitudes_No_Satisfechas': self.Solicitudes_No_Satisfechas,
            'Numero_Renovaciones': self.Numero_Renovaciones,
            'Disponibilidad_Actual': self.Disponibilidad_Actual,
            'Categoria_Libro': self.Categoria_Libro
        }])


def save_object(obj, file_path):
    return joblib.dump(obj, file_path)

def load_object(file_path):
    return joblib.load(file_path)

def save_model(model):
    return save_object(model,MODEL_PATH)

def load_model():
    return load_object(MODEL_PATH)

def save_encoders(encoder):
    return save_object(encoder,ENCODER_PATH)

def load_model():
    return load_object(MODEL_PATH)

def load_encoders():
    return load_object(ENCODER_PATH)

