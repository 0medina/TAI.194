#librerias
from fastapi import FastAPI, HTTPException
from typing import Optional, List

app = FastAPI(
    title="API de Gestión de Tareas",
    description="Gestión de tareas académicas para Ingeniería en Sistemas Computacionales",
    version="1.0.0"
)

# base de datos simulada
tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de TAI", "vencimiento": "2024-02-14", "estado": "completada", "profesor": "Isay"},
    {"id": 2, "titulo": "Investigar sobre IA", "descripcion": "Leer sobre redes neuronales", "vencimiento": "2024-02-18", "estado": "no completada", "profesor": "Javier"},
    {"id": 3, "titulo": "Desarrollar API REST", "descripcion": "Crear endpoints en FastAPI", "vencimiento": "2024-02-20", "estado": "no completada", "profesor": "Cecilia"},
    {"id": 4, "titulo": "Terminar proyecto de software", "descripcion": "Finalizar código del sistema de gestión", "vencimiento": "2024-02-25", "estado": "completada", "profesor": "Julio"},
    {"id": 5, "titulo": "Leer sobre estructuras de datos", "descripcion": "Revisar listas, pilas y colas", "vencimiento": "2024-03-02", "estado": "no completada", "profesor": "Isay"},
    {"id": 6, "titulo": "Resolver ejercicios de lógica", "descripcion": "Practicar problemas de programación competitiva", "vencimiento": "2024-03-05", "estado": "completada", "profesor": "Javier"},
    {"id": 7, "titulo": "Aprender FastAPI", "descripcion": "Ver tutoriales y practicar", "vencimiento": "2024-03-10", "estado": "no completada", "profesor": "Cecilia"}
]

#endpoint de inicio 
@app.get("/", tags=['Inicio'])
def main():
    return {"message": "¡Bienvenido a la API de Gestión de Tareas!"}

#endpoint obtener todas las tareas
@app.get("/tareas", tags=['Operaciones CRUD'])
def obtener_todas_las_tareas():
    return {'Tareas Registradas': tareas}

#enpointe obtener una tarea por ID
@app.get("/tareas/{id}", tags=['Operaciones CRUD'])
def obtener_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#endpoint crear una nueva tarea
@app.post("/tareas", tags=['Operaciones CRUD'])
def crear_tarea(tarea: dict):
    for t in tareas:
        if t['id'] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="La tarea ya existe")
    tareas.append(tarea)
    return tarea

#endpoint actualizar
@app.put("/tareas/{id}", tags=['Operaciones CRUD'])
def actualizar_tarea(id: int, tarea_actualizada: dict):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas[index].update(tarea_actualizada)
            return tareas[index]
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
