"""
Tp Nº5 de python
nombre y apellido: Joaquin Avila
"""
"""

Trabajo Práctico: Desarrollo de una API REST con FastAPI
Objetivo: Desarrollar una aplicación utilizando el framework FastAPI, implementando una API REST con una arquitectura en capas. La temática de la API es de libre elección, permitiendo explorar diferentes enfoques y modelos de aplicación.

Requisitos:

La aplicación debe estar basada en FastAPI y cumplir con los principios de una API REST.
Se debe implementar una arquitectura en capas, asegurando la separación de responsabilidades y manteniendo buenas prácticas en el desarrollo de software.
La temática de la API es libre. Se permite utilizar una API de terceros para mapear su formato o estructurar los datos según convenga al diseño de la aplicación.
Los estudiantes pueden aprovechar esta oportunidad para desarrollar un prototipo de su proyecto final del curso, en caso de que sea aplicable. Sin embargo, esto no aplica en proyectos grupales, ya que este trabajo es de carácter individual.
Se recomienda utilizar como referencia la siguiente implementación de arquitectura: FastAPI Example. No obstante, es posible utilizar otra estructura, siempre y cuando se sigan las buenas prácticas de desarrollo en Python.
Criterios de Evaluación:

Correcta implementación de la arquitectura en capas.
Uso adecuado de FastAPI y sus funcionalidades.
Aplicación de buenas prácticas de programación en Python.
Documentación clara del código y uso de Swagger (OpenAPI) para la especificación de la API.
Calidad y coherencia del diseño de la API.
Entrega: Cada estudiante deberá subir su código a un repositorio en GitHub, proporcionando un archivo README con instrucciones claras sobre cómo ejecutar la aplicación y probar sus endpoints.
"""

from fastapi import FastAPI
from app.control.peliculas import router as movies_router

app=FastAPI()
app.include_router(movies_router)