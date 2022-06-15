import uvicorn
from fastapi import File, FastAPI, UploadFile
import numpy as np
import pandas as pd
from model_dev import prep_data_utils as prep

import mlflow
import mlflow.h2o
from mlflow.tracking import MlflowClient
from mlflow.entities import ViewType

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}

@app.post("/model/predict")
def predict(file: UploadFile = File(...)):
    """
    Predict the outcome of the uploaded file.
    """
    # load the file
    data = pd.read_csv(file.file)
    # process the data
    data = prep.preprocess_data(data)
    # call the model to predict the outcome
    return data


