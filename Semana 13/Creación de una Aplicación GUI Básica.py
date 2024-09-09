import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_info():
    info = entry.get()
    if info:
        listbox.insert(tk.END, info)
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista
def limpiar_lista():
    listbox.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Crear y colocar los componentes
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=10)

entry = tk.Entry(ventana, width=40)
entry.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
