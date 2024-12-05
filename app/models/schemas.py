from pydantic import BaseModel, create_model
from typing import Any

def create_prediction_request_schema(inputs):
    """
    Crea un esquema dinámico de entrada basado en los inputs del archivo MLmodel.

    Args:
        inputs (list): Lista de diccionarios con la estructura de entrada del modelo.

    Returns:
        BaseModel: Clase Pydantic para validar los datos de entrada.
    """
    # Crear un diccionario para los campos del esquema dinámico
    fields = {
        input_["name"].replace(" ", "_"): (float, ...) for input_ in inputs
    }

    # Crear un modelo dinámico usando Pydantic
    PredictionRequest = create_model("PredictionRequest", **fields)
    return PredictionRequest

class PredictionResponse(BaseModel):
    """
    Esquema de salida, estático, ya que las predicciones son siempre una lista de floats.
    """
    predictions: list[float]