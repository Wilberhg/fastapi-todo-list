from fastapi import FastAPI
from random import randint

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Atividade ADICIONADA com sucesso!"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: str):
    tasks[task_id-1] = task
    return {"message": "Atividade ATUALIZADA com sucesso!"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks.pop(task_id-1)
    return {"message": "Atividade DELETADA com sucesso!"}