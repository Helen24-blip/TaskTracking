import tkinter as tk
from tkinter import messagebox
import json  # Импорт модуля json для работы с файлами
import os

def add_task():
    task = task_entry.get() # здесь мы получаем слова из поля для ввода
    if task:
        task_listBox.insert(tk.END, task) # здесь с помощью константы END вставляем полученное слово в конец списка
        task_entry.delete(0, tk.END) # здесь очищаем поле для ввода, от нулевого индекса и до конца

def delete_task():
    selected_task = task_listBox.curselection() # с помощью функции **curselection** элемент, на который мы нажмём, будет передавать свой ID, индекс, в переменную  selected_task
    if selected_task:
        task_listBox.delete(selected_task) # удаляем выбранный элемент из списка

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="purple")
        # с помощью функции **itemconfig** выполненная задача изменит цвет заливки

# Функция для редактирования задачи
def edit_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task = task_listBox.get(selected_task)
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task)
        task_listBox.delete(selected_task)

# Функция для сохранения задач в файл
def save_tasks():
    tasks = task_listBox.get(0, tk.END)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    messagebox.showinfo("Сохранение", "Задачи сохранены успешно!")

# Функция для загрузки задач из файла
def load_tasks():
    if os.path.exists("tasks.json"):  # Проверка на существование файла
        if os.stat("tasks.json").st_size == 0:  # Проверка на пустоту файла
            return
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_listBox.insert(tk.END, task)

# Функция для сортировки задач
def sort_tasks():
    tasks = list(task_listBox.get(0, tk.END))
    tasks.sort()
    task_listBox.delete(0, tk.END)
    for task in tasks:
        task_listBox.insert(tk.END, task)


root = tk.Tk()
root.title("Task list")
root.configure(background= "#E0F7FA")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="MediumSeaGreen",fg="white")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="AliceBlue",fg="black")
task_entry.pack(pady = 10)

add_task_button = tk.Button(root, text="Добавить задачу",command=add_task, bg="LightCoral", activebackground="Tomato")
add_task_button.pack(pady=5)

edit_button = tk.Button(root, text="Редактировать задачу", command=edit_task, bg="LightCoral", activebackground="Tomato")
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task, bg="LightCoral", activebackground="Tomato")
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task, bg="LightCoral", activebackground="Tomato")
mark_button.pack(pady=5)

# Кнопка для сортировки задач
sort_button = tk.Button(root, text="Сортировать задачи", command=sort_tasks, bg="LightCoral", activebackground="Tomato")
sort_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:",bg="LightCoral", activebackground="Tomato")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="PaleTurquoise1")
task_listBox.pack(pady=10)

# Кнопка для сохранения задач
save_button = tk.Button(root, text="Сохранить задачи", command=save_tasks, bg="LightCoral", activebackground="Tomato")
save_button.pack(pady=5)

# Загрузка задач при старте
load_tasks()

root.mainloop()
