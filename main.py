import json
from pathlib import Path

from fastapi import FastAPI

app = FastAPI()

def load_data():
    data_path = Path(__file__).resolve().parent / 'patient.json'
    with data_path.open('r') as f:
        data = json.load(f)
        
    return data
        
        

@app.get("/")
def hello():
    return {'message' : 'Patient Management System'}

@app.get('/about')
def about():
    return {'message' : 'A fully functional API to manage Patient records'}

@app.get('/view')
def view():
    data = load_data()
    
    return data
    
@app.get('/patient/{patient_id}')
def view_patient(patient_id :str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {'error : Patient data Not Found'}

    
