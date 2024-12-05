from fastapi import FastAPI
from app.api import predict

# Crear la instancia de FastAPI
app = FastAPI(
    title="ML Model Inference API",
    description="API para inferencias usando un modelo registrado en MLflow",
    version="1.0.0",
)

# Incluir las rutas de la API
app.include_router(predict.router, prefix="/api")