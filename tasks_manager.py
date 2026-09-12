
import sqlite3
from datetime import datetime

conn=sqlite3.connect("tasks.db")

cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        done INTEGER, 
        created_at TEXT
    )
''')

conn.commit()
conn.close()

def add_task(title):
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()
    created_time=datetime.now().isoformat()
    cursor.execute("INSERT INTO tasks (title,done,created_at) VALUES(?,?,?)",(title,0,created_time))
    conn.commit()
    conn.close()

def view_task():
    conn=sqlite3.connect("tasks.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks=cursor.fetchall()
    #print(tasks)
    for i, task in enumerate(tasks, start=1):
        #print(task)
        if task["done"]==1:
            mark="\u2714"
        else:
            mark=" "
        print(f"{i}. [{mark}]{task['title']} {task['created_at']}")

    conn.close()

def complete_task(task_id):

    conn=sqlite3.connect("tasks.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    cursor.execute("UPDATE tasks SET done= ? WHERE id= ?", (1,task_id))
    conn.commit()
    conn.close()
    view_task()

def delete_task(task_id):
    conn=sqlite3.connect("tasks.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    cursor.execute("DELETE FROM tasks where id=?",(task_id,))
    conn.commit()
    conn.close()
    view_task()

def display_menu():
    print("========Main Menu=======")
    print("1. Add Task.")
    print("2. View Tasks.")
    print("3. Complete Tasks.")
    print("4. Delete Task.")
    print("5. Exit.")

def main():

    while True:
        display_menu()
        
        try:
            choice=input("Enter Your Choice (1-5): ").strip()
            if choice=="1":
                #add_task("task1")
                task=input("Please Enter Your Task:")
                add_task(task)
            elif choice=="2":
                view_task()
            elif choice=="3":
                complete_task_id=int(input("Please Enter Task id which is you complete:"))
                complete_task(complete_task_id)
            elif choice=="4":
                delete_task_id=int(input("Please Enter task id which is you want delete:"))
                delete_task(delete_task_id)
            elif choice=="5":
                print("Exiting Program----Thank You")
                break
            else:
                print("Invalid option.. Please enter 1, 2, 3 ..")
        except ValueError:
            print("Plese Enter only digit")
               

if __name__=="__main__":
    main()






#complete_task(1)
#delete_task(1)

