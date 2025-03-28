from fastapi import APIRouter, HTTPException
from app.modelos.peliculas_modelo import Movie

router=APIRouter()
movies_db=[
    {"id":1,"titulo":"Inception","director":
    "Christopher Nolan","año": 2010,"rating":8.8},
    {"id":2,"titulo":"The Matrix","director": 
    "Lana Wachowski, Lilly Wachowski","año":1999,"rating":8.7},
    {"id":3 ,"titulo":"Casa Movie","director":
    "federico mapez","año": 2025,"rating":2.9},
]
@router.get("/movies")
def get_movies():
    """
    te da la lista de las peliculas
    retorna: list[dict] la lista de peliculas dentro de movies_db
    """
    return movies_db
@router.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    """
    se obtiene la pelicula por su ID
    movie_id (int): ID de la pelicula y retorna con dict sobre la info de la pelicula por su ID
    next(): se usa para obtener un elemento y si no lo encuentra te dara un None
    raise HTTPExcetion: te da un error 404 debido al id de la pelicula si no fue encontrada
    """
    movie=next((movie for movie in movies_db if movie["id"]==movie_id),None)
    if movie is None:
        raise HTTPException(status_code=404, detail="Película no ha sido encontrada")
    return movie
@router.post("/movies", status_code=201)
def create_movie(movie: Movie):
    """
    el usuario crea una nueva pelicula dentro de la base de datos de la pagina
    movie (Movie): el dato para crear una pelicula, retorna Movie: en cuando la pelicula ha sido creada
    raise HTTPException: si existe el ID de la pelicula dentro de la base de datos
    """
    for movie_in_db in movies_db:
        if movie_in_db["id"]==movie.id:
            raise HTTPException(status_code=400,detail="El ID de la pelicula ya existe")
    movies_db.append(movie.dict())
    return movie
@router.put("/movies/{movie_id}")
def update_movie(movie_id:int, updated_movie:Movie):
    """
    se actualiza los datos de una pelicula existente en la web o se crea otra si no existe
    movie_id (int): el ID de la pelicula
    update_movie (movie): se actualiza los datos de la pelicula
    raise HTTPExcetion: te da un error 404 debido al id de la pelicula si no fue encontrada
    """
    for index, movie in enumerate(movies_db):
        if movie["id"]==movie_id:
            movies_db[index]=updated_movie.dict()
            return updated_movie
    raise HTTPException(status_code=404,detail="Pelicula no ha sido encontrada")

@router.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    """
    elimina peliculas por el ID
    movie_id: el ID de la pelicula que se va a eliminarse
    retorna con un dict: un mensaje de confirmacion
    raise HTTPExcetion: te da un error 404 debido al id de la pelicula si no fue encontrada
    """
    global movies_db
    movies_db=[movie for movie in movies_db if movie["id"]!=movie_id]
    return {"mensaje": "La pelicula fue eliminada correctamente"}