import pandas as pd
from typing import Optional
import joblib
from DataModel import DataModel
from fastapi import FastAPI
from fastapi import Request

app = FastAPI()

# Cargar el modelo una sola vez al iniciar la aplicación
model = joblib.load("linear_regression_pipeline.joblib")


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame([dataModel.dict()])
    df.columns = dataModel.columns()
    result = model.predict(df)
    return {"prediction": result.tolist()}



@app.post("/predict")
async def make_predictions(request: Request):
    data = await request.json()
    print("Datos recibidos:", data)  # Para ver si los datos llegan bien
    return {"message": "Datos recibidos"}

