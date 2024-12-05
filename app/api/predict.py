from fastapi import APIRouter
from app.utils.mlflow_utils import load_model, predict, get_model_signature
from app.models.schemas import create_prediction_request_schema, PredictionResponse

# Crear el router
router = APIRouter()

# Cargar el modelo al iniciar
model = load_model()

# Obtener la firma del modelo y generar el esquema dinámico
model_inputs = get_model_signature()
PredictionRequest = create_prediction_request_schema(model_inputs)

@router.post("/predict", response_model=PredictionResponse)
async def make_prediction(request: PredictionRequest):
    """
    Endpoint para realizar predicciones con el modelo cargado.
    """
    # Convertir los datos de entrada a un diccionario
    input_data = request.dict()

    # Realizar la predicción
    predictions = predict(model, input_data)

    # Devolver las predicciones
    return {"predictions": predictions}