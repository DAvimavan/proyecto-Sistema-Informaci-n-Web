from pydantic import BaseModel
from typing import Union

class Product(BaseModel):
    nombreProduct: str
    descripcionProduct: str 
    precio: float
    disponibilidad: bool


class Usuario (BaseModel):
        nombreUsuario: str
        email: str
        contrasena: str

