from typing import Optional
from pydantic import BaseModel

class Time(BaseModel):  # Classe no singular
    id: Optional[int] = None  # Já que é opcional
    nome: str
    posicao: int
    tecnico: str