from pydantic import BaseModel, Field
from typing import List

class Alumno(BaseModel):
    nombre: str
    apellidos: str
    matricula: str
    edad: int
    materias: List[str]

class Config:
    schema_extra = {
        "example": {
            "nombre": "Ricardo",
            "apellidos": "Guerrero",
            "matricula": "12345",
            "edad": 24,
            "materias":["IA", "ML", "DM"]
        }
    }