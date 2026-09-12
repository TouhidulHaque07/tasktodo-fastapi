
from fastapi import FastAPI
from pydantic import BaseModel
import os
import sqlite3
from datetime import datetime

os.makedirs("data", exist_ok=True)


app=FastAPI()

conn = sqlite3.connect("data/tasks.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done INTEGER,
        created_at TEXT
    )
""")
conn.commit()
conn.close()


@app.get("/")
def read_root():
    return{"message":"Hellow! Fast API!"}

@app.get("/task/{task_id}")
def get_task(task_id:int):
    return{"Task_ ID":task_id}

@app.get("/search")
def search_item(keyword:str="", limit:int=10):
    return {"Keyword":keyword, "Limit":limit}


class Item(BaseModel):
    name: str
    price: float
    secret_code:str

class ItemPublic(BaseModel):
    name: str
    price: float

class TaskCreated(BaseModel):
    title: str

@app.post("/item", response_model=ItemPublic)
def create_item(item: Item):
    return item

@app.post("/tasks")
def add_task(task: TaskCreated):
    conn=sqlite3.connect("data/tasks.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO tasks (title, done, created_at) VALUES(?,?,?)", 
                   (task.title,0,datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return {"Message":"Task Add", "Title":task.title}


@app.get("/task")
def view_task():
    conn=sqlite3.connect("data/tasks.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows=cursor.fetchall()

    dataList=[]
    for row in rows:
        dataList.append(dict(row))

    return dataList

@app.delete("/delete/{task_id}")
def delete_task(task_id:int):
    conn=sqlite3.connect("data/tasks.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM tasks where id=?",(task_id,))
    conn.commit()
    conn.close()
    return {"Message":"Task delete successfully","Task Id":task_id}

@app.put("/update/{task_id}")
def uptate_task(task_id:int):
    conn=sqlite3.connect("data/tasks.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE tasks SET done= ? WHERE id= ?", (1,task_id))
    conn.commit()
    conn.close()
    return {"Message:":"Task update successfully","Task Id":task_id}