import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def agregar_tarea(event=None):
    tarea = entry_tarea.get()
    if tarea != "":
        listbox_tareas.insert(tk.END, tarea)
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

# Función para marcar una tarea como completada
def marcar_como_completada():
    try:
        indice = listbox_tareas.curselection()[0]
        tarea = listbox_tareas.get(indice)
        listbox_tareas.delete(indice)
        listbox_tareas.insert(tk.END, f"{tarea} (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        indice = listbox_tareas.curselection()[0]
        listbox_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Campo de entrada para nuevas tareas
entry_tarea = tk.Entry(ventana, width=40)
entry_tarea.grid(row=0, column=0, padx=10, pady=10)

# Botón para añadir tarea
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.grid(row=0, column=1, padx=10, pady=10)

# Lista para mostrar las tareas
listbox_tareas = tk.Listbox(ventana, height=10, width=50, selectmode=tk.SINGLE)
listbox_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar como completada
btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_como_completada)
btn_completar.grid(row=2, column=0, padx=10, pady=5)

# Botón para eliminar tarea
btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.grid(row=2, column=1, padx=10, pady=5)

# Evento para añadir tarea con la tecla Enter
ventana.bind('<Return>', agregar_tarea)

# Ejecutar la aplicación
ventana.mainloop()
