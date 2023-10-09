from app.model.schemas import CreateModelSchema
import pandas as pd
import pickle
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from datetime import datetime

regresor_path = open('./app/model/regresor.pkl', 'rb')
regresor_model = pickle.load(regresor_path)

clasificador_path = open('./app/model/clasificador.pkl', 'rb')
clasificador_model = pickle.load(clasificador_path)

# Luego pasar esto a una vista de configuraciones desde el frontend
JUNE = 6
SEPTEMBER = 9
TRESHOLD_TURBIDITY = 3.0
RANGE_LOW_HOUR = 8
RANGE_HIGHT_HOUR = 20

class ModelService:
    def calcule_turbiedad(model: CreateModelSchema):
        today = datetime.today()
        hour = today.hour
    
        clasificador_intradia = 0 if hour >= RANGE_LOW_HOUR and hour <= RANGE_HIGHT_HOUR else 1
        if model.turbiedad < TRESHOLD_TURBIDITY and clasificador_intradia == 0:
            return {
                'regresor': 'No Aplicar',
                'clasificador': 'No Aplicar'
            }

        month = today.month
        clasificador_mensual = 0.0 if month >= JUNE and month <= SEPTEMBER else 1.0
    
        data = {
            'caudal': [model.caudal],
            'agua_cruda_p_h': [model.agua_cruda_ph],
            'agua_cruda_color': [model.agua_cruda_color],
            'agua_cruda_alcalinidad': [model.agua_cruda_alcalinidad],
            'agua_cruda_conductividad': [model.agua_cruda_conductividad],
            'vel_viento': [model.vel_viento],
            'precipitacion': [model.precipitacion],
            'temp_humeda': [model.temp_humeda],
            'clasificador_mensual': [clasificador_mensual],
        }

        input_data = pd.DataFrame(data)
        regresor = regresor_model.predict(input_data)
        clasificador = clasificador_model.predict(input_data)

        return {
            'regresor': regresor[0],
            'clasificador': clasificador[0]
        }