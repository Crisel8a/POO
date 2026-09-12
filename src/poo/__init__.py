class Libro:
    def __init__(self, titulo, autor, paginas, dospos=None):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.dospos = dospos


mi_libro = Libro(
    "El Principito", "Antoine de Saint-Exupéry", 96, dospos="Edición especial"
)
otro_libro = Libro("1984", "George Orwell", 328, dospos="Edición de bolsillo")
un_libro = Libro(
    "Cien Años de Soledad", "Gabriel García Márquez", 417, dospos="Edición de lujo"
)

catalogo = [mi_libro, otro_libro, un_libro]

for libro in catalogo:
    print(
        f"Título: {libro.titulo}, Autor: {libro.autor}, Páginas: {libro.paginas}, Dospos: {libro.dospos}"
    )
