import pickle
import pandas as pd
import json
import os
import yaml
# Diccionario de mapeo entre los nombres de entrada y los nombres esperados por el modelo
FEATURE_NAME_MAPPING = {
    "fixed_acidity": "fixed acidity",
    "volatile_acidity": "volatile acidity",
    "citric_acid": "citric acid",
    "residual_sugar": "residual sugar",
    "chlorides": "chlorides",
    "free_sulfur_dioxide": "free sulfur dioxide",
    "total_sulfur_dioxide": "total sulfur dioxide",
    "density": "density",
    "pH": "pH",
    "sulphates": "sulphates",
    "alcohol": "alcohol",
}
def get_model_signature(artifacts_path="./artifacts"):
    """
    Lee el archivo MLmodel en los artefactos y extrae la firma del modelo.
    """
    mlmodel_path = os.path.join(artifacts_path, "MLmodel")

    # Verificar que el archivo existe
    if not os.path.exists(mlmodel_path):
        raise FileNotFoundError(f"No se encontró el archivo MLmodel en {mlmodel_path}")

    # Leer el archivo MLmodel
    with open(mlmodel_path, "r") as f:
        mlmodel_data = f.read()

    # Parsear el archivo como YAML
    mlmodel_dict = yaml.safe_load(mlmodel_data)

    # Extraer la firma del modelo
    signature = mlmodel_dict.get("signature", {})
    inputs = signature.get("inputs", "[]")  # Defaults a una lista vacía

    # Convertir los inputs de string a una lista de diccionarios
    inputs = json.loads(inputs)

    return inputs
def load_model():
    """
    Carga el modelo desde el archivo local `artifacts/model.pkl`.
    """
    model_path = "./artifacts/model.pkl"
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

def predict(model, input_data: dict):
    """
    Realiza una predicción con el modelo cargado.

    Args:
        model: El modelo cargado.
        input_data (dict): Datos de entrada como un diccionario con nombres de features.

    Returns:
        list: Lista de predicciones generadas por el modelo.
    """
    # Renombrar las características al formato esperado por el modelo
    input_data_renamed = {
        FEATURE_NAME_MAPPING[key]: value for key, value in input_data.items()
    }

    # Crear un DataFrame con los datos renombrados
    data = pd.DataFrame([input_data_renamed])

    # Realizar la predicción
    predictions = model.predict(data)

    # Convertir las predicciones a una lista y devolver
    return predictions.tolist()
