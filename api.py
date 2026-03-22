from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()

model = pickle.load(open("house_rent.pkl","rb"))

class HouseData(BaseModel):
    Total_Bedrooms:int
    Total_Bathrooms:int
    Living_area:float
    Lot_area:float
    Total_floors:int
    House_condition:int
    House_grade:int
    Total_area:float
    Basement_area:float
    Built_year:int
    Renovation_year:int
    School_nearby:int
    Airport_distance:float


@app.get("/")
def home():
    return {"message":"House Price Prediction API"}


@app.post("/predict")
def predict(data:HouseData):

    df = pd.DataFrame([data.dict()])

    prediction = model.predict(df)

    return {"Predicted_price":float(prediction[0])}