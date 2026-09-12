class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        # Variables privadas (Encapsulación)
        self.__disponible = disponible  # variable privada para disponibilidad
        self.__prestado = 0

    # ---- GETTER para prestado ----
    def get_prestado(self):
        return self.__prestado

    # ---- SETTER para prestado ----
    # Recibe el nuevo valor, lo valida y lo guarda
    def set_prestado(self, nuevo_valor):
        if type(nuevo_valor) != int:
            raise ValueError("El valor debe ser un número entero")
        if nuevo_valor < 0:
            raise ValueError("El valor no puede ser negativo")
        self.__prestado = nuevo_valor

    # ---- GETTER para disponible ----
    def get_disponible(self):
        return self.__disponible

    # ---- SETTER para disponible ----
    def set_disponible(self, estado):
        if type(estado) != bool:
            raise ValueError("La disponibilidad debe ser True o False.")
        self.__disponible = estado

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {'Sí' if self.get_disponible() else 'No'}"

    def prestar(self):
        # Ahora llamamos a las funciones con párentesis ()
        if self.get_disponible():
            self.set_disponible(False)
            # Para sumar 1, primero obtenemos el valor actual, le sumamos 1 y luego lo guardamos
            prestamos_actuales = self.get_prestado()  # Obtenemos el valor actual
            self.set_prestado(prestamos_actuales + 1)

            return f"{self.titulo} ha sido prestado."
        else:
            return f"{self.titulo} no está disponible"

    def devolver(self):
        if not self.get_disponible():
            self.set_disponible(True)
            return f"{self.titulo} ha sido devuelto y disponible nuevamente."
        else:
            return f"{self.titulo} no puede ser devuelto."

    def es_popular(self):
        return self.get_prestado() >= 5


book1 = Libro(
    "Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0", True
)
book2 = Libro(
    "Don Quijote de la Mancha", "Miguel de Cervantes", "978-1-23-456789-0", False
)
book3 = Libro(
    "Harry Potter y la Piedra Filosofal", "J.K. Rowling", "978-0-12-345678-9", True
)


catalogo = [book1, book2, book3]

for libro in catalogo:
    print(libro)
    print(f"Prestado: {libro.get_prestado()} veces")
    print(f"Disponible: {'Sí' if libro.get_disponible() else 'No'}")
    print(f"¿Es Popular? {'Sí' if libro.es_popular() else 'No'}")
    print("-" * 40)
    print(libro.prestar())
    print(libro.devolver())
