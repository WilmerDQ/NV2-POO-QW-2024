import tkinter as tk
from tkinter import messagebox, Listbox, END

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Campo de entrada
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Asignación de atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())  # Tecla "Enter"
        self.root.bind("c", lambda event: self.complete_task())   # Tecla "C"
        self.root.bind("d", lambda event: self.delete_task())     # Tecla "D"
        self.root.bind("<Delete>", lambda event: self.delete_task())  # Tecla "Delete"
        self.root.bind("<Escape>", lambda event: self.root.quit())  # Tecla "Escape"

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(END, task)
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(END, f"{task} (Completada)")
            self.task_listbox.itemconfig(END, {'fg': 'green'})
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
