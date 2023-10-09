from datetime import datetime

from humps import camelize
from pydantic import BaseModel as BaseSchema


def to_camelcase(value):
    return camelize(value)


class ModelBase(BaseSchema):
    agua_cruda_ph: float
    agua_cruda_color: float
    agua_cruda_alcalinidad: float
    agua_cruda_conductividad: float
    vel_viento: float
    precipitacion: float
    temp_humeda: float
    caudal: float
    turbiedad: float

class ModelSchema(ModelBase):
    class Config:
        alias_generator = to_camelcase
        populate_by_name = True


class CreateModelSchema(ModelSchema):
    pass
