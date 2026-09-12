class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True, count=0):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.count = count

    def __str__(self):
        return f"{self.titulo} por {self.autor} disponible: {self.disponible}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.count += 1
        return f"'{self.titulo}' prestado exitosamente"

    def es_popular(self):
        if self.count >= 5:
            return f"'{self.titulo}' es un libro popular"
        else:
            return f"'{self.titulo}' no es un libro popular"

    def devolver(self):
        self.disponible = True
        return f"'{self.titulo}' devuelto y disponible nuevamente"


mi_libro = Libro(
    "100 Años de Soledad", "Gabriel Garcia Marquez", "9781644734728", True, 5
)
otro_libro = Libro("El Principito", "Saint-Exupéry", "9781644731234728", True, 3)
un_libro = Libro("El Alquimista", "Paulo Coelho", "9781644731234728", True, 12)

catalogo = [mi_libro, otro_libro, un_libro]

for libro in catalogo:
    print(libro)
    print(libro.prestar())
    print(libro.es_popular())
    print(libro.devolver())
    print()
