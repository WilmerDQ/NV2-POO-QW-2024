class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"'{self.titulo}' de {self.autor} - {self.categoria} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

    def listar_libros_prestados(self):
        return self.libros_prestados


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para libros con ISBN como clave
        self.usuarios = set()  # Conjunto para IDs de usuarios únicos

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido quitado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn} en la biblioteca.")

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario in {usuario.id_usuario for usuario in self.usuarios}:
            print(f"El ID de usuario {id_usuario} ya está registrado.")
        else:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios.add(usuario)
            print(f"Usuario '{nombre}' registrado con ID {id_usuario}.")

    def dar_baja_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if libro and usuario:
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
            else:
                print(f"El libro '{libro.titulo}' ya está prestado a '{usuario.nombre}'.")
        else:
            if not libro:
                print(f"No se encontró el libro con ISBN {isbn}.")
            if not usuario:
                print(f"No se encontró el usuario con ID {id_usuario}.")

    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if libro and usuario:
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por '{usuario.nombre}'.")
            else:
                print(f"El libro '{libro.titulo}' no está prestado a '{usuario.nombre}'.")
        else:
            if not libro:
                print(f"No se encontró el libro con ISBN {isbn}.")
            if not usuario:
                print(f"No se encontró el usuario con ID {id_usuario}.")

    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, k) == v for k, v in kwargs.items()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            return usuario.listar_libros_prestados()
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return []


# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "1234567890")
libro2 = Libro("1984", "George Orwell", "Distopía", "0987654321")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario("Alice", "u001")
biblioteca.registrar_usuario("Bob", "u002")

# Prestar y devolver libros
biblioteca.prestar_libro("1234567890", "u001")
print("Libros prestados a Alice:", biblioteca.listar_libros_prestados("u001"))

biblioteca.devolver_libro("1234567890", "u001")
print("Libros prestados a Alice después de devolver:", biblioteca.listar_libros_prestados("u001"))

# Buscar libros
print("Buscar libros por título '1984':", biblioteca.buscar_libro(titulo="1984"))
