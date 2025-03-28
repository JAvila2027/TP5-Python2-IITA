from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    """
    una clase sobre peliculas
    id (int): identificador de las peliculas
    titulo (str): titulo de la pelicula
    director (str): el director
    año (int): el año en el que salio
    rating (Optional[float]): es el rating o puntaje sobre una pelicula
    """
    id:int
    titulo:str
    director:str
    año:int
    rating:Optional[float]=None 