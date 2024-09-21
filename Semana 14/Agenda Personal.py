import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Función para agregar un nuevo evento a la lista
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, completa todos los campos.")

# Función para eliminar el evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este evento?")
        if confirmacion:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("Selección inválida", "Por favor, selecciona un evento para eliminar.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_fecha.set_date('')
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Crear el Frame para los eventos
frame_eventos = tk.Frame(ventana)
frame_eventos.pack(pady=10)

# Crear el Treeview para mostrar los eventos
tree = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Crear el Frame para la entrada de datos
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Etiquetas y campos de entrada
label_fecha = tk.Label(frame_entrada, text="Fecha:")
label_fecha.grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_entrada, date_pattern='y-mm-dd')
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

label_hora = tk.Label(frame_entrada, text="Hora:")
label_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Crear el Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Botones para agregar, eliminar y salir
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=5, pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
