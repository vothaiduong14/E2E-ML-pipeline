import uvicorn
from fastapi import File, FastAPI, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse
import numpy as np
import pandas as pd
import utils as utils

import mlflow
from mlflow import pyfunc
from io import BytesIO

app = FastAPI()

# load the model
model = pyfunc.load_model('Modelfile/model')

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}

@app.post("/predict")
async def get_prediction(file: UploadFile = File(...)):
    """
    Predict the outcome of the uploaded file.
    """
    # load the file
    contents = await file.read()
    buffer = BytesIO(contents)
    df = pd.read_csv(buffer)
    buffer.close()

    # process the data
    processor = utils.DataProcessor(df)
    processor.process_data()
    df = processor.df
    id_col = processor.id_col

    # predict the outcome
    pred = model.predict(df)

    # for H2O, we need to get the 'predict' column from the dataframe
    result = pd.DataFrame(id_col, columns=['id'])
    result['predict'] = pred['predict']
    
    return result.to_json(orient='records')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)