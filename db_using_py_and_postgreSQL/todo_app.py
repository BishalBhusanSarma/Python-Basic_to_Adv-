import tkinter as tk
import psycopg2
from tkinter import *
root = tk.Tk()

hostname = "localhost"
database = "students"
username = "postgres"
pw = "1234"
port = 5432
conn = None
cur = None

conn = psycopg2.connect(host = hostname,
                                dbname = database,
                                user = username,
                                password = pw,
                                port = port)

cur = conn.cursor()
    
table = cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
                            id SERIAL PRIMARY KEY,
                            task TEXT NOT NULL,
                            completed BOOLEAN DEFAULT FALSE)''')
    


cur.execute("SELECT * FROM tasks")
rows = cur.fetchall()






def add_t():
    task = enter_task.get()
    if task != "":
        task_list.insert(tk.END, task)
        cur.execute('INSERT INTO tasks (task) VALUES (%s)', (task, ))
        conn.commit()
        enter_task.delete(0, tk.END)


def del_t():
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        
        task = task_list.get(index)
        task_list.delete(index)
        cur.execute('DELETE FROM tasks WHERE task = %s', (task,))
        conn.commit()

def comp_t():
    selected = task_list.curselection()
    if selected:
        index = selected[0]


        task = task_list.get(index)

        if "completed" in task:
            update_task = task.replace(" (completed)", "")

            cur.execute("UPDATE tasks SET completed = %s where task = %s", (False, update_task))
            
            
        else:
            update_task = f"{task} (completed)"
            cur.execute(
                "UPDATE tasks SET completed = %s WHERE task = %s",
                (True, task)
            )

        # Update database
        cur.execute(
            "UPDATE tasks SET task = %s WHERE task = %s",
            (update_task, task)
        )
        conn.commit()

        task_list.delete(index)
        task_list.insert(index, update_task)
        

root.title("I'm your todo list")
root.geometry("800x800")
root.configure(background="#BFEABF")

text_label= Label(root, text="Enter task", fg="#000000", bg="#BFEABF")
text_label.pack(pady=10)
text_label.config(font=('Verdana', 24))

enter_task = tk.Entry(root, width=30, background="#D1FFAF", fg="#000000")
enter_task.pack(ipady=10, ipadx=10)
enter_task.config(font=('Arial', 20))



button_frame = tk.Frame(root, background="#EFE9C7")
button_frame.pack(ipady = 10)
# add task button
add_task_button = tk.Button(button_frame, text="Enter",  fg="#0A0A0A", command=add_t)
add_task_button.pack(side=tk.LEFT, pady=10, padx=10)
add_task_button.config(font=('Arial', 20))

# delete task button
delete_task_button = tk.Button(button_frame, text="Delete",  fg="#0A0A0A", command=del_t)
delete_task_button.pack(side=tk.LEFT, pady=10, padx=10)
delete_task_button.config(font=('Arial', 20))

#completed task button
Complete_task_button = tk.Button(button_frame, text="Mark as complete",  fg="#0A0A0A", command=comp_t)
Complete_task_button.pack(side=tk.LEFT, pady=10, padx=10)
Complete_task_button.config(font=('Arial', 20))


task_list = tk.Listbox(
    root,
    width=40,
    height=15,
    font=('Arial', 18),
    bg="#FFFFFF",
    fg="#000000"
)
task_list.pack(pady=10)




for row in rows:
    task_list.insert(tk.END, row[1])



conn.commit()

tk.mainloop()
conn.close()