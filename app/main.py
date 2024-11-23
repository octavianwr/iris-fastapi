from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load the trained model
with open("app/iris_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define the data model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Prediction API"}

@app.post("/predict/")
def predict_species(input_data: IrisInput):
    data = np.array([[input_data.sepal_length, input_data.sepal_width,
                      input_data.petal_length, input_data.petal_width]])
    prediction = model.predict(data)
    species = ["setosa", "versicolor", "virginica"]
    return {"species": species[prediction[0]]}
