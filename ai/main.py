from sklearn.tree import DecisionTreeClassifier
from train.preprocess_functions import numerize_data
from model.model import save_model,save_encoders,PredictionInput
from model.view import predict
from train.model_trainer import fit_model,test_model
import pandas as pd
from train import TRAINING_FILE_PATH


def load_data(preprocess_function):
    df = pd.read_csv(TRAINING_FILE_PATH)
    df,encoders = preprocess_function(df)
    model_input = df.iloc[:,:-1]
    model_output = df.iloc[:,-1]
    save_encoders(encoders)
    return model_input,model_output

if __name__ == '__main__':
    model_input, model_output = load_data(numerize_data)
    model,input,output = fit_model(DecisionTreeClassifier,model_input,model_output)
    print(test_model(model,input,output))
    save_model(model)
    input_test = PredictionInput(Numero_Prestamos_Anteriores=12,Solicitudes_No_Satisfechas=3,Numero_Renovaciones=2,Disponibilidad_Actual=5,Categoria_Libro='Ficción')
    print(predict(input_test,model))