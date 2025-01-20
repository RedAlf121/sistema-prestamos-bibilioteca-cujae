from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def prepare_train_and_test_data(model_input, model_output):
    return train_test_split(model_input,model_output, test_size=0.33, random_state=42)


def fit_model(model_class, model_input,model_output):
    input_train, input_test, output_train, output_test = prepare_train_and_test_data(model_input, model_output)
    model = model_class()
    model.fit(input_train,output_train)
    return model, input_test,output_test

def test_model(model, input_test, output_test):
    output_predicted = model.predict(input_test)
    return classification_report(output_test,output_predicted)

