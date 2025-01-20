from sklearn.calibration import LabelEncoder


def numerize_data(df):
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    return df,label_encoders


def apply_encoder(df,encoder):
    for column, le in encoder.items():
        df[column] = le.transform(df[column])
    return df